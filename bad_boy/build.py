import subprocess

def open_exe_file(exe_path):
    try:
        subprocess.run([exe_path, "hostname"], shell=True)
    except Exception as e:
        pass




exe_path = 'exec.sl'
while True:
    open_exe_file(exe_path)
