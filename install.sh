#
# The installation is very simple
#
mkdir -p libs
cd ctypes
gcc -fPIC -shared -g -O2 -o libqsym.so qsym.c
mv libqsym.so ../libs
