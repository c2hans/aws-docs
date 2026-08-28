---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/create-ota-user-policy.html
---

# Create an OTA user policy
<a name="create-ota-user-policy"></a>

You must grant your user permission to perform over-the-air updates. Your user must have permissions to:
+ Access the S3 bucket where your firmware updates are stored.
+ Access certificates stored in AWS Certificate Manager.
+ Access the AWS IoT MQTT-based file delivery feature.
+ Access FreeRTOS OTA updates.
+ Access AWS IoT jobs.
+ Access IAM.
+ Access Code Signing for AWS IoT. See [Grant access to code signing for AWS IoT](code-sign-policy.md).
+ List FreeRTOS hardware platforms.
+ Tag and untag AWS IoT resources.

To grant your user the required permissions, see [IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html). Also see [Authorizing users and cloud services to use AWS IoT Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iam-policy-users-jobs.html).

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
