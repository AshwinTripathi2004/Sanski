import sys
import os
import math

# --- Global Storage ---
variables = {} 
functions = {}
classes = {}

# --- Helper Classes for Control Flow ---
class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value
class BreakLoop(Exception): pass
class ContinueLoop(Exception): pass

# --- Helper Classes for OOP ---
class SanskiClass:
    """Represents a class definition in Sanski."""
    def __init__(self, name, parent, constructor, methods):
        self.name = name
        self.parent = parent # --- NEW: Reference to the parent class ---
        self.constructor = constructor
        self.methods = methods

class SanskiObject:
    """Represents an instance of a SanskiClass."""
    def __init__(self, class_ref):
        self.class_ref = class_ref
        self.properties = {}

# --- Helper Class for Functions ---
class Function:
    """Represents a user-defined function or a class method."""
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def execute(self, args, instance=None):
        """Executes the function/method."""
        local_scope = variables.copy()
        if instance:
            if not self.params or self.params[0] != 'svayam':
                raise TypeError(f"Method '{self.name}' must have 'svayam' as its first parameter.")
            local_scope['svayam'] = instance
            expected_args = len(self.params) - 1
        else:
            expected_args = len(self.params)

        if len(args) != expected_args:
            raise TypeError(f"Truti: {self.name}() takes {expected_args} arguments but {len(args)} were given")

        param_offset = 1 if instance else 0
        for i, arg in enumerate(args):
            local_scope[self.params[i + param_offset]] = arg
            
        try:
            execute_block(self.body, local_scope)
        except ReturnValue as ret:
            return ret.value
        return None

# --- Built-in Sanski Functions ---
def vad(statement, scope):
    try: print(eval_sanski(statement, scope))
    except Exception as e: print(f"Truti (Error) in 'vad': {e}")
def grahan_karo(prompt=""): return input(prompt)
def jodo(a_list, item):
    if isinstance(a_list, list): a_list.append(item)
    else: raise TypeError("Truti: 'jodo' function can only be used with lists.")
    return a_list
def lambai(data):
    if isinstance(data, (list, str, dict)): return len(data)
    else: raise TypeError("Truti: 'lambai' function can only be used with lists, strings, or dictionaries.")
def file_kholo(filename, mode="r"): return open(filename, mode, encoding='utf-8')
def file_likho(file_object, data): file_object.write(str(data))
def file_padho(file_object): return file_object.read()
def file_band_karo(file_object): file_object.close()
def string_upper(text): return str(text).upper()
def string_lower(text): return str(text).lower()
def string_replace(text, old, new): return str(text).replace(str(old), str(new))
def string_split(text, separator=","): return str(text).split(str(separator))
def string_strip(text): return str(text).strip()

# --- Core Interpreter Logic ---
def eval_sanski(expression, scope):
    """Evaluates an expression, handling variables, properties, and function/class instantiation."""
    expression = expression.strip()

    if '.' in expression and '(' not in expression:
        obj_name, prop_name = expression.split('.', 1)
        obj = eval_sanski(obj_name, scope)
        if isinstance(obj, SanskiObject):
            return obj.properties.get(prop_name)
        else:
            raise TypeError(f"Truti: Cannot access property '{prop_name}' on a non-object.")

    start_paren = expression.find('(')
    end_paren = expression.rfind(')')
    if start_paren != -1 and end_paren != -1 and end_paren > start_paren:
        func_name = expression[:start_paren].strip()
        arg_str = expression[start_paren + 1 : end_paren]
        args = [eval_sanski(arg.strip(), scope) for arg in arg_str.split(',')] if arg_str else []

        if func_name in classes:
            class_def = classes[func_name]
            instance = SanskiObject(class_def)
            
            # --- NEW: Implicitly call parent constructors ---
            parent_chain = []
            current_class = class_def
            while current_class.parent:
                parent_chain.append(current_class.parent)
                current_class = current_class.parent
            
            for parent_class in reversed(parent_chain):
                if parent_class.constructor:
                    # Simple model: parent constructors are called with no arguments
                    parent_class.constructor.execute([], instance)

            if class_def.constructor:
                class_def.constructor.execute(args, instance)
            return instance
        elif func_name in functions:
            return functions[func_name](*args)

    return eval(expression, functions, scope)

def execute_block(block_lines, scope):
    i = 0
    while i < len(block_lines):
        try:
            i = execute(block_lines, i, scope)
        except ContinueLoop: continue
        except BreakLoop: break

