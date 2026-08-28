---
source_url: https://docs.aws.amazon.com/filegateway/latest/files3/maintenance-updates-on-off.html
---

# Turn maintenance updates on or off
<a name="maintenance-updates-on-off"></a>

When maintenance updates are turned on, your gateway automatically applies these updates according to the configured maintenance window schedule. For more information, see [Modify the gateway maintenance window schedule](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceManagingUpdate-common.html#configure-maintenance-window-schedule).

If maintenance updates are turned off, the gateway will not apply these updates automatically, but you can always apply them manually using the Storage Gateway console, API, or CLI. Urgent updates will sometimes be applied during your configured maintenance window, regardless of this setting.

**Note**
The following procedure describes how to turn gateway updates on or off using the Storage Gateway console. To change this setting programmatically using the API, see [UpdateMaintenanceStartTime](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateMaintenanceStartTime.html) in the *Storage Gateway API Reference*.

**To turn maintenance updates on or off using the Storage Gateway console:**

1. Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/).

1. On the navigation pane, choose **Gateways**, and then choose the gateway for which you want to configure maintenance updates.

1. Choose **Actions**, and then choose **Edit maintenance settings**.

1. For **Maintenance updates**, select **On** or **Off**.

1. Choose **Save changes** when finished.

You can verify the updated setting on the **Details** tab for the selected gateway in the Storage Gateway console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query filegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
