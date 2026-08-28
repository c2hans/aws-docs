---
source_url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/dashboard-disabling.html
---

# Disabling the Amazon Q Developer dashboard
<a name="dashboard-disabling"></a>

You might want to disable the Amazon Q Developer dashboard if you have concerns about data privacy, page load times, or other potential issues. When you disable the dashboard, the dashboard page (and any links to it) will no longer be available in the Amazon Q Developer console.

For more information about the dashboard, see [Viewing usage metrics (dashboard)](dashboard.md).

**To disable the dashboard**

1. Open the Amazon Q Developer console:
   + If you set up Amazon Q Developer with an organization instance of AWS IAM Identity Center, then sign in using a management account or member account.
   + If you set up Amazon Q Developer with an account instance of IAM Identity Center, then sign in using the account associated with that instance.

1. Choose **Settings**, and in the **Amazon Q Developer user activity** section, choose **Edit**.

1. Disable **Amazon Q Developer usage dashboard**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
