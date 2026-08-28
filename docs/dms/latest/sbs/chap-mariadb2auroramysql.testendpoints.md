---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-mariadb2auroramysql.testendpoints.html
---

# Test the endpoints for MariaDB database migration
<a name="chap-mariadb2auroramysql.testendpoints"></a>

1. On the navigation pane, choose **Endpoints**.

1. Choose the source endpoint name (`maria-on-prem`) and do the following:

   1. Choose **Test connections**.

   1. Choose the replication instance to test (`mariadb-mysql`).

   1. Choose **Run Test** and wait for the status to be **successful**.

1. On the navigation pane, choose **Endpoints**.

1. Choose the target endpoint name (`mysqltrg-rds`) and do the following:

   1. Choose **Test Connections**.

   1. Choose the replication instance to test (`mariadb-mysql`).

   1. Choose **Run Test** and wait for the status to be **successful**.

**Note**
If **Run Test** returns a status other than **successful**, the reason for the failure is displayed. Make sure that you resolve the issue before proceeding further.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
