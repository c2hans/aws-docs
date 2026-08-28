---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-delete.html
---

# Delete an account pool
<a name="account-pools-delete"></a>

To use the AWS CLI to delete an account pool, use the `delete-account-pool` command.

**Important**
This operation will delete the account pool for the domain. This operation cannot be undone.
+ Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI to run the `delete-account-pool` command with the following format, where the domain ID and account pool ID are required arguments.

  ```
  aws datazone delete-account-pool --domain-identifier {{DOMAIN_ID}} --identifier {{ACCOUNT_POOL_ID}}
  ```

  Example command:

  ```
  aws datazone delete-account-pool --domain-identifier {{dzd_dkqsou2EXAMPLE}} --identifier 5htvndro7wd89z
  ```

  This command performs the deletion and does not return any output.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
