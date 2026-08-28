---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/pull-requests-close.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Closing a pull request
<a name="pull-requests-close"></a>

You can mark a pull request as **Closed**. This does not merge the pull request, but it can help you determine which pull requests require action and which pull requests are no longer relevant. We recommend closing a pull request if you no longer plan to merge those changes, or if the changes were merged by another pull request.

Closing a pull request will automatically send an email to the creator of the pull request as well as any required or optional reviewers. It will not automatically change the status of any issues linked to the pull request.

**Note**
You cannot re-open a pull request after it has been closed.<a name="pull-requests-close-pull-request"></a>

**To close a pull request**

1. Navigate to the project where you want to close a pull request.

1. On the project page, open pull requests are displayed. Choose the pull request that you want to close.

1. Choose **Close**.

1. Review the information, and then choose **Close pull request**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
