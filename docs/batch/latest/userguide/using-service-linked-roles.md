---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/using-service-linked-roles.html
---

# Using service-linked roles for AWS Batch
<a name="using-service-linked-roles"></a>

AWS Batch uses AWS Identity and Access Management (IAM) [ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS Batch. Service-linked roles are predefined by AWS Batch and include all the permissions that the service requires to call other AWS services on your behalf.

AWS Batch uses two different service-linked roles:
+ [AWSServiceRoleForBatch](using-service-linked-roles-batch-general.md) - For AWS Batch operations including compute environments.
+ [AWSServiceRoleForAWSBatchWithSagemaker](using-service-linked-roles-batch-sagemaker.md) - For SageMaker AI workload management and queuing.

**Topics**
+ [Using roles for AWS Batch](using-service-linked-roles-batch-general.md)
+ [Using roles for AWS Batch with SageMaker AI](using-service-linked-roles-batch-sagemaker.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
