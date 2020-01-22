"""
@author Ryan TIffany
"""

from pprint import pprint as pp
import SoftLayer


CLIENT = SoftLayer.create_client_from_env()

OBJECT_MASK = "mask[id, storageType[keyName]]"
OBJECT_FILTER = {
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
RESULT = CLIENT.call('SoftLayer_Account', 'getNasNetworkStorage',
                     mask=OBJECT_MASK, filter=OBJECT_FILTER)
pp(RESULT)
