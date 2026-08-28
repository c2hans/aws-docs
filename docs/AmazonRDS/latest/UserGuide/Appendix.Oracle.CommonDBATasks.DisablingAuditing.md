---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.DisablingAuditing.html
---

# Disabling auditing for the SYS.AUD$ table
<a name="Appendix.Oracle.CommonDBATasks.DisablingAuditing"></a>

To disable auditing on the database audit trail table `SYS.AUD$`, use the Amazon RDS procedure `rdsadmin.rdsadmin_master_util.noaudit_all_sys_aud_table`. This procedure takes no parameters.

The following query returns the current audit configuration for `SYS.AUD$` for a database:

```
SELECT * FROM DBA_OBJ_AUDIT_OPTS WHERE OWNER='SYS' AND OBJECT_NAME='AUD$';
```

The following command disables audit of `ALL` on `SYS.AUD$`.

```
EXEC rdsadmin.rdsadmin_master_util.noaudit_all_sys_aud_table;
```

For more information, see [NOAUDIT (traditional auditing)](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/NOAUDIT-Traditional-Auditing.html) in the Oracle documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
