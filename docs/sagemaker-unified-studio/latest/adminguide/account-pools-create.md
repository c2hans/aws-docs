---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-create.html
---

# Create an account pool
<a name="account-pools-create"></a>

To use the AWS CLI to create an account pool, you run the **create-account-pool** command and provide the source.
+ **For Lambda handler sources**: Provide the Lambda function and an IAM role with permissions to invoke the lambda, and trusts the `datazone.amazonaws.com` service principal.
+ **For static account sources**: Provide a list of account and region pairs as key-value pairs in the command.

Once configured in your domain, account pools automatically provide account and region information when creating new projects.

**Topics**
+ [Create an account pool with a custom handler source](account-pools-create-handler.md)
+ [Create an account pool with a static list of account and region pairs](account-pools-create-static.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
