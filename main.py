# You MUST install Pywin32 as a dependency for Windows admin privileges.
# It does not need to be imported, but it needs to be installed.

# Dependencies
import os, subprocess, getpass, pyuac, winreg as reg
from pyuac import main_requires_admin

# Types
from typing import List

@main_requires_admin
def main():
    def create_script(script_name: str = None, code: str = None) -> None:
        """
            Create a script with the content you want inside of it. The
        """

        # Set paths to directories
        user_dir = f'C:\\Users\\{getpass.getuser()}'
        custom_commands_dir = f"{user_dir}\\.custom-commands"
        cc_bin_dir = f"{custom_commands_dir}\\bin"

        # Check if directories exist. If not, create them
        if (os.path.isdir(custom_commands_dir) == False):
            os.mkdir(custom_commands_dir)
        if (os.path.isdir(cc_bin_dir) == False):
            os.mkdir(cc_bin_dir)

        path_env_var: List[str] = os.environ['Path'].split(';')

        if (cc_bin_dir not in path_env_var):
            all_paths = os.pathsep.join(path_env_var)
            all_paths += os.pathsep + cc_bin_dir
            os.system(f'SETX /M Path "{all_paths}" & timeout 5')

        os.system(f"""cd {cc_bin_dir} & {code} > {script_name}.bat""")

    create_script('testme', 'echo "testsy"')

if __name__ == '__main__':
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main() 