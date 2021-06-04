from pathlib import Path
import random
import subprocess
import sys

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def git(args):
    cmd = args.split()
    cmd.insert(0, "git")
    subprocess.run(cmd, cwd=git_dir)


def fill(filename, contents=None):
    if contents is None:
        subprocess.run(["touch", filename], cwd=git_dir)
    else:
        with open(f"{git_dir}/{filename}", 'w') as f:
            f.write(contents)


def randname():
    return (
          random.choice(ALPHABET)
        + random.choice(ALPHABET)
        + random.choice(ALPHABET)
        + random.choice(ALPHABET)
        + random.choice(ALPHABET)
        + random.choice(ALPHABET)
        + random.choice(ALPHABET)
        + random.choice(ALPHABET)
        + random.choice(ALPHABET)
        + random.choice(ALPHABET)
        + random.choice(ALPHABET)
        + random.choice(ALPHABET)
    )


if sys.version_info.major < 3:
    raise SystemExit("requires Python 3")

if len(sys.argv) < 2:
    raise SystemExit("requires an argument telling me where to put the repo")

new_repo_path = Path(sys.argv[1]).resolve()

if new_repo_path.exists():
    raise SystemExit(f"{new_repo_path} already exists")

print(f"putting the new repo in: {new_repo_path}")
new_repo_path.mkdir(parents=True, exist_ok=False)

git_dir = str(new_repo_path)

print(f"on to the Git stuff")

git("init")
fill("_base.txt", randname())
git("add .")
git("commit -m base")
git("switch -c feature")
for _ in range(100):
    some_chars = randname()
    fill(f"{some_chars}.txt", some_chars)
    git(f"add {some_chars}.txt")
    git(f"commit -qm {some_chars}")
    print(".", end='', flush=bool(random.randint(0,19)))
print()