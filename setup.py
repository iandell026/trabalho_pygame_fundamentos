import cx_Freeze

executables = [cx_Freeze.Executable(script="jogo.py", icon="assets/icon.ico" )]
cx_Freeze.setup(
    name = "Docelândia",
    options = {"build_exe":{"packages":["pygame"]
    , "include_files": ["assets"]
    } },
    executables = executables
)