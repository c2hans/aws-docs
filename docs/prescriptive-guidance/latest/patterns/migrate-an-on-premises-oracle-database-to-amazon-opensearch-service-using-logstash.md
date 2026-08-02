---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-opensearch-service-using-logstash.html
---

# Migrate an on-premises Oracle database to Amazon OpenSearch Service using Logstash
<a name="migrate-an-on-premises-oracle-database-to-amazon-opensearch-service-using-logstash"></a>

*Aditya Goteti, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-oracle-database-to-amazon-opensearch-service-using-logstash-summary"></a>

This pattern describes how to move data from an on-premises Oracle database to Amazon OpenSearch Service using Logstash. It includes architectural considerations and some required skill sets and recommendations. The data can be from a single table or from multiple tables in which a full-text search will need to be performed.

OpenSearch Service can be configured within a virtual private cloud (VPC), or it can be placed publicly with IP-based restrictions. This pattern describes a scenario where OpenSearch Service is configured within a VPC. Logstash is used to collect the data from the Oracle database, parse it to JSON format, and then feed the data into OpenSearch Service.

## Prerequisites and limitations
<a name="migrate-an-on-premises-oracle-database-to-amazon-opensearch-service-using-logstash-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Java 8 (required by Logstash 6.4.3)
+ Connectivity between the on-premises database servers and Amazon Elastic Compute Cloud (Amazon EC2) instances in a VPC, established using AWS Virtual Private Network (AWS VPN)
+ A query to retrieve the required data to be pushed to OpenSearch Service from the database
+ Oracle Java Database Connectivity (JDBC) drivers

**Limitations**
+ Logstash cannot identify records that are hard-deleted from the database

**Product versions**
+ Oracle Database 12c
+ OpenSearch Service 6.3
+ Logstash 6.4.3

## Architecture
<a name="migrate-an-on-premises-oracle-database-to-amazon-opensearch-service-using-logstash-architecture"></a>

**Source technology stack**
+ On-premises Oracle database
+ On-premises AWS VPN

**Target technology stack**
+ VPC
+ EC2 instance
+ OpenSearch Service
+ Logstash
+ NAT Gateway (for operating system updates on EC2 instances and to install Java 8, Logstash, and plugins)

**Data migration architecture**

![How to move data from an on-premises Oracle database to Amazon OpenSearch Service using Logstash.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/09f6d2de-de2f-4ed6-af93-34b71b75a263/images/df6a61fb-09fb-49d4-a7e8-b04e88c003df.png)

## Tools
<a name="migrate-an-on-premises-oracle-database-to-amazon-opensearch-service-using-logstash-tools"></a>
+ Logstash 6.4.3
+ JDBC input plugin ([download and more information](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-jdbc.html))
+ Logstash output plugin ([logstash-output-amazon\_es](https://github.com/awslabs/logstash-output-amazon_es))
+ Oracle JDBC drivers

## Epics
<a name="migrate-an-on-premises-oracle-database-to-amazon-opensearch-service-using-logstash-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify the size of the source data. | The size of the source data is one of the parameters that you use to determine the number of shards to be configured in an index. | DBA, Database developer |
| Analyze the data types of each column and corresponding data. | OpenSearch Service dynamically maps the data type when a previously unseen field is found in the document. If there are any specific data types or formats (for example, date fields) that need to be explicitly declared, identify the fields and define the mapping for those fields during index creation. | App owner, Developer, Database developer |
| Determine if there are any columns with primary or unique keys. | To avoid duplication of records in Amazon OpenSearch Service during updates or inserts, you need to configure the `document_id` setting in the output section of the `amazon_es` plugin (for example, `document_id => "%{customer_id}"` where `customer_id` is a primary key). | App owner, Developer |
| Analyze the number and frequency of new records added; check how frequently the records are deleted. | This task is required to understand the growth rate of source data. If data is intensively read and insertions are rare, you can have a single index. If new records are inserted frequently and there are no deletions, the shard size can easily exceed the recommended maximum size of 50 GB. In this case, you can dynamically create an index by configuring index patterns in Logstash and in the code where you can access it by using an alias. | App owner, Developer |
| Determine how many replicas are required. |  | App owner, Developer |
| Determine the number of shards to be configured on the index. |  | App owner, Developer |
| Identify the instance types for dedicated master nodes, data nodes, and the EC2 instance. | For more information, see the [Related resources](#migrate-an-on-premises-oracle-database-to-amazon-opensearch-service-using-logstash-resources) section. | App owner, Developer |
| Determine the number of dedicated master nodes and data nodes required. | For more information, see the [Related resources](#migrate-an-on-premises-oracle-database-to-amazon-opensearch-service-using-logstash-resources) section. |  |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch an EC2 instance. | Launch an EC2 instance within the VPC to which AWS VPN is connected. | Amazon VPC constructs, AWS VPN |
| Install Logstash on the EC2 instance. |  | Developer |
| Install the Logstash plugins. | Install the required Logstash plugins `jdbc-input` and` logstash-output-amazon_es`. | Developer |
| Configure Logstash. | Create the Logstash keystore to store sensitive information such as AWS Secrets Manager keys and database credentials, and then place the references in a Logstash configuration file. | Developer |
| Configure the dead letter queue and persistent queue. | By default, when Logstash encounters an event that it cannot process because the data contains a mapping error or some other issue, the Logstash pipeline either hangs or drops the unsuccessful event. To protect against data loss in this situation, you can configure Logstash to write unsuccessful events to a dead letter queue instead of dropping them. To protect against data loss during abnormal termination, Logstash has a persistent queue feature that will store the message queue on disk. Persistent queues provide the data durability in Logstash. | Developer |
| Create the Amazon OpenSearch Service domain. | Create the Amazon OpenSearch Service domain with an access policy that doesn't require signing requests with AWS Identity and Access Management (IAM) credentials. The Amazon OpenSearch Service domain must be created within the same VPC. You should also select the instance types and set the number of dedicated and master nodes based on your analysis. | Developer |
| Configure the required Amazon OpenSearch Service logs. | For more information, see the [OpenSearch Service documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/cloudwatch-alarms.html). |  |
| Create the index. |  | Developer |
| Start Logstash. | Run Logstash as a background service. Logstash runs the configured SQL query, pulls the data, converts it to JSON format, and feeds it to OpenSearch Service. For the initial load, do not configure the scheduler in the Logstash configuration file. | Developer |
| Check documents. | Check the number of documents on the index and whether all documents are present in the source database. During initial load, they are added to the index and used to stop Logstash. <br />Change the Logstash configuration to add a scheduler that runs at a fixed interval depending on client requirements, and restart Logstash. Logstash will pick only the records that were updated or added after the last run, and the last run timestamp is stored in the file that is configured with the property `last_run_metadata_path => "/usr/share/logstash/.logstash_jdbc_last_run"` in the Logstash configuration file. | Developer |

## Related resources
<a name="migrate-an-on-premises-oracle-database-to-amazon-opensearch-service-using-logstash-resources"></a>
+ [Recommended CloudWatch Alarms](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/cloudwatch-alarms.html)
+ [Dedicated Amazon OpenSearch Service Master Nodes](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains-dedicatedmasternodes.html)
+ [Sizing Amazon OpenSearch Service Domains](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/sizing-domains.html)
+ [Logstash documentation](https://www.elastic.co/guide/en/logstash/current/getting-started-with-logstash.html)
+ [JDBC input plugin](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-jdbc.html)
+ [Logstash output plugin](https://github.com/awslabs/logstash-output-amazon_es)
+ [Amazon OpenSearch Service website](https://aws.amazon.com/elasticsearch-service/)
