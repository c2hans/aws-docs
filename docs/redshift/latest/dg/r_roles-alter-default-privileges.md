---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_roles-alter-default-privileges.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ALTER DEFAULT PRIVILEGES for RBAC
<a name="r_roles-alter-default-privileges"></a>

Use the ALTER DEFAULT PRIVILEGES statement to define the default set of access permissions to be applied to objects that are created in the future by the specified user. By default, users can change only their own default access permissions. With RBAC, you can set the default access permissions for roles. For more information, see the [ALTER DEFAULT PRIVILEGES](r_ALTER_DEFAULT_PRIVILEGES.md) command.

RBAC enables you to assign database object permissions to roles, similarly to system permissions. Then you can assign roles to users, authorize users with system and/or database permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
