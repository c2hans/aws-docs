---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetpredefined.html
---

# Predefined permissions for AWS managed policies
<a name="permissionsetpredefined"></a>

You can create a predefined permission set with AWS managed policies.

When you create a permission set with predefined permissions, you choose one policy from a list of AWS managed policies. Within the available policies, you can choose from **Common permission policies** and **Job function policies**.

**Common permission policies**
Choose from a list of AWS managed policies that make it possible to access resources in your entire AWS account. You can add one of the following policies:
+ AdministratorAccess
+ PowerUserAccess
+ ReadOnlyAccess
+ ViewOnlyAccess

**Job function policies**
Choose from a list of AWS managed policies that make it possible to access resources in your AWS account that might be relevant to a job within your organization. You can add one of the following policies:
+ Billing
+ DataScientist
+ DatabaseAdministrator
+ NetworkAdministrator
+ SecurityAudit
+ SupportUser
+ SystemAdministrator

For detailed descriptions of the available common permission policies and job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *AWS Identity and Access Management user guide*.

For instructions on how to create a permission set, see [Create, manage, and delete permission sets](permissionsets.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
