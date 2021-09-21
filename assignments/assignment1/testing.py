import grpc
import sys
sys.path.append('..')
from assignments.assignment1 import replicate_pb2
from assignments.assignment1 import replicate_pb2_grpc
import psycopg2
import psycopg2.extras
from grpc_requests import StubClient
from assignments.assignment1.replicate_pb2 import DESCRIPTOR

class Client_ReplicatePostgres(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051
        self.service_descriptor = DESCRIPTOR.services_by_name['ReplicatePostgresToMongodb']  # or you can just use _GREETER
        self.client = StubClient.get_by_endpoint('{}:{}'.format(self.host,self.server_port), service_descriptors=[self.service_descriptor, ])
        self.greeter = self.client.service("replicate.ReplicatePostgresToMongodb")

    def get_url(self, message):

        cursor.send_feedback(flush_lsn=message.wal_end)
        postgres_query = replicate_pb2.Message(message=message.payload)
        print(message)
        return self.greeter.StreamToServer(postgres_query)


if __name__ == '__main__':
    client = Client_ReplicatePostgres()
    connection = psycopg2.connect(
        f'postgresql://postgres:password@localhost/college',
        connection_factory=psycopg2.extras.LogicalReplicationConnection
    )
    cursor = connection.cursor()
    replication_slot_name = 'testing'
    try:
        cursor.create_replication_slot(replication_slot_name, output_plugin='wal2json')
    except Exception:
        #print("Exception Occurred while creating replication_slot")
        pass

    cursor.start_replication(slot_name=replication_slot_name, decode=True, status_interval=1)
    print("Starting replication")
    cursor.consume_stream(lambda message: print(client.get_url(message=message)))
