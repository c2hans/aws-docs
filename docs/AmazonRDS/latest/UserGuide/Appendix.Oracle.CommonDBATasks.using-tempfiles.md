---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.using-tempfiles.html
---

# Working with tempfiles in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.using-tempfiles"></a>

## Adding a tempfile to the instance store on a read replica
<a name="Appendix.Oracle.CommonDBATasks.adding-tempfile-replica"></a>

When you create a temporary tablespace on a primary DB instance, the read replica doesn't create tempfiles. Assume that an empty temporary tablespace exists on your read replica for either of the following reasons:
+ You dropped a tempfile from the tablespace on your read replica. For more information, see [Dropping tempfiles on a read replica](Appendix.Oracle.CommonDBATasks.dropping-tempfiles-replica.md).
+ You created a new temporary tablespace on the primary DB instance. In this case, RDS for Oracle synchronizes the metadata to the read replica.

You can add a tempfile to the empty temporary tablespace, and store the tempfile in the instance store. To create a tempfile in the instance store, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.add_inst_store_tempfile`. You can use this procedure only on a read replica. The procedure has the following parameters.

| Parameter name | Data type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `p_tablespace_name` | varchar | — | Yes | The name of the temporary tablespace on your read replica. |

In the following example, the empty temporary tablespace {{temp01}} exists on your read replica. Run the following command to create a tempfile for this tablespace, and store it in the instance store.

```
EXEC rdsadmin.rdsadmin_util.add_inst_store_tempfile(p_tablespace_name => '{{temp01}}');
```

For more information, see [Storing temporary data in an RDS for Oracle instance store](CHAP_Oracle.advanced-features.instance-store.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
