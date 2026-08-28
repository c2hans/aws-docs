---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-list-accounts.html
---

# View the list of accounts in an account pool
<a name="account-pools-list-accounts"></a>

To use the AWS CLI to view the accounts in an account pool where the source is a list of static accounts, use the `list-accounts-in-account-pool` command.
+ Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI to run the `list-accounts-in-account-pool` command with the following format, where the domain ID is a required argument.

  ```
  aws datazone list-accounts-in-account-pool --domain-identifier {{DOMAIN_ID}} --identifier {{ACCOUNT_POOL_ID}}
  ```

  Example command:

  ```
  aws datazone list-accounts-in-account-pool --domain-identifier {{dzd_dkqsou2EXAMPLE}} --identifier {{cln5qjqEXAMPLE}}
  ```

  This command returns output with the account pool account list details.

  ```
  {
      "items": [
          {
              "awsAccountId": "{{111122223333}}",
              "supportedRegions": [
                  "us-east-1"
              ],
              "awsAccountName": "ExampleAccount"
          }
      ]
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
