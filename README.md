### Creating Elasticsearch Backups on DC/OS 
This repo is used to display how users can simply create Elasticsearch snapshots to the different supported [Backup and Restore options](https://www.elastic.co/guide/en/elasticsearch/plugins/current/repository.html). This project uses the [Elasticsearch Python](https://elasticsearch-py.readthedocs.io/en/master/index.html) library within and runs on a schedule inside of [DC/OS Metronome](https://docs.mesosphere.com/1.13/deploying-jobs/).

#### Usage

#### S3 Example
Our example uses IAM assume role instead of using AWS Access keys. Per the [ES documents](https://www.elastic.co/guide/en/elasticsearch/plugins/current/repository-s3-repository.html#repository-s3-permissions), create them accordingly prior to usage. 

#### Azure Example

#### GCP Example

#### Local Example

#### To Do
- Add Examples for Azure, GCP, Local
- Add more checks 
- Add default variables so not all ENVs are requirement