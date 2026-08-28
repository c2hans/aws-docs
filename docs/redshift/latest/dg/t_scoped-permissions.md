---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/t_scoped-permissions.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Scoped permissions
<a name="t_scoped-permissions"></a>

Scoped permissions let you grant permissions to a user or role on all objects of a type within a database or schema. Users and roles with scoped permissions have the specified permissions on all current and future objects within the database or schema.

You can view the scope of database-level scoped permissions in [SVV\_DATABASE\_PRIVILEGES](r_SVV_DATABASE_PRIVILEGES.md). You can view the scope of schema-level scoped permissions in [SVV\_SCHEMA\_PRIVILEGES](r_SVV_SCHEMA_PRIVILEGES.md).

 For more information on applying scoped permissions, see [GRANT](r_GRANT.md) and [REVOKE](r_REVOKE.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
