"""
@author Ryan TIffany
"""

from pprint import pprint as pp
import SoftLayer

CLIENT = SoftLayer.create_client_from_env()

OBJECT_MASK = "mask[id, storageType[keyName]]"
OBJECT_FILTER = {
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

RESULT = CLIENT.call('SoftLayer_Account', 'getIscsiNetworkStorage',
                     mask=OBJECT_MASK, filter=OBJECT_FILTER)
pp(RESULT)
