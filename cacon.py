from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def cassandra_connect(): 
    cloud_config = {
    'secure_connect_bundle': 'casbundle.zip'
    }
    auth_provider = PlainTextAuthProvider('PmdXZysXcUCQlkPboIcbnrPW', 'RBhpIG9zZJxcFC8KEMmFTt47GmGvW8WpdZcyCSkF59SZt+sGT5Z-u_HKG5UClt.hwzYJlMr7f-ndzz5P+oQYpF_eztvbZdEJ2qrpMUkh2QrGobnBe0vzHL1o5vfcEASN')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    return session
