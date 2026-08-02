---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue.html
---

# Migrate Apache Cassandra workloads to Amazon Keyspaces by using AWS Glue
<a name="migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue"></a>

*Nikolai Kolesnikov, Karthiga Priya Chandran, and Samir Patel, Amazon Web Services*

## Summary
<a name="migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue-summary"></a>

This pattern shows you how to migrate your existing Apache Cassandra workloads to Amazon Keyspaces (for Apache Cassandra) by using CQLReplicator on AWS Glue. You can use CQLReplicator on AWS Glue to minimize the replication lag of migrating your workloads down to a matter of minutes. You also learn how to use an Amazon Simple Storage Service (Amazon S3) bucket to store data required for the migration, including [Apache Parquet](https://parquet.apache.org/) files, configuration files, and scripts. This pattern assumes that your Cassandra workloads are hosted on Amazon Elastic Compute Cloud (Amazon EC2) instances in a virtual private cloud (VPC).

## Prerequisites and limitations
<a name="migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue-prereqs"></a>

**Prerequisites**
+ Cassandra cluster with a source table
+ Target table in Amazon Keyspaces to replicate the workload
+ S3 bucket to store intermediate Parquet files that contain incremental data changes
+ S3 bucket to store job configuration files and scripts

**Limitations**
+ CQLReplicator on AWS Glue requires some time to provision Data Processing Units (DPUs) for the Cassandra workloads. The replication lag between the Cassandra cluster and the target keyspace and table in Amazon Keyspaces is likely to last for only a matter of minutes.

## Architecture
<a name="migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue-architecture"></a>

**Source technology stack  **
+ Apache Cassandra
+ DataStax Server
+ ScyllaDB

**Target technology stack  **
+ Amazon Keyspaces

**Migration architecture  **

The following diagram shows an example architecture where a Cassandra cluster is hosted on EC2 instances and spread across three Availability Zones. The Cassandra nodes are hosted in private subnets.

![Custom service role, Amazon Keyspaces, and Amazon S3, with AWS Glue connecting to the nodes VPC.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e08048da-8996-4f2c-b8ed-da49fe9e693b/images/76256ab3-a1e6-4c9e-9c40-dc78f51edf0f.png)

The diagram shows the following workflow:

1. A custom service role provides access to Amazon Keyspaces and the S3 bucket.

1. An AWS Glue job reads the job configuration and scripts in the S3 bucket.

1. The AWS Glue job connects through port 9042 to read data from the Cassandra cluster.

1. The AWS Glue job connects through port 9142 to write data to Amazon Keyspaces.

## Tools
<a name="migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue-tools"></a>

**AWS services and tools**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) is a browser-based shell that you can use to manage AWS services by using the AWS Command Line Interface (AWS CLI) and a range of preinstalled development tools.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed ETL service that helps you reliably categorize, clean, enrich, and move data between data stores and data streams.
+ [Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html) is a managed database service that helps you migrate, run, and scale your Cassandra workloads in the AWS Cloud.

**Code**

