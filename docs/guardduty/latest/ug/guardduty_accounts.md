---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html
---

# Multiple accounts in Amazon GuardDuty
<a name="guardduty_accounts"></a>

When your AWS environment has multiple accounts, you can manage them by designating one AWS account as the administrator account. You can then associate the multiple AWS accounts with this administrator account as its member accounts. With this configuration, a designated GuardDuty administrator account can assess and monitor the overall security of your organization. The administrator account can also perform account management tasks, such as reviewing all generated findings and configuring protection plans within GuardDuty.

In GuardDuty, an organization consists of a delegated GuardDuty administrator account and one or more associated member accounts. You can associate the accounts in two ways – by integrating with AWS Organizations, or by using a legacy method of sending and accepting membership invitations in the GuardDuty console. GuardDuty recommends that you integrate with AWS Organizations.

**Note**
The **Edit** button in the auto-enable section on the **Accounts** page redirects you to the [Configuring protection plans](protection-plans.md) page instead of opening the legacy configuration modal.

AWS Organizations is a global account management service that enables AWS administrators to consolidate and centrally manage multiple AWS accounts. It provides account management and consolidated billing features that are designed to support budgetary, security, and compliance needs. It’s offered at no additional charge and it integrates with multiple AWS services, including Macie, AWS Security Hub CSPM, and Amazon GuardDuty. For more information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

**Topics**
+ [Understanding the relationship between GuardDuty administrator account and member accounts](administrator_member_relationships.md)
+ [Managing GuardDuty accounts with AWS Organizations](guardduty_organizations.md)
+ [Managing GuardDuty accounts by invitation](guardduty_invitations.md)
+ [GuardDuty considerations for exporting member account details in CSV format](exporting-guardduty-accounts-data-to-csv.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
