cd src/server
read -p "Firebase Project ID: " FIREBASE_PROJECT_ID
sed -i "s/TODO/$FIREBASE_PROJECT_ID/" .firebaserc
npm i
cd functions
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
deactivate
cd ../../..
