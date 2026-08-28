---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_Users.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Users
<a name="r_Users"></a>

You can create and manage database users using the Amazon Redshift SQL commands CREATE USER and ALTER USER. Or you can configure your SQL client with custom Amazon Redshift JDBC or ODBC drivers. These manage the process of creating database users and temporary passwords as part of the database logon process.

The drivers authenticate database users based on AWS Identity and Access Management (IAM) authentication. If you already manage user identities outside of AWS, you can use a SAML 2.0-compliant identity provider (IdP) to manage access to Amazon Redshift resources. You use an IAM role to configure your IdP and AWS to permit your federated users to generate temporary database credentials and log on to Amazon Redshift databases. For more information, see [Using IAM authentication to generate database user credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-user-credentials.html).

Amazon Redshift users can only be created and dropped by a database superuser. Users are authenticated when they log on to Amazon Redshift. They can own databases and database objects (for example, tables). They can also grant permissions on those objects to users, groups, and schemas to control who has access to which object. Users with CREATE DATABASE rights can create databases and grant permissions to those databases. Superusers have database ownership permissions for all databases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