The code for this pattern is available in the GitHub [CQLReplicator](https://github.com/aws-samples/cql-replicator/tree/main/glue) repository.

## Best practices
<a name="migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue-best-practices"></a>
+ To determine the necessary AWS Glue resources for the migration, estimate the number of rows in the source Cassandra table. For example, 250 K rows per 0.25 DPU (2 vCPUs, 4 GB of memory) with 84 GB disk.
+ Pre-warm Amazon Keyspaces tables before running CQLReplicator. For example, eight CQLReplicator tiles (AWS Glue jobs) can write up to 22 K WCUs per second, so the target should be pre-warmed up to 25-30 K WCUs per second.
+ To enable communication between AWS Glue components, use a self-referencing inbound rule for all TCP ports in your security group.
+ Use the incremental traffic strategy to distribute the migration workload over time.

## Epics
<a name="migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue-epics"></a>

### Deploy CQLReplicator
<a name="deploy-cqlreplicator"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a target keyspace and table.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue.html) | App owner, AWS administrator, DBA, App developer |
| Configure the Cassandra driver to connect to Cassandra. | Use the following configuration script:<pre>Datastax-java-driver {<br />  basic.request.consistency = "LOCAL_QUORUM"<br />  basic.contact-points = ["127.0.0.1:9042"]<br />   advanced.reconnect-on-init = true<br />   basic.load-balancing-policy {<br />        local-datacenter = "datacenter1"<br />}<br />advanced.auth-provider = {<br />       class = PlainTextAuthProvider<br />       username = "user-at-sample"<br />       password = "S@MPLE=PASSWORD="<br />}<br />}</pre>The preceding script uses the Spark Cassandra Connector. For more information, see the reference configuration for[ Cassandra](https://docs.datastax.com/en/developer/java-driver/4.17/manual/core/configuration/reference/). | DBA |
| Configure the Cassandra driver to connect to Amazon Keyspaces. | Use the following configuration script:<pre>datastax-java-driver {<br />basic {<br />  load-balancing-policy {<br />    local-datacenter = us-west-2<br />        }<br />  contact-points = [<br />            "cassandra.us-west-2.amazonaws.com:9142"<br />        ]<br />  request {<br />  page-size = 2500<br />  timeout = 360 seconds<br />  consistency = LOCAL_QUORUM<br />        }<br />    }<br />advanced {<br /> control-connection {<br />  timeout = 360 seconds<br />        }<br /> session-leak.threshold = 6<br /> connection {<br /> connect-timeout = 360 seconds<br /> init-query-timeout = 360 seconds<br /> warn-on-init-error = false<br />        }<br /> auth-provider = {<br />  class = software.aws.mcs.auth.SigV4AuthProvider<br />  aws-region = us-west-2<br /> }<br /><br /> ssl-engine-factory {<br />  class = DefaultSslEngineFactory<br />        }<br />    }<br />}</pre>The preceding script uses the Spark Cassandra Connector. For more information, see the reference configuration for[ Cassandra](https://docs.datastax.com/en/developer/java-driver/4.17/manual/core/configuration/reference/). | DBA |
| Create an IAM role for the AWS Glue job. | Create a new AWS service role named `glue-cassandra-migration` with AWS Glue as a trusted entity.The `glue-cassandra-migration` should provide read and write access to the S3 bucket and Amazon Keyspaces. The S3 bucket contains the .jar files, configuration files for Amazon Keyspaces and Cassandra, and the intermediate Parquet files. For example, it contains the `AWSGlueServiceRole`, `AmazonS3FullAccess`, and `AmazonKeyspacesFullAccess` managed policies. | AWS DevOps |
| Download CQLReplicator in AWS CloudShell. | Download the project to your home folder by running the following command:<pre>git clone https://github.com/aws-samples/cql-replicator.git<br />cd cql-replicator/glue<br /># Only for AWS CloudShell, the bc package includes bc and dc. Bc is an arbitrary precision numeric processing arithmetic language<br />sudo yum install bc -y</pre> |  |
| Modify the reference configuration files. | Copy `CassandraConnector.conf` and `KeyspacesConnector.conf` to the `../glue/conf` directory in the project folder. | AWS DevOps |
| Initiate the migration process. | The following command initializes the CQLReplicator environment. Initializaition involves copying .jar artifacts, and creating an AWS Glue connector, an S3 bucket, an AWS Glue job, the `migration` keyspace, and the `ledger` table:<pre>cd cql-replicator/glue/bin<br />./cqlreplicator --state init --sg '"sg-1","sg-2"' \ <br />                --subnet "subnet-XXXXXXXXXXXX" \ <br />                --az us-west-2a --region us-west-2 \ <br />                --glue-iam-role glue-cassandra-migration \ <br />                --landing-zone s3://cql-replicator-1234567890-us-west-2<br /></pre><br />The script includes the following parameters:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue.html) | AWS DevOps |
| Validate the deployment. | After you run the previous command, the AWS account should contain the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue.html) | AWS DevOps |

### Run CQLReplicator
<a name="run-cqlreplicator"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start the migration process. | To operate CQLReplicator on AWS Glue, you need to use the `--state run` command, followed by a series of parameters. The precise configuration of these parameters is primarily determined by your unique migration requirements. For example, these settings might vary if you choose to replicate time to live (TTL) values and updates, or you offload objects exceeding 1 MB to Amazon S3.<br />To replicate the workload from the Cassandra cluster to Amazon Keyspaces, run the following command: <pre>./cqlreplicator --state run --tiles 8  \<br />                --landing-zone s3://cql-replicator-1234567890-us-west-2 \ <br />                --region us-west-2 \                              <br />                --src-keyspace source_keyspace \ <br />                --src-table source_table \  <br />                --trg-keyspace taget_keyspace \<br />                --writetime-column column_name \<br />                --trg-table target_table --inc-traffic</pre><br />Your source keyspace and table are `source_keyspace.source_table` in the Cassandra cluster. Your target keyspace and table are `target_keyspace.target_table` in Amazon Keyspaces. The parameter `--inc-traffic` helps prevent incremental traffic from overloading the Cassandra cluster and Amazon Keyspaces with a high number of requests.<br />To replicate updates, add `--writetime-column regular_column_name` to your command line. The regular column is going to be used as the source of the write timestamp. | AWS DevOps |

### Monitor the migration process
<a name="monitor-the-migration-process"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate migrated Cassandra rows during the historical migration phase. | To obtain the number of rows replicated during the backfilling phase, run the following command:<pre>./cqlreplicator --state stats \<br />                --landing-zone s3://cql-replicator-1234567890-us-west-2 \  <br />                --src-keyspace source_keyspace --src-table source_table --region us-west-2</pre> | AWS DevOps |

### Stop the migration process
<a name="stop-the-migration-process"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use the `cqlreplicator` command or the AWS Glue console. | To stop the migration process gracefully, run the following command:<pre>./cqlreplicator --state request-stop --tiles 8 \                         <br />                --landing-zone s3://cql-replicator-1234567890-us-west-2 \     <br />                --region us-west-2 \                     <br />                --src-keyspace source_keyspace --src-table source_table</pre><br />To stop the migration process immediately, use the AWS Glue console. | AWS DevOps |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the deployed resources. | The following command will delete the AWS Glue job, connector, S3 bucket, and Keyspaces table `ledger`:<pre>./cqlreplicator --state cleanup --landing-zone s3://cql-replicator-1234567890-us-west-2</pre> | AWS DevOps |

## Troubleshooting
<a name="migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS Glue jobs failed and returned an Out of Memory (OOM) error. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue.html) |

## Related resources
<a name="migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue-resources"></a>
+ [CQLReplicator with AWS Glue README.MD](https://github.com/aws-samples/cql-replicator/blob/main/glue/README.MD)
+ [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
+ [Amazon Keyspaces documentation](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html)
+ [Apache Cassandra](https://cassandra.apache.org/_/index.html)

## Additional information
<a name="migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue-additional"></a>

**Migration considerations**

You can use AWS Glue to migrate your Cassandra workload to Amazon Keyspaces, while keeping your Cassandra source databases completely functional during the migration process. After the replication is complete, you can choose to cut over your applications to Amazon Keyspaces with minimal replication lag (less than minutes) between the Cassandra cluster and Amazon Keyspaces. To maintain data consistency, you can also use a similar pipeline to replicate the data back to the Cassandra cluster from Amazon Keyspaces.

**Write unit calculations**

As an example, consider that you intend to write 500,000,000 with the row size 1 KiB during one hour. The total number of Amazon Keyspaces write units (WCUs) that you require is based on this calculation:

`(number of rows/60 mins 60s) 1 WCU per row = (500,000,000/(60*60s) * 1 WCU) = 69,444 WCUs required`

69,444 WCUs per second is the rate for 1 hour, but you could add some cushion for overhead.  For example, `69,444 * 1.10 = 76,388 WCUs` has 10 percent overhead.

**Create a keyspace by using CQL**

To create a keyspace by using CQL, run the following commands:

```
CREATE KEYSPACE target_keyspace WITH replication = {'class': 'SingleRegionStrategy'}
CREATE TABLE target_keyspace.target_table ( userid uuid, level text, gameid int, description text, nickname text, zip text, email text, updatetime text, PRIMARY KEY (userid, level, gameid) ) WITH default_time_to_live = 0 AND CUSTOM_PROPERTIES = {'capacity_mode':{ 'throughput_mode':'PROVISIONED', 'write_capacity_units':76388, 'read_capacity_units':3612 }} AND CLUSTERING ORDER BY (level ASC, gameid ASC)
```
