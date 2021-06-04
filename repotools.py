from pathlib import Path
import random
import subprocess
import sys

_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class RepoTool:
    def __init__(self, requested_path):
        new_repo_path = Path(requested_path).resolve()

        if new_repo_path.exists():
            raise SystemExit(f"{new_repo_path} already exists")

        print(f"putting the new repo in: {new_repo_path}")
        new_repo_path.mkdir(parents=True, exist_ok=False)

        self.git_dir = str(new_repo_path)

    def git(self, args):
        cmd = args.split()
        cmd.insert(0, "git")
        subprocess.run(cmd, cwd=self.git_dir)

    def fill(self, filename, contents=None):
        if contents is None:
            subprocess.run(["touch", filename], cwd=self.git_dir)
        else:
            with open(f"{self.git_dir}/{filename}", 'w') as f:
                f.write(contents)

    def randname(self):
        return (
            random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
            + random.choice(_ALPHABET)
        )
