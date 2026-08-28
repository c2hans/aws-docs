---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/sample-use-cases.html
---

# Sample Use Cases
<a name="sample-use-cases"></a>

This library includes a collection of functional use case implementations to demonstrate the usage of Constructs architectural patterns. These can be used in the same way as architectural patterns, and can be conceptualized as an additional "higher-level" abstraction of those patterns. The following use cases are provided as functional examples.

## AWS Static S3 Website
<a name="aws-static-s3-website"></a>

This use case pattern (`aws-s3-static-website`) implements an Amazon CloudFront distribution, Amazon S3 bucket, and AWS Lambda-based custom resource to copy the static website content for the Wild Rydes demo website (part of the `aws-serverless-web-app` implementation).

**Source Code (aws-s3-static-website)**
 [https://github.com/awslabs/aws-solutions-constructs/tree/master/source/use_cases/aws-s3-static-website](https://github.com/awslabs/aws-solutions-constructs/tree/master/source/use_cases/aws-s3-static-website)

## AWS Restaurant Management Demo
<a name="aws-restaurant-management-demo"></a>

This use case pattern (`aws-restaurant-management-demo`) implements a complex, multi-stack architecture that models a restaurant management system. This use case will provision a stack for service/wait staff to open/close orders, a stack for kitchen staff to view/complete orders, and a stack for managers to perform various business functions. It will also provision a stack containing a central DynamoDB table for managing orders, as well as a Lambda layer for sharing common database access patterns.

**Source Code (aws-restaurant-management-demo)**
 [https://github.com/awslabs/aws-solutions-constructs/tree/master/source/use_cases/aws-restaurant-management-demo](https://github.com/awslabs/aws-solutions-constructs/tree/master/source/use_cases/aws-restaurant-management-demo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
