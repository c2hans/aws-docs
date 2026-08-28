---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/settings-managed-licenses.html
---

# Managed license settings in License Manager
<a name="settings-managed-licenses"></a>

The following settings are available for managed licenses.

## License asset discovery and ruleset settings
<a name="settings-license-asset-groups"></a>

For organizations using License asset groups, you can configure license asset discovery and ruleset settings to enable cross-region discovery and organization-wide license management across multiple AWS regions and accounts within your AWS Organizations.

License asset discovery settings include:
+ Region discovery configuration to select source AWS regions for software discovery
+ Organization-wide discovery settings for organization owners

## Account details
<a name="settings-account-details"></a>

You can review your account details to see information such as the account type, whether accounts in AWS Organizations are linked, the account's License Manager S3 bucket ARN, and the AWS Resource Access Manager share ARN. This section also enables you to link your AWS Organizations accounts.

To distribute managed entitlements or self-managed licenses within your organization, choose **Link AWS Organizations accounts**. The distributed grants for managed entitlements are auto-accepted by all of your member accounts. When you select this option, we add a service-linked role to the [ management](management-role.md) and [member](member-role.md) accounts.

**Note**
To enable this option, sign in to your management account and enable all features in AWS Organizations. For more information, see [Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *AWS Organizations User Guide*.
 This selection also creates an AWS Resource Access Manager resource share in your management account, which allows you to seamlessly share self-managed licenses. For more information, see the [AWS Resource Access Manager User Guide](https://docs.aws.amazon.com/ram/latest/userguide).

To disable this option, call the [UpdateServiceSettings](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateServiceSettings.html) API.

## Cross-account resource discovery
<a name="settings-resource-discovery"></a>

You can turn on cross-account resource discovery in order to manage license usage across all of your accounts in AWS Organizations.

To enable cross-account resource discovery in your organization, choose **Turn on** for cross-account resource discovery. When you turn on the cross-account resource discovery, AWS Organizations is automatically linked to perform resource discovery across all of your accounts.

License Manager uses [Systems Manager inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) to discover software usage. Verify that you have configured Systems Manager inventory on all of your resources. Querying Systems Manager inventory requires a [resource data sync](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-datasync.html) to store inventory in an Amazon S3 bucket.

## Simple Notification Service (SNS)
<a name="settings-sns"></a>

You can configure an Amazon SNS to receive notifications and alerts from License Manager.

**To configure an Amazon SNS topic**

1. Choose **Edit** next to **Simple Notification Service (SNS)**.

1. Specify an SNS topic ARN in the following format:

   `arn:{{<aws_partition>}}:sns:{{<region>}}:{{<account_id>}}:aws-license-manager-service-*`

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
