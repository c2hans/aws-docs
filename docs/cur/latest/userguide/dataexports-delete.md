---
source_url: https://docs.aws.amazon.com/cur/latest/userguide/dataexports-delete.html
---

# Deleting exports
<a name="dataexports-delete"></a>

You can use the **Data Exports** page in the AWS Billing and Cost Management console to delete your exports.

**To delete an export**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Data Exports**.

1. From your list of exports, choose the name of the export that you want to delete.

1. On the **Export details** page, choose **Delete**.

1. Choose **Delete** once more to confirm that you want to delete the export.

**Note**
This procedure deletes your export from Data Exports. However, it doesn't delete the objects stored in your Amazon S3 bucket.
For a Cost and Usage Dashboard, the above procedure deletes the Cost and Usage Dashboard from Data Exports. However, it doesn't delete the objects stored in your S3 bucket, QuickSight dashboard, and additional QuickSight resources. To delete your Cost and Usage Dashboard from QuickSight, see [Deleting an Amazon QuickSight dashboard](https://docs.aws.amazon.com/quicksight/latest/user/deleting-a-dashboard.html).
When you delete an Amazon QuickSight dashboard, the dashboard is permanently removed from your account and all folders the dashboard was a part of. You'll no longer be able to access the deleted dashboard. You can only delete dashboards that you own or co-own.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cur` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
