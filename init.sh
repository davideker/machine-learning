if [ -d "$HOME/.local/bin" ] ; then
  PATH="$PATH:$HOME/.local/bin"
fi

python3 -m venv ml
source ml/bin/activate
pip3 install wheel
pip3 install -r requirements.txt

#https://stackoverflow.com/questions/13312139/opencv-and-python-virtualenv
echo "Importing opencv library from host into venv..."
# Find cv2 library for the global Python installation.
GLOBAL_CV2=$(/usr/bin/python3 -c 'import cv2; print(cv2.__file__)')
# Find site-packages directory in the venv
VENV_SITEPACKAGES_DIR=$(python3 -c 'import site; print(site.getsitepackages()[0])')
# Copy host-installed library file into venv
cp ${GLOBAL_CV2} ${VENV_SITEPACKAGES_DIR}



