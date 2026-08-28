---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/global-view.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Manage large-scale migrations with global view
<a name="global-view"></a>

The AWS Transform MGN global view feature enables you to manage large-scale migrations across multiple accounts. Global view provides visibility, and the ability to perform actions on source servers, apps, and waves in different AWS accounts.

Global view uses AWS Organizations to structure a management account that has access to source servers in multiple member accounts, and member accounts that only have access to their own source servers.

To use this feature:
+ You need to have an AWS account in which AWS Transform MGN is initialized.
+ The account must be a management account in AWS Organizations, or a delegated admin for AWS Transform MGN which has the same feature permissions as a management account in AWS Organizations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
