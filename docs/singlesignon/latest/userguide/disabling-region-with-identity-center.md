---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/disabling-region-with-identity-center.html
---

# Disabling an AWS Region where IAM Identity Center is enabled
<a name="disabling-region-with-identity-center"></a>

If you disable an AWS Region in which IAM Identity Center is installed, IAM Identity Center is also disabled. After IAM Identity Center is disabled in a Region, users in that Region won’t have single sign-on access to AWS accounts and applications.

To re-enable IAM Identity Center in [opt-in AWS Regions](regions.md#manually-enabled-regions), you must re-enable the Region. Because IAM Identity Center must reprocess all paused events, re-enabling IAM Identity Center might take some time.

**Note**
IAM Identity Center can manage access only to the AWS accounts that are enabled for use in an AWS Region. To manage access across all accounts in your organization, enable IAM Identity Center in the management account in an AWS Region that is automatically activated for use with IAM Identity Center.

For more information about enabling and disabling AWS Regions, see [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the *AWS General Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
