---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-group-modify.html
---

# Modify a host resource group in License Manager
<a name="host-resource-group-modify"></a>

You can modify the settings for a host resource group at any time. You cannot set the host limit lower than the number of existing hosts in the host resource group. You cannot remove an instance type if there's an instance of that type running in the host resource group.

**To modify a host resource group**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the left navigation pane, choose **Host resource groups**.

1. Select the host resource group and choose **Actions**, **Edit**.

1. Modify the settings as needed.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
