# -*- mode: python -*-
import libaudioverse

data_files = []
for i, j in libaudioverse.find_datafiles():
    for k in j:
        data_files.append((k, i))

block_cipher = None


a = Analysis(['audiograph.py'],
             pathex=['c:\\projects\\in_progress\\audiograph'],
             binaries=[],
             datas=data_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='audiograph',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='audiograph')
