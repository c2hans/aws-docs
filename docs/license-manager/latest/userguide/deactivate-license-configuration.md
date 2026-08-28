---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/deactivate-license-configuration.html
---

# Deactivate a self-managed license in License Manager
<a name="deactivate-license-configuration"></a>

When you deactivate a self-managed license, existing resources using the license are unaffected and AMIs using the license can still be launched. However, license consumption is no longer tracked.

When a self-managed license is deactivated, it must not be attached to any running instance. After deactivation, launches cannot be performed with the self-managed license.

**To deactivate a self-managed license**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the left navigation pane, choose **self-managed licenses**.

1. Select the self-managed license.

1. Choose **Actions**, **Deactivate**. When prompted for confirmation, choose **Deactivate**.

**To deactivate a self-managed license using the command line**
+ [update-license-configuration](https://docs.aws.amazon.com/cli/latest/reference/license-manager/update-license-configuration.html) (AWS CLI)
+ [Update-LICMLicenseConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-LICMLicenseConfiguration.html) (AWS Tools for PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
