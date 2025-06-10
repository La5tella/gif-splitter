@echo off
setlocal EnableDelayedExpansion

REM === 1) Define your required Python modules here ===
set "MODULES=moviepy imageio-ffmpeg Pillow"

REM === 2) Check for Python on PATH ===
where python >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found in PATH. Please install Python 3 and add it to your PATH.
    exit /b 1
) else (
    echo [OK] Python detected.
)

REM === 3) Check for pip (fall back to python -m pip) ===
where pip >nul 2>&1
if errorlevel 1 (
    echo [WARN] pip not found. Using "python -m pip" instead.
    set "PIP_CMD=python -m pip"
) else (
    echo [OK] pip detected.
    set "PIP_CMD=pip"
)

REM === 4) Loop through each module, test import, install if missing ===
for %%M in (%MODULES%) do (
    echo.
    echo Checking Python module: %%M
    python -c "import %%M" >nul 2>&1
    if errorlevel 1 (
        echo [MISSING] %%M installing...
        %PIP_CMD% install --upgrade --user %%M
        if errorlevel 1 (
            echo [ERROR] Failed to install %%M.
            exit /b 1
        ) else (
            echo [INSTALLED] %%M
        )
    ) else (
        echo [OK] %%M is already installed.
    )
)

echo.
echo All dependencies are now installed and up to date.
echo To run, please enter cmd "py slice.py <filename> <col> <row> <outdir> (OPTIONAL ->) <target_w> <target_h> in a terminal of the same directory."
echo.
pause
