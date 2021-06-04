import sys

from repotools import RepoTool

if sys.version_info.major < 3:
    raise SystemExit("requires Python 3")

if len(sys.argv) < 2:
    raise SystemExit("requires an argument telling me where to put the repo")

r = RepoTool(sys.argv[1])
git = r.git
fill = r.fill
randname = r.randname

print(f"on to the Git stuff")

git("init")

# create a "base" commit
fill("_base.txt", randname())
git("add .")
git("commit -m base")

# create a new commit in mainline
fill("_new.txt", randname())
git("add .")
git("commit -m new")

# now put a wide structure off of the base commit
for x in range(10000):
    some_chars = randname()
    git(f"switch -qc {some_chars} HEAD^")
    fill(f"{some_chars}.txt", some_chars)
    git(f"add {some_chars}.txt")
    git(f"commit -qm {some_chars}")
    print(".", end='', flush=bool(x % 20))
print()

# later:
# git for-each-ref --format='%(refname:lstrip=2)' | grep -v "main" | xargs git merge
