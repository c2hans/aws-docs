---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RevokePrivileges.html
---

# Revoking SELECT or EXECUTE privileges on SYS objects
<a name="Appendix.Oracle.CommonDBATasks.RevokePrivileges"></a>

To revoke privileges on a single object, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.revoke_sys_object`. The procedure only revokes privileges that the master user has already been granted through a role or direct grant.

The `revoke_sys_object` procedure has the following parameters.

| Parameter name | Data type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `p_obj_name` | varchar2 | — | Yes | The name of the object to revoke privileges for. The object can be a directory, function, package, procedure, sequence, table, or view. Object names must be spelled exactly as they appear in `DBA_OBJECTS`. Most system objects are defined in uppercase, so we recommend that you try that first.  |
| `p_revokee` | varchar2 | — | Yes | The name of the user or role to revoke privileges from.  |
| `p_privilege` | varchar2 | null | Yes | The privilege to revoke. Valid values include `SELECT`, `EXECUTE`, and `ALL`. |

The following example revokes select privileges on an object named `V_$SESSION` from a user named `USER1`.

```
begin
    rdsadmin.rdsadmin_util.revoke_sys_object(
        p_obj_name  => '{{V_$SESSION}}',
        p_revokee   => '{{USER1}}',
        p_privilege => '{{SELECT}}');
end;
/
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
