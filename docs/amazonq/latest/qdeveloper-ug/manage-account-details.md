---
source_url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/manage-account-details.html
---

# Finding the Start URL for use with Amazon Q Developer
<a name="manage-account-details"></a>

**Note**
This section does not apply to personal accounts (Builder IDs).

If you're an administrator who has subscribed a set of IAM Identity Center workforce users to the Pro tier, those users will need to sign in to Amazon Q in their IDE or at the command line using your IAM Identity Center's Start URL and Region. If you need to provide this URL to your users, you can find it in the Amazon Q Developer console, on the **Settings** page. The start URL is specific to your organization.

**To find the Start URL**

1. Sign in to the AWS Management Console.

1. Switch to the Amazon Q Developer console.

   To use the Amazon Q Developer console, you must have the permissions defined in [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users) .

1. Choose **Settings**.

   The start URL is shown in **Start URL** near the top of the page. The start URL is specific to your organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
