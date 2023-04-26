# General Bash

### Wildcards for file glob patterns

- `*` matches any sequence of characters, including none.
- `?` matches any single character.
- `[abc]` matches any single character inside the brackets. You can also use ranges, like [a-z] for any character between a and z.

- `**` matches any level of subdirectories. For example, dir/\*\*/\_.txt matches all .txt files in dir and its subdirectories.

- `{a,b}` matches either a or b.
- `!(pattern)` matches anything that doesn't match pattern.

- `?(pattern)` matches zero or one occurrence of pattern.

- `+(pattern)` matches one or more occurrences of pattern.
- `_(pattern)` matches zero or more occurrences of pattern.

- `@(pattern)` matches exactly one occurrence of pattern.
