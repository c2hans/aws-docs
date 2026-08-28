---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/modify-license-configuration.html
---

# Edit a self-managed license in License Manager
<a name="modify-license-configuration"></a>

You can edit values for the following fields in a self-managed license:
+ Self-managed license name
+ Description
+ Expiry Date
+ Number of <option>
+ Enforce license type limit
+ Include stopped instances

**To edit a self-managed license**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the left navigation pane, choose **self-managed licenses**.

1. Select the self-managed license.

1. Choose **Actions**, **Edit**.

1. Edit the details as needed and then choose **Update**.

**Note**
Once the License Expiry Date is set, License Manager can send notifications on 120 days, 90 days, 60 days, 30 days, 0 day to the Amazon SNS topic that's configured in [Managed license settings in License Manager](settings-managed-licenses.md).

**To edit a self-managed license using the command line**
+ [update-license-configuration](https://docs.aws.amazon.com/cli/latest/reference/license-manager/update-license-configuration.html) (AWS CLI)
+ [Update-LICMLicenseConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-LICMLicenseConfiguration.html) (AWS Tools for PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
