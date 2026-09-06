---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

 **Data flows from test vehicles through ingestion extraction, and analytics. Full text description follows**

![scene intelligence with rosbag on aws](http://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/scene-intelligence-with-rosbag-on-aws.png)

The high-level process flow for the solution components deployed with the CloudFormation template is as follows:

1. The AV uploads the rosbag file to [Amazon S3](https://aws.amazon.com/s3/). The end user invokes the workflow to start processing through [Amazon MWAA](https://aws.amazon.com/managed-workflows-for-apache-airflow/) and a DAG. See [Invoke the DAG](invoke-the-dag.md) for instructions on this process.

1.  [AWS Batch](https://aws.amazon.com/batch/) performs the following actions:

   1. Pulls the rosbag file from Amazon S3

   1. Parses and extracts the sensor and image data

   1. Writes this data to another S3 bucket

1.  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) applies object detection and LaneDet models to the extracted data. SageMaker AI then writes the data and labels to another S3 bucket.

1.  [Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/) (with an Apache Spark job) applies business logic to the data and labels in Amazon S3. This generates metadata related to the object detection and LaneDet. Amazon EMR Serverless then writes the metadata to [DynamoDB](https://aws.amazon.com/dynamodb/) and another S3 bucket.

1. An [AWS Lambda](https://aws.amazon.com/lambda/) function publishes new incoming DynamoDB data (metadata) to the [OpenSearch Service](https://aws.amazon.com/opensearch-service/) cluster. The end user accesses the OpenSearch Service cluster through a proxy on [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) to submit queries against the metadata.
