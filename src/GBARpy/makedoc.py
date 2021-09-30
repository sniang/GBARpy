from docstr_md.src_href import Github
from docstr_md.python import PySoup, compile_md

src_href = Github('https://github.com/sniang/GBARpy/tree/main/src/GBARpy')
soup = PySoup(path='MCPPicture.py', parser='sklearn', src_href=src_href)
compile_md(soup, compiler='sklearn', outfile='../../docs/readme.md')
