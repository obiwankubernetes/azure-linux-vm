# exit the ssh session
    # exit

# view web server in action
    # in browser enter public ip address: <publicipaddress>

# stop vm
    # az vm stop --resource-group <namerg> --name <namevm>

# start vm
    # az vm start --resource-group <namerg> --name <namevm>

# deallocat vm to stop billing
    # az vm deallocate --name <namevm> --no-wait --resource-group <namerg>

# delete vm
    # az vm delete --resource-group <namerg> --name <namevm> --yes

# delete resource group
    # az group delete --name <namerg> --no-wait --yes
