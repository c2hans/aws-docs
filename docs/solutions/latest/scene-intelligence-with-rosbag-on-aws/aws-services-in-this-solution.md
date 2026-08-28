---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/aws-services-in-this-solution.html
---

# AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [AWS Batch](https://aws.amazon.com/batch/)  |  **Core.** The solution uses AWS Batch processing for extracting Apache Parquet and PNG files. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Core.** This solution creates a DynamoDB table for tracking the batch of rosbag files, and another DynamoDB table for tracking the metadata that is generated after identifying lanes and objects from drive files. This solution uses the second DynamoDB table for downstream consuming and querying purposes. |
|  [Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html)  |  **Core.** The solution loads outputs from object detection and LaneDet into data frames and integration with the Parquet data by using Amazon EMR Serverless. This provides metadata for querying. |
|  [Amazon MWAA](https://aws.amazon.com/managed-workflows-for-apache-airflow/)  |  **Core.** Amazon MWAA orchestrates the workflow of uploading the rosbag files, extracting images and lanes from the files using open source YOLO model, and writing the required metadata to DynamoDB table. |
|  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)  |  **Core.** This solution creates an OpenSearch Service cluster for advanced querying purposes. This cluster uses the metadata from DynamoDB. |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Core.** The solution stages all rosbag input files in a source S3 bucket for raw data, and the intermediate artifacts (such as Apache Parquet, PNG, and JSON files) in an intermediate S3 bucket for staged data. |
|  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)  |  **Core.** The solution runs object detection and LaneDet jobs by using SageMaker AI processing jobs. |
|  [AWS CodeBuild](https://aws.amazon.com/codebuild/)  |  **Supporting.** AWS CodeBuild manages module deployments for this solution. |
|  [Amazon EC2](https://aws.amazon.com/ec2/)  |  **Supporting.** A micro Amazon EC2 instance acts as a secure proxy to the OpenSearch Dashboard. |
|  [Amazon ECR](https://aws.amazon.com/ecr/)  |  **Supporting.** The solution builds and stores container images related to the `ros-parquet`, `ros-png`, `lane-detection`, and `object-detection` applications in internal Amazon ECR repositories. |
|  [AWS IAM](https://aws.amazon.com/iam/)  |  **Supporting.** This solution creates IAM roles for all the AWS services that require permissions to communicate with other AWS APIs. This solution uses least-privileged IAM policies. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Supporting.** This solution uses a Lambda function to load the data from the DynamoDB table into an OpenSearch Service cluster. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting.** The solution allows Systems Manger tunneling for port forwarding to an Amazon EC2 instance in a private Amazon VPC subnet. This allows secure access to the OpenSearch Dashboard. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Scene Intelligence with Rosbag on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
