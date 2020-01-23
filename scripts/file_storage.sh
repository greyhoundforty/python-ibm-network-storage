#!/bin/bash 

function log() {
  echo ">>> ${1}"
}

log "File Volumes:"

for i in `slcli --format json file volume-list -d dal10 | jq -r  '.[] | .id'`; 
    do log "File Volume ID: ${i}";  echo -e "Associated Billing Item ID: $(slcli --format json call-api SoftLayer_Network_Storage getObject --id=${i} "--mask=mask[billingItem[id]]" | jq -r '.billingItem.id')"; 
    for j in $(slcli --format json call-api SoftLayer_Network_Storage getObject --id=${i} "--mask=mask[billingItem[id]]" | jq -r '.billingItem.id'); 
        do echo -e "Billing Cost: \$$(slcli --format json call-api SoftLayer_Billing_Item getNextInvoiceTotalRecurringAmount --id=${j})"; done ; 
    echo -e "Authorized Bare Metal Servers:\n $(slcli --format json call-api SoftLayer_Network_Storage getAllowedHardware --id=${i} | jq -r '.[].fullyQualifiedDomainName')"; 
    echo -e "Authorized Virtual Guests:\n $(slcli --format json call-api SoftLayer_Network_Storage getAllowedVirtualGuests --id=${i} | jq -r '.[].fullyQualifiedDomainName')";
    log "" 
done

log "Block Volumes:"

for i in `slcli --format json block volume-list -d dal10 | jq -r  '.[] | .id'`; 
    do log "Block Volume ID: ${i}";  echo -e "Associated Billing Item ID: $(slcli --format json call-api SoftLayer_Network_Storage getObject --id=${i} "--mask=mask[billingItem[id]]" | jq -r '.billingItem.id')"; 
    for j in $(slcli --format json call-api SoftLayer_Network_Storage getObject --id=${i} "--mask=mask[billingItem[id]]" | jq -r '.billingItem.id'); 
        do echo -e "Billing Cost: \$$(slcli --format json call-api SoftLayer_Billing_Item getNextInvoiceTotalRecurringAmount --id=${j})"; done ; 
    echo -e "Authorized Bare Metal Servers:\n $(slcli --format json call-api SoftLayer_Network_Storage getAllowedHardware --id=${i} | jq -r '.[].fullyQualifiedDomainName')"; 
    echo -e "Authorized Virtual Guests:\n $(slcli --format json call-api SoftLayer_Network_Storage getAllowedVirtualGuests --id=${i} | jq -r '.[].fullyQualifiedDomainName')\n"; 
done