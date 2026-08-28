---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-prerequisites.html
---

# Prerequisites
<a name="pb-aoss-prerequisites"></a>

Confirm all of the following before you start:
+ The source Amazon OpenSearch Service domain is healthy and reachable, and you know its HTTPS endpoint and engine version.
+ You have AWS credentials with permission to create Amazon OpenSearch Serverless NextGen security policies, access policies, and collections (`aoss:CreateSecurityPolicy`, `aoss:CreateAccessPolicy`, `aoss:CreateCollection`, `aoss:BatchGetCollection`), and to register an Amazon S3 snapshot repository on the source domain.
+ Migration Assistant is deployed on [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks). See [Deploy the solution](deploy-the-solution.md).
+ The source domain and the collection endpoint are reachable from the Amazon EKS cluster. If either is in a VPC, the cluster’s networking and the collection’s network policy must allow that path.
+ An [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3) bucket is available for the snapshot repository. Migration Assistant provisions a default bucket named `s3://migrations-default-<ACCOUNT_ID>-<STAGE>-<REGION>`.
+ You have identified the AWS Region for the migration and have a naming convention for the collection and its policies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
