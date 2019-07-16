import markdown
import os
import sys


def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
            'markdown.extensions.toc']

    html = '''
    <html lang="en">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="github-markdown.css" rel="stylesheet">
    <style>
    .markdown-body {
        box-sizing: border-box;
        min-width: 200px;
        max-width: 980px;
        margin: 0 auto;
        padding: 45px;
    }
    </style>
    </head>
    <body class="markdown-body">
    %s
    </body>
    </html>
    '''

    ret = markdown.markdown(mdstr, extensions=exts)
    return html % ret


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: main.py source_filename target_file')
        sys.exit()

    infile = open(sys.argv[1], 'r')
    md = infile.read()
    infile.close()

    if os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])

    outfile = open(sys.argv[2], 'a')
    outfile.write(md2html(md))
    outfile.close()

    print('convert %s to %s success!' % (sys.argv[1], sys.argv[2]))
