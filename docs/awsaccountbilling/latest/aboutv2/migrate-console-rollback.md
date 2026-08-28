---
source_url: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/migrate-console-rollback.html
---

# Rollingback your bulk migration policy changes
<a name="migrate-console-rollback"></a>

You can rollback all policy changes you make during the bulk migration process safely, using the steps provided in the bulk migration tool. The rollback feature works at an account-level. You can rollback policy updates for all accounts, or specific groups of migrated accounts. However, you can't rollback changes for specific policies in an account.

**To rollback bulk migration changes**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).

1. In the search bar at the top of the page, enter **Bulk Policy Migrator**.

1. On the **Manage new IAM actions** page, choose the **Rollback changes** tab.

1. Select any accounts to rollback. The accounts must have `Migrated` showing in the **Rollback status** column.

1. Choose **Rollback changes** button.

1. Remain on the console page until rollback is complete.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awsaccountbilling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
