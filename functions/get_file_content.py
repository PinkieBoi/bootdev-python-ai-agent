import os


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))
    if abs_working_dir not in abs_target_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abs_target_path):
        return f'Error: File not found or is not a regular file: "{file_path}"' 
    try:
        with open(abs_target_path, "r") as file:
            content = file.read()
            if len(content) > 10000:
                content = file.read(10000) + '[...File "{file_path}" truncated at {MAX_LENGTH} characters]'
    except Exception as e:
        return f'Error: {str(e)}'
    return content
