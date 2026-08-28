---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security-service-roles.html
---

# Service role requirements for model evaluation jobs
<a name="model-evaluation-security-service-roles"></a>

To create a model evaluation job, you must specify a service role. A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*.

The required IAM actions and resource depend on the type of model evaluation job you are creating. Use the following sections to learn more about the required Amazon Bedrock,Amazon SageMaker AI, and Amazon S3 IAM actions, service principals, and resources. You can optionally choose to encrypt your data using AWS Key Management Service.

**Topics**
+ [Service role requirements for automatic model evaluation jobs](automatic-service-roles.md)
+ [Service role requirements for human-based model evaluation jobs](model-eval-service-roles.md)
+ [Required service role permissions for creating a model evaluation job that uses a judge model](judge-service-roles.md)
+ [Service role requirements for knowledge base evaluation jobs](rag-eval-service-roles.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
