---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/generative-bi-q-business-delete-connection.html
---

# Disconnect an Amazon Q Business application from an Amazon Quick account
<a name="generative-bi-q-business-delete-connection"></a>

Quick account admins can use the following procedure to disconnect an Amazon Q Business application from a Quick account.

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. Choose the user icon at the top right, and then choose **Manage Quick**.

1. Choose **Security & permissions**.

1. On the **Quick access to AWS services** page, choose **SELECT APPLICATION**.

1. Perform one of the following options:

   1. To disconnect a single Amazon Q Business application from a Quick account, navigate to the application that you want to remove, open the dropdown, and choose **NONE**.

   1. To disconnect all Amazon Q Business applications from a Quick account, uncheck the **Amazon Q Business application** checkbox.

When you disconnect an Amazon Q Business application from a Quick account, the Amazon Q Business application that you created for Quick is not deleted. The application, index, retriever, and any unstructured data source connections that you configured remain in your Amazon Q Business account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
