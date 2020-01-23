"""
@author Ryan TIffany
Return the Billing Item Ids for all file volumes
"""

from pprint import pprint as pp
import SoftLayer

client = SoftLayer.create_client_from_env()

object_mask = "mask[id,billingItem[id]]"
object_filter = {
    'nasNetworkStorage': {
        'serviceResource': {
            'type': {
                'type': {
                    'operation': '!~ NAS'
                    }
                }
            },
        'storageType': {
            'keyName': {
                'operation': '*= FILE_STORAGE'
                }
            },
        'storageType': {
            'keyName': {
                'operation': '!~ FILE_STORAGE_REPLICANT'
                }
            }
        }
    }

result = client.call('SoftLayer_Account', 'getNasNetworkStorage',
                     mask=object_mask, filter=object_filter)

for item in result:
    billing = item.get('billingItem', False)
    if billing:
        print(billing.get('id','No Billing Id!'))
    else:
        print("No Billing Item for {}".format(item.get('id')))
