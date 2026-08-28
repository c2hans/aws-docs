---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-add-delegated-administrator.html
---

# Add a CloudTrail delegated administrator
<a name="cloudtrail-add-delegated-administrator"></a>

You can add a delegated administrator to manage an organization's CloudTrail resources, such as trails and event data stores.

You can add a CloudTrail delegated administrator for your AWS organization using the CloudTrail console or the AWS CLI.

Before you add a delegated administrator, be sure they have an account in your organization and you are signed in with the management account for your organization. For information about how to create a new AWS account for your organization, see [Creating an AWS account in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html). For information about how to invite an existing AWS account to your organization, see [Inviting an AWS account to join your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html).

------
#### [ CloudTrail console ]

The following procedure shows you how to add a CloudTrail delegated administrator using the CloudTrail console.

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. Choose **Settings** in the left navigation pane of the CloudTrail console.

1. In the **Organization delegated administrators** section, choose **Register administrator**.

1. Enter the twelve-digit AWS account ID of the account that you want to assign as the CloudTrail delegated administrator for the organization's trails and event data stores.

1. Choose **Register administrator**.

------
#### [ AWS CLI ]

The following example adds a CloudTrail delegated administrator.

```
aws cloudtrail register-organization-delegated-admin
  --member-account-id="{{memberAccountId}}"
```

This command produces no output if it's successful.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
