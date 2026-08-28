---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-default-roles.html
---

# Amazon RDS for Db2 default roles
<a name="db2-default-roles"></a>

RDS for Db2 adds the following six roles and grants them to the `master_user_role` with the `ADMIN` option. When the database is provisioned, RDS for Db2 grants `master_user_role` to the master user. The master user can in turn grant these roles to other users, groups, or roles with native `GRANT` statements by connecting to the database.
+ **DBA** – RDS for Db2 creates this empty role with `DATAACCESS` authorization. The master user can add more authorizations or privileges to this role, and then grant the role to other users, groups, or roles.
+ **DBA\_RESTRICTED** – RDS for Db2 creates this empty role. The master user can add privileges to this role, and then grant the role to other users, groups, or roles.
+ **DEVELOPER** – RDS for Db2 creates this empty role with `DATAACCESS` authorization. The master user can add more authorizations or privileges to this role, and then grant the role to other users, groups, or roles.
+ **ROLE\_NULLID\_PACKAGES** – RDS for Db2 grants `EXECUTE` privileges to this role on `ALL NULLID` packages that were bound by Db2 when `CREATE DATABASE` was run.
+ **ROLE\_PROCEDURES** – RDS for Db2 grants `EXECUTE` privileges to this role on all `SYSIBM` procedures.
+ **ROLE\_TABLESPACES** – RDS for Db2 grants `USAGE` privileges on tablespaces created by the `CREATE DATABASE` command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
