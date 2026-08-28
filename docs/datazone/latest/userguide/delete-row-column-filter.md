---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/delete-row-column-filter.html
---

# Delete row or column filters in Amazon DataZone
<a name="delete-row-column-filter"></a>

To delete a row or a column filter, follow the steps below:

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and sign in with the AWS account where the domain was created, then choose **Open data portal**.

1. Navigate to the **Data** tab for the project.

1. Choose **Published data** or **Inventory data** from the left navigation pane, then select the asset where you want to delete a row or a column filter.

1. On the asset details page, go to the **Asset filters** tab and then open the filter you want to delete.

1. Choose **Actions**, **Delete** and then confirm the deletion.

**Note**
You can delete a filter only if it is not being used in active subscriptions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
