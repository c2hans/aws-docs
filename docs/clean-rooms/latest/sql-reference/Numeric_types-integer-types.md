---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Numeric_types-integer-types.html
---

# Integer types
<a name="Numeric_types-integer-types"></a>

Use the following data types to store whole numbers of various ranges. You can't store values outside of the allowed range for each type.

| Name  | Storage  | Range  |
| --- | --- | --- |
| SMALLINT | 2 bytes  | -32768 to \+32767  |
| SHORT  | 2 bytes  | -32768 to \+32767  |
| INTEGER or INT | 4 bytes  | -2147483648 to \+2147483647  |
| BIGINT | 8 bytes  | -9223372036854775808 to 9223372036854775807  |
| LONG  | 8 bytes  | -9223372036854775808 to 9223372036854775807  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
