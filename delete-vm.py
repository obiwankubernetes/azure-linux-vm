# exit the ssh session
    # exit

# view web server in action
    # in browser enter public ip address: 13.82.170.117

# stop vm
    # az vm stop --resource-group firstlinuxvmrg --name myfirstvm

# start vm
    # az vm start --resource-group firstlinuxvmrg --name myfirstvm

# deallocat vm to stop billing
    # az vm deallocate --name myfirstvm --no-wait --resource-group firstlinuxvmrg

# delete vm
    # az vm delete --resource-group firstlinuxvmrg --name myfirstvm --yes

# delete resource group
    # az group delete --name firstlinuxvmrg --no-wait --yes