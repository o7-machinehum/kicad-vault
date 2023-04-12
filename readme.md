# Kicad Vault
Kicad Vault is a Python based part management systems. It will automatically hunt for KiCad projects and generate a webserver highlighting components, their current prices and availability. It is currently only available with digikey integration.

## Getting setup
Start [here](https://developer.digikey.com/) to get some digikey api credentials.

Install digikey python api.
``` bash
pip install digikey-api
```

Install and setup environment variables. Leave this in your bashrc.
``` bash
export DIGIKEY_CLIENT_ID="client_id"
export DIGIKEY_CLIENT_SECRET'="client_secret"
```

## Running
``` bash
cd ~/project/ # Assuming all digikey projects are in here
git clone git@github.com:o7-machinehum/kicad-vault.git
cd kicad-vault
python main.py ../
```
