#!/usr/bin/env bash
#
# Keep your fork synced with the original
# To setup:
#  1) Make sure your upstream is set to the original repo you forked from
#  2) add "update-master.sh" to .git/info/exclude file
#  3) run update-master.sh when you want sync your fork
#

echo "Updating your master branch with upstream"

git checkout master
git fetch upstream
git merge upstream/master
git push

echo "Master branch updated. Your fork is now synced."
