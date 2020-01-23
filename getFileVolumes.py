"""
@author Ryan Tiffany
Using Classes to return File Volume Ids
"""
import SoftLayer
from pprint import pprint as pp

class fileVolumeIds():
    def __init__(self):
        self.client = SoftLayer.create_client_from_env()
        # debugger = SoftLayer.DebugTransport(self.client.transport)
        # self.client.transport = debugger
        
    def main(self):
        object_mask = "mask[id]"
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

        result = self.client('SoftLayer_Account', 'getNasNetworkStorage',
                    mask=object_mask, filter=object_filter)
        pp(result)
        

    def debug(self):
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))
            
if __name__ == "__main__":
    main = fileVolumeIds()
    main.main()