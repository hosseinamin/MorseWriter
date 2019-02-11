# -*- mode: python -*-

block_cipher = None


a = Analysis(['MorseCodeGUI.py'],
             pathex=[],
             binaries=[
             ("libwinpthread-1.dll", "."),
             ("libstdc++-6.dll", "."),
             ("libsqlite3-0.dll", "."),
             ("libpresage-1.dll", "."),
             ("libgcc_s_seh-1.dll", "."),
             ],
             datas=[
             ("morse-writer.ico", "."),
             ("layouts.json", "."),
             ("res/database_en.db", "res/"),
             ("res/presage.xml", "res/"),
             ("res/abbreviations_en.txt", "res/"),
             ],
             hiddenimports=["PyQt5.sip"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='MorseWriter',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon="morse-writer.ico")
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='MorseWriter')
