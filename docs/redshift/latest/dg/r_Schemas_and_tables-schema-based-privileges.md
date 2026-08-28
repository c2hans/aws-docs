---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_Schemas_and_tables-schema-based-privileges.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Schema-based permissions
<a name="r_Schemas_and_tables-schema-based-privileges"></a>

 Schema-based permissions are determined by the owner of the schema:
+ By default, all users have CREATE and USAGE permissions on the PUBLIC schema of a database. To disallow users from creating objects in the PUBLIC schema of a database, use the [REVOKE](r_REVOKE.md) command to remove that permission.
+ Unless they are granted the USAGE permission by the object owner, users cannot access any objects in schemas they do not own.
+ If users have been granted the CREATE permission to a schema that was created by another user, those users can create objects in that schema.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
