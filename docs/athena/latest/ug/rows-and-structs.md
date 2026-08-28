---
source_url: https://docs.aws.amazon.com/athena/latest/ug/rows-and-structs.html
---

# Query arrays with complex types and nested structures
<a name="rows-and-structs"></a>

Your source data often contains arrays with complex data types and nested structures. Examples in this section show how to change element's data type, locate elements within arrays, and find keywords using Athena queries.

**Topics**
+ [Create a `ROW`](creating-row.md)
+ [Change field names in arrays using `CAST`](changing-row-arrays-with-cast.md)
+ [Filter arrays using the `.` notation](filtering-with-dot.md)
+ [Filter arrays with nested values](filtering-nested-with-dot.md)
+ [Filter arrays using `UNNEST`](filtering-with-unnest.md)
+ [Find keywords in arrays using `regexp_like`](filtering-with-regexp.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
