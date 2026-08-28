---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/view-license-configuration.html
---

# View self-managed licenses in License Manager
<a name="view-license-configuration"></a>

You can view your self-managed licenses through the License Manager console to monitor usage, compliance, and distribution across your AWS environment.

## View licenses in a single account
<a name="view-single-account-licenses"></a>

To view self-managed licenses within your current account:

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the left navigation pane, choose **Self-managed licenses**.

1. Review the list of licenses, their status, and current usage.

1. Choose a license name to view detailed information including associated resources and compliance status.

## View aggregated licenses (For Organization Administrator or Delegated Administrator)
<a name="view-aggregated-licenses"></a>

Organization Administrators and Delegated Administrators can view self-managed licenses across all AWS accounts in their organization from a centralized location. This provides organization-wide visibility and management capabilities for license compliance.

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Ensure you are signed in as an Organization Administrator or Delegated Administrator.

1. In the left navigation pane, choose **Self-managed licenses**.

1. Choose the **Organization license configuration** tab to view the aggregated license view.

1. Review the aggregated view of all self-managed licenses across your organization's accounts.

This aggregated view enables centralized license governance and helps ensure compliance across your entire AWS organization.

**To view aggregated licenses using the command line**
+ [list-license-configurations-for-organization](https://docs.aws.amazon.com/cli/latest/reference/license-manager/list-license-configurations-for-organization.html) (AWS CLI)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
