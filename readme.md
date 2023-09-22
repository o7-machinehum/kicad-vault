![](img/logo.png)
Kicad Vault is a Python based part management systems. It will automatically hunt for KiCad projects and generate a webserver highlighting components, their current prices and availability. It is currently only available with digikey integration. I've pared down the software, it simply will create a CSV file with prices of parts. In the future I will expand it to have full web server functionality.

## Getting setup
Requires KiCad 7.0+ for the `kicad-cli` export utility. This should come native in Linux/OSX, in Windows you need to make sure you have access to the app though the command line.

Start [here](https://developer.digikey.com/) to get some digikey api credentials.

Install and setup environment variables. Leave this in your .bashrc. If you're using Windows you need to add these to your environment variables.
``` bash
export DIGIKEY_CLIENT_ID="client_id"
export DIGIKEY_CLIENT_SECRET'="client_secret"
```

## Running
``` bash
pip install kicad-vault
kicad-vault <your_file>.kicad_sch --field MPN
```
Where "MPN" is the field in KiCad where you give the part number.
