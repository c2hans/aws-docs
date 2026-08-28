---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rdsadmin_transport_util_list_xtts_orphan_files.html
---

# Listing orphaned files after a tablespace import
<a name="rdsadmin_transport_util_list_xtts_orphan_files"></a>

Use the `rdsadmin.rdsadmin_transport_util.list_xtts_orphan_files` procedure to list data files that were orphaned after a tablespace import. After you identify the data files, you can delete them by calling `rdsadmin.rdsadmin_transport_util.cleanup_incomplete_xtts_import`.

## Syntax
<a name="rdsadmin_transport_util_list_xtts_orphan_files-syntax"></a>

```
FUNCTION list_xtts_orphan_files RETURN xtts_orphan_files_list_t PIPELINED;
```

## Examples
<a name="rdsadmin_transport_util_list_xtts_orphan_files-examples"></a>

The following example runs the procedure `rdsadmin.rdsadmin_transport_util.list_xtts_orphan_files`. The output shows two data files that are orphaned.

```
SQL> SELECT * FROM TABLE(rdsadmin.rdsadmin_transport_util.list_xtts_orphan_files);

FILENAME       FILESIZE
-------------- ---------
datafile_7.dbf 104865792
datafile_8.dbf 104865792
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
