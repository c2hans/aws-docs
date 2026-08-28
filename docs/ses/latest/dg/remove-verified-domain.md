---
source_url: https://docs.aws.amazon.com/ses/latest/dg/remove-verified-domain.html
---

# Delete an identity using the SES console
<a name="remove-verified-domain"></a>

You can use the Amazon SES console to remove a domain or email address identity from your account in the selected AWS Region.

**To remove a domain or email address identity**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the console, use the Region selector to choose the AWS Region from which you want to delete one or more identities.

1. In the navigation pane, under **Configuration**, choose **Verified identities**.

   The **Loaded identities** table displays a list of both domain and email address identities.

1. In the **Identity** column, select the identity that you want to delete. You can delete multiple identities by checking the box next to each identity that you want to delete.

1. Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
