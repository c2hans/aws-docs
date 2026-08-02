---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to this solution:

 **resource**

An AWS resource, such as an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket or [AWS Lambda](https://aws.amazon.com/lambda/) function.

 **relationship**

A link between two resources, such as an [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) role and an associated AWS Lambda function.

 **resource type**

The classification category of a resource. Always follows the CloudFormation naming convention, such as `AWS::Lambda::Function`.

 **discovery**

The process that the solution initiates to map resources and their relationships in your AWS accounts and Regions.

 **account discovery mode**

The method of discovering accounts and adding them to the solution: either self-managed through the Workload Discovery on AWS UI or delegated to AWS Organizations.

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).
