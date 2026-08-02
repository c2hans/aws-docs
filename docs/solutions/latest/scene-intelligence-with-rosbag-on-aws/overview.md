---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/overview.html
---

# Extract sensor data and apply object detection with custom business logic
<a name="overview"></a>

Scene Intelligence with Rosbag on AWS provides an end-to-end solution for extracting sensor data from [rosbag](http://wiki.ros.org/rosbag) files generated from autonomous driving use cases. This solution guides users through a sample use case to demonstrate how the processing occurs and where custom logic can be applied to the extracted data. You can use this solution to:
+ Stage sample rosbag files
+ Extract rosbag sensor data such as metadata and images
+ Apply object detection ([YOLOv5](https://pytorch.org/hub/ultralytics_yolov5/)) and lane detection ([LaneDet](https://github.com/Turoad/lanedet)) models to extracted images
+ Apply scene detection business logic and store the output in an indexable fashion, using [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)

This implementation guide provides an overview of the Scene Intelligence with Rosbag on AWS solution, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the solution to the Amazon Web Services (AWS) Cloud.

The intended audience for using this solution’s features and capabilities in their environment includes solution architects, business decision makers, DevOps engineers, data scientists, and cloud professionals.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution.<br />The estimated cost for running this solution in the **US East (N. Virginia)** Region is **USD $605.13 per month** for AWS resources. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security-1.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know which AWS Regions support this solution. |  [Supported AWS Regions](supported-aws-regions.md)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation template](aws-cloudformation-template-for-deployment.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/awslabs/autonomous-driving-data-framework/tree/SO0279-v1.0.2)  |
