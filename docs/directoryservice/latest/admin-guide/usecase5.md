---
source_url: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/usecase5.html
---

# Use Case 5: Extend your on-premises Active Directory to the AWS Cloud
<a name="usecase5"></a>

If you already have an Active Directory infrastructure and want to use it when migrating Active Directory-aware workloads to the AWS Cloud, AWS Managed Microsoft AD can help. You can use [Active Directory trusts](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_test_lab_trust.html) to connect AWS Managed Microsoft AD to your existing Active Directory. This means your users can access Active Directory-aware and AWS applications with their on-premises Active Directory credentials, without needing you to synchronize users, groups, or passwords.

For example, your users can sign in to the AWS Management Console and Amazon WorkSpaces by using their existing Active Directory user names and passwords. Also, when you use Active Directory-aware applications such as SharePoint with AWS Managed Microsoft AD, your logged-in Windows users can access these applications without needing to enter credentials again.

You can also migrate your on-premises Active Directory domain to AWS to be free of the operational burden of your Active Directory infrastructure using the [Active Directory Migration Toolkit (ADMT)](https://aws.amazon.com/blogs/security/how-to-migrate-your-on-premises-domain-to-aws-managed-microsoft-ad-using-admt/) along with the Password Export Service (PES) to perform the migration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
