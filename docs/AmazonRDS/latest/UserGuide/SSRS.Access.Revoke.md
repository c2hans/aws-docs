---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSRS.Access.Revoke.html
---

# Revoking system-level permissions
<a name="SSRS.Access.Revoke"></a>

The `RDS_SSRS_ROLE` system role doesn't have sufficient permissions to delete system-level role assignments. To remove a user or user group from `RDS_SSRS_ROLE`, use the same stored procedure that you used to grant the role but use the `SSRS_REVOKE_PORTAL_PERMISSION` task type.

**To revoke access from a domain user for the SSRS web portal**
+ Use the following stored procedure.

  ```
  exec msdb.dbo.rds_msbi_task
  @task_type='SSRS_REVOKE_PORTAL_PERMISSION',
  @ssrs_group_or_username=N'{{AD_domain}}\{{user}}';
  ```

**To revoke access from a domain user for the PBIRS web portal (SQL Server 2025 and higher)**
+ Use the following stored procedure.

  ```
  exec msdb.dbo.rds_msbi_task
  @task_type='PBIRS_REVOKE_PORTAL_PERMISSION',
  @pbirs_group_or_username=N'{{AD_domain}}\{{user}}';
  ```

Doing this deletes the user from the `RDS_SSRS_ROLE` system role (for SSRS) or the equivalent PBIRS role. It also deletes the user from the `Content Manager` item-level role if the user has it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
