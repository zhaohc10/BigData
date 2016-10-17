### Basic example for call InfluxDB api
```
from influxdb import InfluxDBClient
json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client.create_database('example')
client.write_points(json_body)
result = client.query('select value from cpu_load_short;')
print("Result: {0}".format(result))
```


```
from influxdb import InfluxDBClusterClient
cc = InfluxDBClusterClient(hosts = [('192.168.0.1', 8086),
                                    ('192.168.0.2', 8086),
                                    ('192.168.0.3', 8086)],
                           username='root',
                           password='root',
                           database='example')
```