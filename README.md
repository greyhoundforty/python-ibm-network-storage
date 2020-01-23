# python-ibm-network-storage
Python scripts to pull network storage details

**blockVolumeBillingItemIds.py**:  
This example will return the Block Volume Billing Item Ids.

**fileVolumeBillingItemIds.py**:  
This example will return the File Volume Billing Item Ids.

**getBlockVolumes.py**:  
This example will return all of the [Block Volumes](https://cloud.ibm.com/docs/infrastructure/BlockStorage?topic=BlockStorage-About#getting-started-with-block-storage) on your account.

**getFileVolumes.py**:  
This example will return all of the [File Volumes](https://cloud.ibm.com/docs/infrastructure/FileStorage?topic=FileStorage-about#getting-started-with-file-storage) on your account.

## Scripts
To use the scripts in the `scripts` directory you will want to have the following tools installed:  
 - [slcli](https://softlayer-api-python-client.readthedocs.io/en/latest/install/)
 - [jq](https://stedolan.github.io/jq/)

Configure the `slcli` tool using this [guide](https://softlayer-api-python-client.readthedocs.io/en/latest/config_file/).

### Running the script

```
git clone https://github.com/greyhoundforty/python-ibm-network-storage.git
cd python-ibm-network-storage/scripts
./storage.sh
```

The output should look something like this:

```
>>> File Volumes:
File Volume ID: 7498601
Associated Billing Item ID: 76075929
Billing Cost: $0.0
Authorized Bare Metal Servers:
Authorized Virtual Guests:

File Volume ID: 11657467
Associated Billing Item ID: 106722257
Billing Cost: $10.0
Authorized Bare Metal Servers:
Authorized Virtual Guests:

File Volume ID: 54735697
Associated Billing Item ID: 362144727
Billing Cost: $8.0364
Authorized Bare Metal Servers:
Authorized Virtual Guests: ykawa.cent7.hrly.ibmcloud.com

File Volume ID: 58484195
Associated Billing Item ID: 377436925
Billing Cost: $125.72079
Authorized Bare Metal Servers:
Authorized Virtual Guests:

File Volume ID: 63081103
Associated Billing Item ID: 399022345
Billing Cost: $2.4978
Authorized Bare Metal Servers: athena.cdetesting.com
Authorized Virtual Guests: dal13.cdetesting.com
```