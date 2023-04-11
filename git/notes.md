# Notes

### How to read `git status -sb`?

The first line of the output shows the current branch you are on and the status of the branch compared to the remote branch.

e.g. `## master...origin/master [ahead 1]
`

The rest of the output:

- ??: The file is untracked.
- A: The file has been added to the staging area.
- M: The file has been modified since the last commit.
- D: The file has been deleted.
- R: The file has been renamed.
- C: The file has been copied.
- U: The file has conflicts that need to be resolved.
