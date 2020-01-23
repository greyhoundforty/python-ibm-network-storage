"""
@author Ryan Tiffany
Return the Billing Item Ids for all Block volumes
"""
import SoftLayer
from pprint import pprint as pp
import json

client = SoftLayer.create_client_from_env()
object_mask = "mask[id,billingItem[id]]"
object_filter = {
    'iscsiNetworkStorage': {
        'serviceResource': {
            'type': {
                'type': {
                    'operation': '!~ ISCSI'
                    }
                }
            },
        'storageType': {
            'keyName': {
                'operation': '*= BLOCK_STORAGE'
                }
            },
        'storageType': {
            'keyName': {
                'operation': '!~ BLOCK_STORAGE_REPLICANT'
                }
            }
        }
    }

result = client('SoftLayer_Account', 'getIscsiNetworkStorage',
            mask=object_mask, filter=object_filter)
  
for item in result:
    billing = item.get('billingItem', False)
    if billing:
        print(billing.get('id','No Billing Id!'))
    else:
        print("No Billing Item for {}".format(item.get('id')))