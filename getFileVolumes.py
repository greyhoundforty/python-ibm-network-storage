"""
@author Ryan TIffany
"""

from pprint import pprint as pp
import SoftLayer

client = SoftLayer.create_client_from_env()

object_mask = "mask[id, storageType[keyName]]"
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
            }
        }
    }
result = client.call('SoftLayer_Account', 'getNasNetworkStorage',
                     mask=object_mask, filter=object_filter)
pp(result)
