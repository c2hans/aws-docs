---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-considerations.html
---

# Considerations
<a name="account-pools-considerations"></a>

The following considerations apply for account pools in Amazon SageMaker Unified Studio.
+ Account pools contain a list of accounts where each account has an associated region.
+ You can have up to 100 account pools per domain. For details, see [Quotas and limits for Amazon SageMaker Unified Studio](quotas.md).
+ Account pools are not supported by Amazon Datazone domains.
+ You can configure custom project profiles to use account pools using either the console or the CLI. Steps for the creation, update, and deletion of account pools are only supported in the AWS CLI.

For more information about creating a custom project profile with an account pool, see [Project profiles in Amazon SageMaker Unified Studio](project-profiles.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
