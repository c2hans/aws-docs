---
source_url: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/delete-cost-categories.html
---

# Deleting cost categories
<a name="delete-cost-categories"></a>

You can delete your cost categories using the following procedure. <a name="edit-cost-categories-steps"></a>

**To delete a cost category**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost categories**.

1. Select the cost category to delete.

1. Choose **Delete cost category**.

**Note**
The deletion of a cost category takes effect starting the current billing month. For example, if you deleted `CostCategoryA` on September 15th, `CostCategoryA` would no longer be visible in reports generated from September onwards. However, it would appear in AWS Cost Explorer reports for the periods prior to September.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awsaccountbilling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
