---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.backup-control-file.html
---

# Backing up a control file
<a name="Appendix.Oracle.CommonDBATasks.backup-control-file"></a>

You can back up a control file using the Amazon RDS procedure `rdsadmin.rdsadmin_rman_util.backup_current_controlfile`.

This procedure uses the following common parameters for RMAN tasks:
+ `p_owner`
+ `p_directory_name`
+ `p_label`
+ `p_compress`
+ `p_rman_to_dbms_output`
+ `p_tag`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md).

This procedure is supported for the following Amazon RDS for Oracle DB engine versions:
+ Oracle Database 26ai (26.0.0)
+ Oracle Database 21c (21.0.0)
+ Oracle Database 19c (19.0.0)

The following example backs up a control file using the specified values for the parameters.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.backup_current_controlfile(
        p_owner               => '{{SYS}}',
        p_directory_name      => '{{MYDIRECTORY}}',
        p_tag                 => '{{CONTROL_FILE_BACKUP}}',
        p_rman_to_dbms_output => {{FALSE}});
END;
/
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