def find_block_end(lines, start_index):
    if start_index >= len(lines): return start_index
    first_line_index = -1
    for i in range(start_index, len(lines)):
        if lines[i].strip():
            first_line_index = i
            break
    if first_line_index == -1: return len(lines)
    indent_level = len(lines[first_line_index]) - len(lines[first_line_index].lstrip())
    if indent_level == 0: return start_index + 1
    block_end = first_line_index + 1
    while block_end < len(lines):
        line = lines[block_end]
        if line.strip() == "":
            block_end += 1
            continue
        current_indent = len(line) - len(line.lstrip())
        if current_indent < indent_level: break
        block_end += 1
    return block_end

def execute(lines, index, scope):
    line = lines[index].strip()
    if not line or line.startswith("#"): return index + 1
    if line == "roko": raise BreakLoop()
    if line == "jaari_rakho": raise ContinueLoop()
    if line.startswith("vapasi"):
        expr = line.replace("vapasi", "").strip()
        raise ReturnValue(eval_sanski(expr, scope))

    dot_pos = line.find('.')
    paren_pos = line.find('(')
    if dot_pos != -1 and paren_pos != -1 and dot_pos < paren_pos:
        try:
            obj_expr, rest = line.split('.', 1)
            method_name = rest.split('(')[0].strip()
            arg_str = rest[len(method_name)+1:-1]
            args = [eval_sanski(arg.strip(), scope) for arg in arg_str.split(',')] if arg_str else []
            
            obj_instance = eval_sanski(obj_expr, scope)
            if isinstance(obj_instance, SanskiObject):
                # --- NEW: Search for method up the inheritance chain ---
                method_found = False
                current_class = obj_instance.class_ref
                while current_class:
                    if method_name in current_class.methods:
                        method = current_class.methods[method_name]
                        method.execute(args, obj_instance)
                        method_found = True
                        break
                    current_class = current_class.parent
                
                if not method_found:
                    raise NameError(f"Truti: Object has no method named '{method_name}'")
            else:
                raise TypeError("Truti: Cannot call a method on a non-object.")
            return index + 1
        except Exception as e:
            print(f"Truti (Error) executing method: {e}")
            return index + 1

    elif line.startswith("rachay"):
        try:
            full_line_str = line
            next_index = index + 1
            open_braces = line.count('{') + line.count('[')
            close_braces = line.count('}') + line.count(']')
            if ("=" in line) and (open_braces > close_braces):
                while next_index < len(lines) and open_braces > close_braces:
                    next_line_content = lines[next_index]
                    full_line_str += next_line_content
                    open_braces += next_line_content.count('{') + next_line_content.count('[')
                    close_braces += next_line_content.count('}') + next_line_content.count(']')
                    next_index += 1
            
            final_statement = full_line_str.replace('\n', ' ').strip()
            parts = final_statement.replace("rachay", "").strip().split("=", 1)
            target_expr = parts[0].strip()
            value_expr = parts[1].strip()
            value = eval_sanski(value_expr, scope)

            if '[' in target_expr and ']' in target_expr:
                exec(f"{target_expr} = value", {"value": value}, scope)
            elif '.' in target_expr:
                obj_name, prop_name = target_expr.split('.', 1)
                obj = eval_sanski(obj_name, scope)
                if isinstance(obj, SanskiObject):
                    obj.properties[prop_name] = value
                else:
                    raise TypeError("Truti: Cannot set property on a non-object.")
            else:
                 scope[target_expr] = value
            return next_index
        except Exception as e:
            print(f"Truti (Error) in 'rachay': {e}")
            return index + 1
    
    elif line.startswith("vad("):
        if line.endswith(')'):
            content = line[len("vad("):-1]
            vad(content, scope)
        else:
            print(f"Syntax Truti: Missing closing parenthesis in '{line}'")
        return index + 1
    elif line.startswith("har_ek"):
        try:
            parts = line.split()
            iterator_var, iterable_name = parts[1], parts[3][:-1]
            iterable_obj = eval_sanski(iterable_name, scope)
            block_start = index + 1
            block_end = find_block_end(lines, block_start)
            loop_body = lines[block_start:block_end]
            for item in iterable_obj:
                try:
                    loop_scope = scope.copy()
                    loop_scope[iterator_var] = item
                    execute_block(loop_body, loop_scope)
                except ContinueLoop: continue
                except BreakLoop: break
            return block_end
        except Exception as e:
            print(f"Truti (Error) in 'har_ek' loop: {e}")
            return find_block_end(lines, index + 1)
    else:
        try:
            eval_sanski(line, scope)
        except Exception as e:
            print(f"Agyat nirdesh (Unknown instruction) or Truti: {e} in line '{line}'")
        return index + 1

