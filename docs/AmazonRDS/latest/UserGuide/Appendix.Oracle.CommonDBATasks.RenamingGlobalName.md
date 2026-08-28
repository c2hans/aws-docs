---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RenamingGlobalName.html
---

# Changing the global name of a database
<a name="Appendix.Oracle.CommonDBATasks.RenamingGlobalName"></a>

To change the global name of a database, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.rename_global_name`. The `rename_global_name` procedure has the following parameters.

| Parameter name | Data type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `p_new_global_name` | varchar2 | — | Yes | The new global name for the database. |

The database must be open for the name change to occur. For more information about changing the global name of a database, see [ALTER DATABASE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ALTER-DATABASE.html) in the Oracle documentation.

The following example changes the global name of a database to `new_global_name`.

```
EXEC rdsadmin.rdsadmin_util.rename_global_name(p_new_global_name => '{{new_global_name}}');
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
