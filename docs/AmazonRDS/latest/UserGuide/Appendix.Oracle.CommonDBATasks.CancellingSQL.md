---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.CancellingSQL.html
---

# Canceling a SQL statement in a session
<a name="Appendix.Oracle.CommonDBATasks.CancellingSQL"></a>

To cancel a SQL statement in a session, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.cancel`.

**Note**
This procedure is supported for Oracle Database 19c (19.0.0) and all higher major and minor versions of RDS for Oracle.

The `cancel` procedure has the following parameters.

| Parameter name | Data type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `sid` | number | — | Yes | The session identifier. |
| `serial` | number | — | Yes | The serial number of the session. |
| `sql_id` | varchar2 | null | No | The SQL identifier of the SQL statement.  |

The following example cancels a SQL statement in a session.

```
begin
    rdsadmin.rdsadmin_util.cancel(
        sid    => {{sid}},
        serial => {{serial_number}},
        sql_id => {{sql_id}});
end;
/
```

To get the session identifier, the session serial number, and the SQL identifier of a SQL statement, query the `V$SESSION` view. The following example gets all sessions and SQL identifiers for the user `AWSUSER`.

```
select SID, SERIAL#, SQL_ID, STATUS from V$SESSION where USERNAME = '{{AWSUSER}}';
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
