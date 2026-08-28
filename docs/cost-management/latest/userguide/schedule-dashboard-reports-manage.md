---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/schedule-dashboard-reports-manage.html
---

# Managing scheduled reports
<a name="schedule-dashboard-reports-manage"></a>

You can view, edit, disable, or delete your scheduled reports from the Dashboards list page. The **Reports** column indicates which dashboards have scheduled reports configured.

**To edit a scheduled report**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Dashboards**.

1. Select the dashboard which corresponds to the scheduled report you want to edit.

1. Click on **Actions**, and then choose **Manage email reports**.

1. Select the report you want to edit.

1. Modify the report settings as needed.

1. Choose **Save**.

**To disable a scheduled report**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Dashboards**.

1. Select the dashboard which corresponds to the scheduled report you want to disable.

1. Click on **Actions**, and then choose **Manage email reports**.

1. Select the report you want to disable.

1. Click on **Actions**, and then choose **Disable report**.

**Note**
Disabling a scheduled report stops future report generation. Download links that were already delivered remain valid until they expire, 15 days after the report was generated. PDF reports that have already been downloaded to a local device are not affected.

**To delete a scheduled report**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Dashboards**.

1. Select the dashboard which corresponds to the scheduled report you want to delete.

1. Click on **Actions**, and then choose **Manage email reports**.

1. Select the report you want to delete.

1. Click on **Actions**, and then choose **Delete report**.

1. In the dialog box that appears, enter **confirm** and choose **Delete**.

**Note**
Deleting a scheduled report does not delete any associated resources in AWS User Notifications. To remove notification configurations and email contacts, manage them directly in the AWS User Notifications console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
