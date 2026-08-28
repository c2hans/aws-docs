---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-named-resource.html
---

# Cross-account data sharing using the named resource method
<a name="cross-account-named-resource"></a>

You can grant permissions to directly to principals in the another AWS account, or to external AWS accounts or AWS Organizations. Granting Lake Formation permissions to Organizations or organizational units is equivalent to granting the permission to every AWS account in that organization or organizational unit.

When you grant permissions to external accounts or organizations, you must include the **Grantable permissions** option. Only the data lake administrator in the external account can access the shared resources until the administrator grants permissions on the shared resources to other principals in the external account.

**Note**
**Grantable permissions** option is not supported when granting permissions directly to IAM principals from external accounts.

Follow instructions in [Granting database permissions using the named resource method](granting-database-permissions.md) to grant cross-account permissions using the named resource method.

 The following video demonstrates how to share data with an AWS organization using Lake Formation.

[![AWS Videos](http://img.youtube.com/vi/S-Mdcmq6oPM?controls=0&/0.jpg)](http://www.youtube.com/watch?v=S-Mdcmq6oPM?controls=0&)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
