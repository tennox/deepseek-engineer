import runpy
import os

def main():
    # Use importlib.resources to find the script
    with importlib.resources.path(__package__, 'deepseek-eng.py') as script_path:
        runpy.run_path(str(script_path), run_name='__main__')

if __name__ == '__main__':
    main()
