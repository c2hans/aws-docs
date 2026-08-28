---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/deleting-review-templates.html
---

# Deleting a review template in AWS WA Tool
<a name="deleting-review-templates"></a>

**To delete a review template**

1. Select **Review templates** in the left navigation pane.

1. In the **Review templates** section, choose the review template you want to delete and in the **Actions** dropdown, select **Delete**.
**Note**
You may also select the name of the template and choose **Delete** from the review template **Overview** tab.

1. In the **Delete** review template dialog box, enter the name of the review template in the field to confirm deletion.

1. Choose **Delete**.

You cannot create a new workload from a review template that has been deleted. If you have shared a review template that you deleted with other IAM users, accounts, or organizations, they will not be able to create workloads from it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
