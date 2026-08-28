---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/adminguide/deleting-instance.html
---

# Deleting an instance
<a name="deleting-instance"></a>

To delete an instance, follow these steps.

**Note**
When you delete an instance, information from the Amazon S3 bucket is not automatically deleted.

1. Open the AWS Supply Chain console at [https://console.aws.amazon.com/scn/home](https://console.aws.amazon.com/scn/home).

1. On the AWS Supply Chain console dashboard, from the dropdown, select the instance that you want to delete.
![Deleting an instance.](http://docs.aws.amazon.com/connect-decisions/legacy/adminguide/images/delete_instance.png)

1. Choose **Delete**.

1. On the **Delete AWS Supply Chain Instance** page, under **Confirmation**, type **delete** to confirm that you want to delete the instance.

1. Choose **Delete**. The instance deletion starts and once the instance is deleted, you will see a confirmation message.

**Note**
After the instance is deleted, information related to Amazon Q in AWS Supply Chain is automatically deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
