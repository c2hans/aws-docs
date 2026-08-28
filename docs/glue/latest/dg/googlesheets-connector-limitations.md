---
source_url: https://docs.aws.amazon.com/glue/latest/dg/googlesheets-connector-limitations.html
---

# Limitations for Google Sheets connector
<a name="googlesheets-connector-limitations"></a>

The following are limitations for the Google Sheets connector:
+  Google Sheets connector does not support Filters. Hence, filter based partitioning cannot be supported.
+  In Record Base Partitioning, there is no provision to return exact record count by SAAS. As a result, there can be scenarios where files with empty records are created.
+  Since the Google Sheets connector does not support filter-based partitioning, `partitionField`, `lowerbound`, and `upperbound` are not valid connection options. If these options are provided, the AWS Glue job is expected to fail.
+  It is essential to designate the first row of the sheet as the header row to avoid data processing issues.
  +  If not provided, header row will be replaced with `Unnamed:1`, `Unnamed:2`, `Unnamed:3`... if the sheet contains data with the first row empty.
  +  If header row is provided, empty column names will be replaced with `Unnamed:<number of column>`. For example, if header row is `['ColumnName1', 'ColumnName2', '', '', 'ColumnName5', 'ColumnName6']`, then it will become `['ColumnName1', 'ColumnName2', 'Unnamed:3', 'Unnamed:4', 'ColumnName5', 'ColumnName6'].`
+  The Google Sheets connector does not support Incremental transfer.
+  Google Sheets connector supports only String datatype.
+  Duplicate headers in a sheet will be iteratively renamed with a numeric suffix. Header names provided by the user will have precedence while renaming the duplicate headers. For example, if the header row is ["Name", "", "Name", null, "Unnamed:6", ""], it will change to: ["Name", "Unnamed:2", "Name1", "Unnamed:4", "Unnamed:6", "Unnamed:61"].
+  Google Sheets connector does not support spaces for a tabName.
+  A folder name can't have the following special characters:
  + \#
  + /

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
