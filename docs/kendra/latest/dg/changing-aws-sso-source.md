---
source_url: https://docs.aws.amazon.com/kendra/latest/dg/changing-aws-sso-source.html
---

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Changing your IAM Identity Center identity source
<a name="changing-aws-sso-source"></a>

**Warning**
Changing your identity source in IAM Identity Center **Settings** might affect the preservation of user and group information. To do this safely, it is recommended you review [Considerations for changing your identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-considerations.html). When you change your identity source, a new identity source ID is generated. Check you are using the correct ID before you set the mode to `AWS_SSO` in [UserGroupResolutionConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UserGroupResolutionConfiguration.html).

**To change your IAM Identity Center identity source**

1. Open the [IAM Identity Center> console](https://console.aws.amazon.com/singlesignon).

1. Choose **Settings**.

1. On the **Settings** page, under **Identity source**, choose **Change**.

1. On the **Change identity source** page, select your preferred identity source, and then choose **Next**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
