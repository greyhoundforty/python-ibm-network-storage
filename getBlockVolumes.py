"""
@author Ryan Tiffany
Using Classes to return Block Volume Ids
"""
import SoftLayer
from pprint import pprint as pp

class blockVolumeIds():
    def __init__(self):
        self.client = SoftLayer.create_client_from_env()
        # debugger = SoftLayer.DebugTransport(self.client.transport)
        # self.client.transport = debugger
        
    def main(self):
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
                    },
                'storageType': {
                    'keyName': {
                        'operation': '!~ BLOCK_STORAGE_REPLICANT'
                        }
                    }
                }
            }

        result = self.client('SoftLayer_Account', 'getIscsiNetworkStorage',
                    mask=object_mask, filter=object_filter)
        pp(result)
        

    def debug(self):
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))
            
if __name__ == "__main__":
    main = blockVolumeIds()
    main.main()