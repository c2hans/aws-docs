---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/view-import-history.html
---

# View the import history for your Connect Customer quick responses
<a name="view-import-history"></a>

Connect Customer retains import history for the lifetime of your knowledge base. To delete that history, you must use the [DeleteKnowledgeBase](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_DeleteKnowledgeBase.html) action to delete the knowledge base.

This topic explains how to use the Connect Customer admin website to view import histories. To view import histories programmatically, see [ListImportJobs](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ListImportJobs.html) in the *agent assist API Reference*.

**To view import history**

1. Log in to the Connect Customer admin website at https://*instance name*.my.connect.aws/. Use an **Admin** account, or an account assigned to a security profile that has **Content Management - Quick responses - View** permission.

1. On the left navigation bar, choose **Content Management**, then **Quick responses**.
![Menu showing Content Management and Quick responses.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-application-1.png)

1. On the **Quick responses** page, choose the **View import** history link.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
