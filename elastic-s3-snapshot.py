import json
import os
from elasticsearch import Elasticsearch

# These are passed in as ENV variables during runtime
# Elastic Settings
es_repository = os.envion['ES_REPOSITORY']
es_snapshot = os.environ['ES_SNAPSHOT']
# AWS Settings
aws_bucket = os.environ['AWS_BUCKET']
aws_bucket_base_path = os.environ['AWS_BUCKET_BASE_PATH']
aws_region = os.environ['AWS_REGION']
aws_role_arn = os.environ['AWS_ROLE_ARN']


def register(es):
    # S3 Settings for Repository
    payload = {
      "type": "s3",
      "settings": {
        "bucket": aws_bucket,
        "base_path": aws_bucket_base_path,
        "region": aws_region,
        "role_arn": aws_role_arn
      }
    }

    # Create Repository if doesnt exist
    try:
        es.snapshot.create_repository(repository=es_repository, body=json.dumps(payload), verify=True)

    except Exception as e:
        print("\n\n[ERROR] Error: %s" % (str(e)))


def snapshot():
    # Create Snapshot
    try:
        es.snapshot.create(repository=es_repository, snapshot=es_snapshot, wait_for_completion=True)

    except Exception as e:
        print("\n\n[ERROR] Error: %s" % (str(e)))


def main():
    # Create the connection
    es = Elasticsearch(
        ['coordinator.logselastic.l4lb.thisdcos.directory'],
        port=9200
    )

    # Ensure Repository Exists
    register(es)

    # Create snapshot.
    # NOTE: This is incremental unless you change the snapshot name
    snapshot(es)

if __name__ == '__main__':
    main()


