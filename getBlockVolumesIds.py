"""
@author Ryan TIffany
Just return the IDs of the Block Volumes
"""

from pprint import pprint as pp
import SoftLayer
import logging

client = SoftLayer.create_client_from_env()

object_mask = "mask[id]"
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
            }
        }
    }

second_mask = "mask[billingItem[id]]"

result = client.call('SoftLayer_Account', 'getIscsiNetworkStorage'
                     ,mask=object_mask, filter=object_filter)

pp(result)
