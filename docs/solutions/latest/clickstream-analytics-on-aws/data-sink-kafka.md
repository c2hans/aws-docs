---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/data-sink-kafka.html
---

# Data sink – Kafka
<a name="data-sink-kafka"></a>

 This data sink will stream the clickstream data collected by the ingestion endpoint into a topic in a Kafka cluster. Currently, guidance support Amazon Managed Streaming for Apache Kafka (Amazon MSK) or a self-hosted Kafka cluster.

## Amazon MSK
<a name="amazon-msk"></a>
+  **Select an existing Amazon MSK cluster.** Select an MSK cluster from the drop-down list, and the MSK cluster needs to meet the following requirements:
  +  MSK cluster and this guidance need to be in the same VPC
  +  Enable **Unauthenticated access** in Access control methods
  +  Enable **Plaintext** in Encryption
  +  Set **auto.create.topics.enable** as true in MSK cluster configuration. This configuration sets whether MSK cluster can create topic automatically.
  +  The value of **default.replication.factor** cannot be larger than the number of MKS cluster brokers

**Note**
 If there is no MSK cluster, the user needs to create an MSK Cluster following above requirements.
+  **Topic**: The user can specify a topic name. By default, the guidance will create a topic with “project-id”.

## Self-hosted Kafka
<a name="self-hosted-kafka"></a>

 Users can also use self-hosted Kafka clusters. To integrate the guidance with Kafka clusters, provide the following configurations:
+  **Broker link**: Enter the brokers link of Kafka cluster that you wish to connect to. The Kafka cluster needs to meet the following requirements:
  +
    + The Kafka cluster and this guidance need to be in the same VPC.
    + At least two Kafka cluster brokers are available.
+  **Topic**: User can specify the topic for storing the data
+  **Security Group**: This VPC security group defines which subnets and IP ranges can access the Kafka cluster.

## Connector
<a name="connector"></a>

 Enable guidance to create Kafka connector and a custom plugin for this connector. This connector will sink the data from Kafka cluster to S3 bucket.

## Additional Settings
<a name="additional-settings"></a>
+  **Sink maximum interval**: Specifies the maximum length of time (in seconds) that records should be buffered before streaming to the AWS service.
+  **Batch size**: The maximum number of records to deliver in a single batch.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
