"""
@author Ryan TIffany
Return the Block Volume Ids and associated Billing Item Ids
"""

from pprint import pprint as pp
import SoftLayer
import logging

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

result = client.call('SoftLayer_Account', 'getIscsiNetworkStorage'
                     ,mask=object_mask, filter=object_filter)

pp(result)