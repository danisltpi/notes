import glob
import os

if os.path.exists('README.md'):
    os.remove('README.md')
readme_description = 'This is a collection of my notes for software development, studying, etc. which can be very useful but easily forgotten.'
with open('./README.md', 'w') as f:
    f.write('# Personal notes\n\n' + readme_description + '\n\n')
    dirs = [dir for dir in glob.glob(
        '*') if os.path.isdir(dir) and glob.glob(dir + '/*.md')]
    for dir in dirs:
        if dir.lower() == 'dev':
            title = 'Software Development'
        else:
            title = dir.capitalize()
        f.write('## ' + title + '\n\n')
        md_files = glob.glob(dir + '/*.md')
        for md_file in md_files:
            md_filename = os.path.basename(md_file)
            with open(md_file, 'r') as md:
                h1_header = md.readline().strip('#').strip()
            f.write('- [' + h1_header + '](./' + md_filename + ')\n')
        f.write('\n')
