---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/manage-automated-remediation.html
---

# Manage automated remediation
<a name="manage-automated-remediation"></a>

When the Web UI is enabled, you manage automated remediation from the **Controls** page instead of editing the Remediation Configuration Amazon DynamoDB table directly. From this page you enable automated remediation for individual controls and scope which findings the solution acts on by applying reusable resource filters.

**Web UI required**
The Controls page requires the Web UI. Without the Web UI, you can manage controls and resource filters through the MCP server, or enable automated remediation by editing the Remediation Configuration DynamoDB table, as described in [Enable fully automated remediations](enable-fully-automated-remediations.md). Resource filters require the Web UI or the MCP server.

Access to the Controls page follows the same roles as the rest of the Web UI. Admins and delegated admins can enable or disable automated remediation, and create, edit, and apply filters. Account operators have read-only access to the Controls and Filters pages.

## Enable automated remediation for a control
<a name="manage-controls"></a>

The Controls page lists every security control that the solution supports, with its current automated remediation status, description, and applied filters. You can search and sort the table by control ID or filter name.

The table also shows the runbook **type** and **version** backing each control. The type is **Built-in** for a runbook that ships with the solution. The type is **Custom** for a Custom Runbook that you registered through the MCP server (see [Custom remediation runbooks](custom-remediation-runbooks.md)). A manually deployed runbook uses the built-in naming convention, so this column reports it as built-in.

The table also includes a **Rollback** column, which shows **Enabled** or **Disabled** for controls that support rollback, and **Not supported** for the rest. This column appears only when you deployed the solution with rollback enabled. For more information, see [Remediation rollback](remediation-rollback.md) and [Rolling back a remediation](rolling-back-a-remediation.md).

The following screenshot shows the Controls table filtered to Custom Runbooks. In this view, the Runbook Type column shows **Custom** and the Runbook Version column shows the deployed version, such as **v1**. The Rollback column shows **Not supported**, because rollback is available only for a defined set of built-in remediations.

 **Controls page filtered to Custom Runbooks**

![Controls table filtered to Custom Runbooks showing runbook type and version plus rollback status.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/controls-custom-runbook.png)

1. Open the Web UI and go to the **Controls** page.
![Controls table in the Web UI.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/controls-table-view.png)

1. Set the automated remediation status for one or more controls.

1. (Optional) Apply one or more resource filters to a control, and choose a filter mode (include or exclude).

1. Choose **Save** to persist your changes. The solution validates and applies all pending changes together.

**Deadline enforcement is a separate path to automated remediation**
Enabling automated remediation on this page is the primary path: when a matching finding arrives, the solution remediates it only if the control is enabled here (subject to any applied resource filters). A second, independent path exists — **deadline enforcement**. If a finding-type notification configuration has `enforceDeadline` turned on, the solution automatically remediates matching overdue findings **regardless of whether the control is enabled on this page**. If you disable a control here to prevent automated remediation, also confirm that no enforcing notification configuration matches those findings. For details, see [Deadline enforcement](configure-notifications.md#deadline-enforcement).

## Create and apply resource filters
<a name="manage-resource-filters"></a>

A resource filter is a reusable definition that scopes which findings the solution automatically remediates. Each filter can combine the following criteria:
+  **Account IDs** – One or more 12-digit AWS account IDs.
+  **Organizational units** – One or more AWS Organizations OU identifiers.
+  **ARN patterns** – One or more resource ARN patterns. Patterns support the ` ` wildcard in any ARN component (for example, `arn:aws:` matches any resource in account `111111111111`).
+  **Resource tags** – One or more tag key-value pairs. The solution ignores tag criteria for resource types that cannot be tagged, such as IAM users and AWS accounts.

To create a filter, open the **Filters** page and choose **Create filter**, then enter a unique name and the criteria to match.

![Create resource filter.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/create-resource-filter-popup.png)

You apply a filter to a single control from the Controls page, or to every control at once with the **Apply to all controls** action on the Filters page. Removing a filter works the same way. Deleting a filter removes it from every control that references it.

## How filters are evaluated
<a name="filter-evaluation"></a>

When a finding arrives, the pre-processor decides whether to automatically remediate it based on the control’s status and the filters applied to that control:
+ If automated remediation is disabled for the control, the solution does not remediate the finding.
+ If automated remediation is enabled and the control has no filters, the solution remediates the finding.
+  **Include mode** – The solution remediates the finding only when it matches **all** filters applied to the control (logical AND).
+  **Exclude mode** – The solution does not remediate the finding when it matches **any** filter applied to the control.

A finding matches a filter when it matches every criterion set in that filter: account ID, organizational unit, resource ARN pattern, and resource tags.

**Use account, OU, or ARN criteria to exclude specific resources**
Tag criteria are evaluated against the resource tags in the finding. AWS Security Hub sometimes delivers a finding without resource tags. A finding with no tags does not match tag criteria, so an exclude-mode filter with any tag criteria does not exclude it, and the finding is remediated. To reliably keep specific resources out of fully automated remediation, build exclude-mode filters from account IDs, organizational units, or ARN patterns.
