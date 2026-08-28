---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-domain-trusts.html
---

# Configuring WorkSpaces Applications to Use Domain Trusts
<a name="active-directory-domain-trusts"></a>

WorkSpaces Applications supports Active Directory domain environments where network resources such as file servers, applications, and computer objects reside in one domain, and the user objects reside in another. The domain service account used for computer object operations does not need to be in the same domain as the WorkSpaces Applications computer objects.

When creating the directory configuration, specify a service account that has the appropriate permissions to manage computer objects in the Active Directory domain where the file servers, applications, computer objects and other network resources reside.

Your end user Active Directory accounts must have the "Allowed to Authenticate" permissions for the following:
+ WorkSpaces Applications computer objects
+ Domain controllers for the domain

For more information, see [Granting Permissions to Create and Manage Active Directory Computer Objects](active-directory-permissions.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
