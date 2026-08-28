---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_roles-database-privileges.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Database object permissions
<a name="r_roles-database-privileges"></a>

Apart from system permissions, Amazon Redshift includes database object permissions that define access options. These include such options as the ability to read data in tables and views, write data, create tables, and drop tables. For more information, see [GRANT](r_GRANT.md).

By using RBAC, you can assign database object permissions to roles, similarly to how you can with system permissions. Then you can assign roles to users, authorize users with system permissions, and authorize users with database permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
