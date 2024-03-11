from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
 
cloud_config = {
    'secure_connect_bundle': 'auth.zip'
}
auth_provider = PlainTextAuthProvider(username='nes', password='learning')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()
session.execute('USE corona')
rows = session.execute('SELECT emp_name,emp_city FROM emp')
for user_row in rows:
    print(user_row.emp_name, user_row.emp_city)