def process_file(lines, current_file_path, imported_files):
    """Processes a list of lines, handling imports, classes, functions, and executing code."""
    
    # 1. First Pass: Find and define all classes
    remaining_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("varg"):
            # --- NEW: Handle inheritance syntax like varg Child(Parent): ---
            header = line.replace("varg", "").strip()[:-1]
            parent_name = None
            if '(' in header and ')' in header:
                class_name = header.split('(')[0].strip()
                parent_name = header[header.find('(')+1:header.find(')')].strip()
            else:
                class_name = header

            parent_class = None
            if parent_name:
                if parent_name in classes:
                    parent_class = classes[parent_name]
                else:
                    raise NameError(f"Truti: Parent class '{parent_name}' not found.")

            body_start = i + 1
            body_end = find_block_end(lines, body_start)
            class_body = lines[body_start:body_end]
            
            constructor = None
            methods = {}
            j = 0
            while j < len(class_body):
                m_line = class_body[j].strip()
                if m_line.startswith("rachna"):
                    m_header = m_line.replace("rachna", "").strip()[:-1]
                    param_str = m_header[m_header.find('(')+1:m_header.rfind(')')]
                    params = [p.strip() for p in param_str.split(',')] if param_str else []
                    m_body_start = j + 1
                    m_body_end = find_block_end(class_body, m_body_start)
                    constructor = Function("__init__", params, class_body[m_body_start:m_body_end])
                    j = m_body_end
                elif m_line.startswith("karya"):
                    m_header = m_line.replace("karya", "").strip()[:-1]
                    method_name = m_header.split('(')[0].strip()
                    param_str = m_header[m_header.find('(')+1:m_header.rfind(')')]
                    params = [p.strip() for p in param_str.split(',')] if param_str else []
                    m_body_start = j + 1
                    m_body_end = find_block_end(class_body, m_body_start)
                    methods[method_name] = Function(method_name, params, class_body[m_body_start:m_body_end])
                    j = m_body_end
                else:
                    j += 1

            classes[class_name] = SanskiClass(class_name, parent_class, constructor, methods)
            i = body_end
        else:
            remaining_lines.append(lines[i])
            i += 1

    # 2. Second Pass: Find and define all global functions
    main_code_lines = []
    i = 0
    while i < len(remaining_lines):
        line = remaining_lines[i].strip()
        if line.startswith("karya"):
            header = line.replace("karya", "").strip()[:-1]
            func_name = header.split('(')[0].strip()
            param_str = header[len(func_name)+1:header.rfind(')')]
            params = [p.strip() for p in param_str.split(',')] if param_str else []
            body_start = i + 1
            body_end = find_block_end(remaining_lines, body_start)
            func_body = remaining_lines[body_start:body_end]
            functions[func_name] = lambda *args, f=Function(func_name, params, func_body): f.execute(args)
            i = body_end
        else:
            main_code_lines.append(remaining_lines[i])
            i += 1
    
    # 3. Third Pass: Execute main code and imports
    i = 0
    while i < len(main_code_lines):
        line = main_code_lines[i].strip()
        if line.startswith("aayat"):
            try:
                module_filename = line.replace("aayat", "").strip().replace('"', '')
                base_dir = os.path.dirname(os.path.abspath(current_file_path))
                module_path = os.path.join(base_dir, module_filename)
                if module_path not in imported_files:
                    imported_files.add(module_path)
                    with open(module_path, 'r', encoding='utf-8') as file:
                        module_lines = file.readlines()
                    process_file(module_lines, module_path, imported_files)
            except Exception as e:
                print(f"Aayat Truti: Could not import module '{module_filename}'. {e}")
            i += 1
        else:
            i = execute(main_code_lines, i, variables)

def run_sanski(filename):
    """The main entry point for the interpreter."""
    imported_files = set()
    try:
        built_ins = {
            'grahan_karo': grahan_karo, 'jodo': jodo, 'lambai': lambai,
            'file_kholo': file_kholo, 'file_likho': file_likho, 'file_padho': file_padho, 'file_band_karo': file_band_karo,
            'string_upper': string_upper, 'string_lower': string_lower, 'string_replace': string_replace,
            'string_split': string_split, 'string_strip': string_strip
        }
        functions.update(built_ins)
        for name in dir(math):
            if not name.startswith("_"): functions[name] = getattr(math, name)

        entry_file_path = os.path.abspath(filename)
        with open(entry_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        process_file(lines, entry_file_path, imported_files)

    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sanski_interpreter.py <filename.sns>")
    else:
        run_sanski(sys.argv[1])
