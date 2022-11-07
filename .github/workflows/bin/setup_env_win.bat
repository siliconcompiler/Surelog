:: Install dependencies
choco install -y make
choco install -y swig --side-by-side --version=3.0.12

:: Build Surelog
:: Based on Surelog CI script: https://github.com/chipsalliance/Surelog/blob/master/.github/workflows/main.yml
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\Enterprise\VC\Auxiliary\Build\vcvars64.bat"

set CMAKE_GENERATOR=Ninja
set CC=cl
set CXX=cl
set NO_TCMALLOC=On
set PREFIX=%GITHUB_WORKSPACE%\siliconcompiler\tools\surelog
set CPU_CORES=%NUMBER_OF_PROCESSORS%

set MAKE_DIR=C:\make\bin
set TCL_DIR=%PROGRAMFILES%\Git\mingw64\bin
set SWIG_DIR=%PROGRMDATA%\chocolatey\lib\swig\tools\install\swigwin-3.0.12
set PATH=%pythonLocation%;%SWIG_DIR%;%JAVA_HOME%\bin;%MAKE_DIR%;%TCL_DIR%;%PATH%

set
where cmake && cmake --version
where make && make --version
where swig && swig -version
where java && java -version
where python && python --version
:: where ninja && ninja --version
