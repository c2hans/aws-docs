---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/introduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Introduction
<a name="introduction"></a>

 When running genomics workloads in the Amazon Web Services (AWS) Cloud, how does an organization manage cost, optimize workload performance, and move fast with control? How does an organization secure sensitive information? What resources are available to help meet a team’s compliance needs? How does an organization perform analytics using machine learning?

 This paper answers these questions by showing how to build a next-generation sequencing (NGS) platform from instrument to interpretation using AWS services. We’ll provide recommendations and reference architectures for developing the platform including: 1) transferring genomics data to the AWS Cloud and establishing data access patterns, 2) running secondary analysis workflows, 3) performing tertiary analysis with data lakes, and 4) performing tertiary analysis using machine learning.

 The genomics market is highly competitive so having a development lifecycle that allows you to move fast with control is critical. Solutions for three of the reference architectures in this paper are provided in AWS Solutions Implementations. These solutions leverage continuous delivery (CD), allowing you to develop the solution to fit your organizational need.

**Note**
To access guidance providing an AWS CloudFormation template to automate the deployment of the secondary analysis solution in the AWS Cloud, see [Genomics Secondary Analysis Using AWS Step Functions and AWS Batch](https://aws.amazon.com/solutions/implementations/genomics-secondary-analysis-using-aws-step-functions-and-aws-batch/).
To access an AWS Solution Implementation providing an AWS CloudFormation template to automate the deployment of the tertiary analysis and data lakes solution in the AWS Cloud, see the [Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS Implementation Guide](https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/solution-overview.html).
To access guidance providing an AWS CloudFormation template to automate the deployment of the tertiary analysis and machine learning solution in the AWS Cloud, see [Genomics Tertiary Analysis and Machine Learning using Amazon SageMaker AI](https://aws.amazon.com/solutions/implementations/genomics-tertiary-analysis-and-machine-learning-using-amazon-sagemaker/).

 A summary of the services used in this platform is shown in Table 1. You can learn about the compliance resources available to you in [Compliance resources](appendix-d-compliance-resources.md).

 Table 1 – AWS services for data transfer, secondary analysis, and tertiary analyses

|  Data Transfer  |  Secondary Analysis  |  Tertiary Analysis  |
| --- | --- | --- |
|  **Data Access Patterns** <br /> AWS DataSync <br /> AWS Storage Gateway for files  |  **Secondary Analysis** <br /> AWS Step Functions <br /> AWS Batch  |  **Data Lakes** <br /> Amazon Athena <br /> AWS Glue  |
|  **Cost Optimization** <br /> AWS DataSync <br /> Amazon S3  |  **Monitor & Alert** <br /> Amazon CloudWatch  |  **Machine Learning** <br /> Amazon SageMaker AI  |
|   |  **DevOps** <br /> AWS CodeCommit <br /> AWS CodeBuild <br /> AWS CodePipeline  |  **DevOps** <br /> AWS CodeCommit <br /> AWS CodeBuild <br /> AWS CodePipeline  |
