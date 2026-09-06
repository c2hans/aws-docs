---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/manage-automated-remediation.html
---

# Manage automated remediation
<a name="manage-automated-remediation"></a>

When the Web UI is enabled, you manage automated remediation from the **Controls** page instead of editing the Remediation Configuration Amazon DynamoDB table or the AWS Systems Manager parameters directly. From this page you enable automated remediation for individual controls and scope which findings the solution acts on by applying reusable resource filters.

**Web UI required**
The Controls page and resource filters require the Web UI. If you did not deploy the Web UI, configure automated remediation through the Remediation Configuration DynamoDB table and the Systems Manager filter parameters, as described in [Enable fully-automated remediations](enable-fully-automated-remediations.md).

Access to the Controls page follows the same roles as the rest of the Web UI. Admins and delegated admins can enable or disable automated remediation, and create, edit, and apply filters. Account operators have read-only access to the Controls and Filters pages.

## Enable automated remediation for a control
<a name="manage-controls"></a>

The Controls page lists every security control that the solution supports, with its current automated remediation status, description, and applied filters. You can search and sort the table by control ID or filter name.

1. Open the Web UI and go to the **Controls** page.
![Controls table in the Web UI.](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/controls-table-view.png)

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

![Create resource filter.](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/create-resource-filter-popup.png)

You apply a filter to a single control from the Controls page, or to every control at once with the **Apply to all controls** action on the Filters page. Removing a filter works the same way. Deleting a filter removes it from every control that references it.

## How filters are evaluated
<a name="filter-evaluation"></a>

When a finding arrives, the pre-processor decides whether to automatically remediate it based on the control’s status and the filters applied to that control:
+ If automated remediation is disabled for the control, the solution does not remediate the finding.
+ If automated remediation is enabled and the control has no filters, the solution remediates the finding.
+  **Include mode** – The solution remediates the finding only when it matches **all** filters applied to the control (logical AND).
+  **Exclude mode** – The solution does not remediate the finding when it matches **any** filter applied to the control.

A finding matches a filter when the finding’s account ID, organizational unit, resource ARN, or resource tags match the corresponding criteria in the filter.
