---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.block-media-recovery.html
---

# Performing block media recovery
<a name="Appendix.Oracle.CommonDBATasks.block-media-recovery"></a>

You can recover individual data blocks, known as block media recovery, using the Amazon RDS procedures `rdsadmin.rdsadmin_rman_util.recover_datafile_block`. You can use this overloaded procedure to recover either an individual data block or a range of data blocks.

This procedure uses the following common parameter for RMAN tasks:
+ `p_rman_to_dbms_output`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md).

This procedure uses the following additional parameters.

| Parameter name | Data type | Valid values | Default | Required | Description |
| --- | --- | --- | --- | --- | --- |
| `p_datafile` | `NUMBER` | A valid data file ID number. | — | Yes | The data file containing the corrupt blocks. Specify the data file in either of the following ways:+  The data file ID number, which is located in `V$DATAFILE.FILE#` <br />+  The full data file name, including the path, located in `V$DATAFILE.NAME`  |
| `p_block` | `NUMBER` | A valid integer. | — | Yes | The number of an individual block to be recovered.<br />The following parameters are mutually exclusive:+  `p_block` <br />+  `p_from_block` and `p_to_block`  |
| `p_from_block` | `NUMBER` | A valid integer. | — | Yes | The first block number in a range of blocks to be recovered.<br />The following parameters are mutually exclusive:+  `p_block` <br />+  `p_from_block` and `p_to_block`  |
| `p_to_block` | `NUMBER` | A valid integer. | — | Yes | The last block number in a range of blocks to be recovered.<br />The following parameters are mutually exclusive:+  `p_block` <br />+  `p_from_block` and `p_to_block`  |

This procedure is supported for the following Amazon RDS for Oracle DB engine versions:
+ Oracle Database 26ai (26.0.0)
+ Oracle Database 21c (21.0.0)
+ Oracle Database 19c (19.0.0)

The following example recovers block 100 in data file 5.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.recover_datafile_block(
        p_datafile            => 5,
        p_block               => 100,
        p_rman_to_dbms_output => TRUE);
END;
/
```

The following example recovers blocks 100 to 150 in data file 5.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.recover_datafile_block(
        p_datafile            => 5,
        p_from_block          => 100,
        p_to_block            => 150,
        p_rman_to_dbms_output => TRUE);
END;
/
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
