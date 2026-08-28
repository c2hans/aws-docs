---
source_url: https://docs.aws.amazon.com/glue/latest/dg/circleci-configuring.html
---

# Configuring CircleCI
<a name="circleci-configuring"></a>

Before you can use AWS Glue to transfer data from CircleCI, you must meet these requirements:

## Minimum requirements
<a name="circleci-configuring-min-requirements"></a>

The following are minimum requirements:
+ You have an account with CircleCI that contains the data that you want to transfer.
+ In the user settings for your account, you've created a personal API token. For more information, see [Creating a personal API token](https://circleci.com/docs/managing-api-tokens/#creating-a-personal-api-token).
+ You provide the personal API token to AWS Glue while creating the connection.

If you meet these requirements, you’re ready to connect AWS Glue to your CircleCI account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
