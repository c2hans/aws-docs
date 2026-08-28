---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## Store and stage data
<a name="store-and-stage-data"></a>

This solution uses Amazon S3 to store the original raw rosbag data, also referred to as staged data. The solution processes the rosbag files and stores the extracted data, both structured and unstructured, in Amazon S3. The unstructured data is stored as .png images, and the structured data is stored as Apache Parquet data.

## Extract rosbag data
<a name="extract-rosbag-data"></a>

The solution processes the rosbag files by using an Amazon MWAA DAG that invokes several AWS services for processing. The solution performs the following actions:
+ Extracts rosbag data by using AWS Batch and custom docker images stored in private Amazon ECR repositories
+ Opens the rosbag files and extracts their sensor data
+ Writes the extracted data back to Amazon S3 as either images (.png files) or Apache Parquet data

## Detect objects and label
<a name="detect-objects-and-label"></a>

The next phase of the Amazon MWAA DAG applies object detection and LaneDet ML processing to the extracted images by using SageMaker AI processing jobs. The processing jobs use custom Docker images stored in private Amazon ECR repositories. The solution writes the resulting output to Amazon S3.

## Apply business logic to extracted data
<a name="apply-business-logic-to-extracted-data"></a>

The final stage of the Amazon MWAA DAG applies custom business logic to the extracted metadata (Apache Parquet) and the resulting output from the object detection and LaneDet processes. The business logic leverages Apache Spark and runs on Amazon EMR Serverless to process the data. The solution writes the resulting metadata output from the Apache Spark job to both Amazon S3 and DynamoDB. When the solution writes the metadata to DynamoDB, it invokes a Lambda function that forwards the data to OpenSearch Service for indexing.

## Search metadata output
<a name="search-metadata-output"></a>

After the solution writes the data to OpenSearch Service, you can query the data with [OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html). The solution provides an Amazon EC2 instance that acts as a proxy for secure communication. This proxy only allows [AWS Systems Manager](https://aws.amazon.com/systems-manager/) tunneling for port-forwarding to enable secure communication.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Scene Intelligence with Rosbag on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
