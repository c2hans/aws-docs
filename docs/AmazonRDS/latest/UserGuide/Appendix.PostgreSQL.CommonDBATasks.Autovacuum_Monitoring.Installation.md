---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Installation.html
---

# Installing autovacuum monitoring and diagnostic tools in RDS for PostgreSQL
<a name="Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Installation"></a>

The `postgres_get_av_diag()` function is currently available in the following RDS for PostgreSQL versions:
+ 17.2 and higher 17 versions
+ 16.7 and higher 16 versions
+ 15.11 and higher 15 versions
+ 14.16 and higher 14 versions
+ 13.19 and higher 13 versions

 In order to use `postgres_get_av_diag()`, create the `rds_tools` extension.

```
postgres=> CREATE EXTENSION rds_tools ;
CREATE EXTENSION
```

Verify that the extension is installed.

```
postgres=> \dx rds_tools
             List of installed extensions
   Name    | Version |  Schema   |                    Description
 ----------+---------+-----------+----------------------------------------------------------
 rds_tools |   1.8   | rds_tools | miscellaneous administrative functions for RDS PostgreSQL
 1 row
```

Verify that the function is created.

```
postgres=> SELECT
    proname function_name,
    pronamespace::regnamespace function_schema,
    proowner::regrole function_owner
FROM
    pg_proc
WHERE
    proname = 'postgres_get_av_diag';
    function_name     | function_schema | function_owner
----------------------+-----------------+----------------
 postgres_get_av_diag | rds_tools       | rds_superuser
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
