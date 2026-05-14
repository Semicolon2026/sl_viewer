import subprocess

def get_rsync_version():
    result = subprocess.check_output(
        ["rsync", "--version"],
        text=True
    )

    return result.splitlines()[0]
