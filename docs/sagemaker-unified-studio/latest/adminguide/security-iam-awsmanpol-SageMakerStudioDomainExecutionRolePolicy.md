---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.html
---

# AWS policy: SageMakerStudioDomainExecutionRolePolicy
<a name="security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy"></a>

Default policy for the SageMakerUnifiedStudioDomainExecutionRole service role. This role is used by Amazon SageMaker Unified Studio to catalog, discover, govern, share, and analyze data in the Amazon SageMaker Unified Studio domain.

This role provides access to all Amazon SageMaker Unified Studio APIs that are required for Amazon SageMaker Unified Studio use, as well as RAM permissions to support usage of associated accounts in a Amazon SageMaker Unified Studio domain. It also provides access to services used outside of a project scope, including AWS CodeConnections, Amazon Q, AWS Systems Manager, and Amazon Bedrock.

To view the permissions for this policy, see [SageMakerStudioDomainExecutionRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SageMakerStudioDomainExecutionRolePolicy.html) in the *AWS Managed Policy Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
