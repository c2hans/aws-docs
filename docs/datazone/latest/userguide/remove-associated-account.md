---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/remove-associated-account.html
---

# Remove an associated account in Amazon DataZone
<a name="remove-associated-account"></a>

To remove an associated AWS account in the Amazon DataZone management console, you must assume an IAM role in the account with administrative permissions. [Configure the IAM permissions required to use the Amazon DataZone management console](create-iam-roles.md) to obtain the minimum permissions.

Complete the following procedure to remove an associated account from your domain.

1. Sign in to the AWS Management Console and open the Amazon DataZone management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone).

1. Choose **View Domains** and choose the domain’s name from the list. The name is a hyperlink.

1. Scroll down to the **Associated accounts** tab. Choose the account ID for the AWS account you want to remove.

1. Choose **Disassociate**. Confirm your choice by entering disassociate in the field and choosing **Disassociate**.

1. The account is now removed from your domain and cannot be used by the domain’s users to publish and consume data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
