---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/idt-usage-metrics.html
---

# Submit IDT usage metrics
<a name="idt-usage-metrics"></a>

If you provide AWS credentials with required permissions, AWS IoT Device Tester collects and submits usage metrics to AWS. This is an opt-in feature and is used to improve IDT functionality. IDT collects information such as the following:
+ The AWS account ID used to run IDT
+  The IDT CLI commands used to run tests
+ The test suite that are run
+ The test suites in the {{<device-tester-extract-location>}} folder
+ The number of devices configured in the device pool
+ Test case names and run times
+ Test result information, such as whether tests passed, failed, encountered errors, or were skipped
+ Product features tested
+ IDT exit behavior, such as unexpected or early exits

 All of the information that IDT sends is also logged to a `metrics.log` file in the `{{<device-tester-extract-location>}}/results/{{<execution-id>}}/` folder. You can view the log file to see the information that was collected during a test run. This file is generated only if you choose to collect usage metrics.

To disable metrics collection, you do not need to take additional action. Simply do not store your AWS credentials, and if you do have stored AWS credentials, do not configure the `config.json` file to access them.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

## Provide AWS credentials to IDT
<a name="idt-metrics-creds"></a>

To allow IDT to access your AWS credentials and submit metrics to AWS, do the following:

1. Store the AWS credentials for your IAM user as environment variables or in a credentials file:

   1. To use environment variables, run the following command:

      ```
      AWS_ACCESS_KEY_ID={{access-key}}
      AWS_SECRET_ACCESS_KEY={{secret-access-key}}
      ```

   1. To use the credentials file, add the following information to the `.aws/credentials file:`

      ```
      [profile-name]
      aws_access_key_id={{access-key}}
      aws_secret_access_key={{secret-access-key}}
      ```

1. Configure the `auth` section of the `config.json` file. For more information, see [(Optional) Configure config.json](set-config-custom.md#config-json-custom).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
