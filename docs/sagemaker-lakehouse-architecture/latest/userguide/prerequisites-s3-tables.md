---
source_url: https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/prerequisites-s3-tables.html
---

# Prerequisites for onboarding data to the lakehouse architecture of Amazon SageMaker
<a name="prerequisites-s3-tables"></a>

Before onboarding data into the lakehouse architecture, ensure you have completed the initial setup. For detailed setup instructions, see [Getting started with the lakehouse architecture of Amazon SageMaker](lakehouse-get-started.md).
+ AWS account with access to the following AWS services:
  + Amazon S3 including S3 Tables
  + IAM
  + Amazon SageMaker Unified Studio
  + AWS Lake Formation and AWS Glue Data Catalog
  + AWS Glue
+ [Create a user with administrative access](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/setting-up.html#create-an-admin).
+ Have access to an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that is a Lake Formation data lake administrator. For instructions, refer to [Create a data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin).
+ [Enable IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html) in the same AWS Region where you want to create your Amazon SageMaker Unified Studio domain. Set up your identity provider (IdP) and synchronize identities and groups with [IAM Identity Center](https://aws.amazon.com/iam/identity-center/). For more information, refer to [IAM Identity Center Identity source tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker lakehouse architecture. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-lakehouse-architecture` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
