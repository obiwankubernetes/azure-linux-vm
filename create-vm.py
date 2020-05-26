# make sure azure cli is working
    # az --version

# login to azure
    # az login

# create resource group
    # az group create --name firstlinuxvmrg --location eastus

# create vm
    # az vm create --resource-group firstlinuxvmrg --name myfirstvm --image UbuntuLTS --admin-username obiwankubernetes --generate-ssh-keys

# Open port 80 for web traffic: By default, only SSH connections are opened when you create a Linux VM in Azure. Use az vm open-port to open TCP port 80 for use with the NGINX web server
    # az vm open-port --port 80 --resource-group firstlinuxvmrg  --name myfirstvm

# connect to vm via ssh
    # ssh obiwankubernetes@13.82.170.117

# check version of linux vm running
    # cat /etc/issue.net

# check name of linux vm running
    # uname -a

# Install web server: To see your VM in action, install the NGINX web server. Update your package sources and then install the latest NGINX package.
    # sudo apt-get -y update
    # sudo apt-get -y install nginx
