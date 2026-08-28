---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_Nested-data-type.html
---

# Nested type
<a name="s_Nested-data-type"></a>

AWS Clean Rooms supports queries involving data with nested data types, specifically the AWS Glue STRUCT, ARRAY, and MAP column types. Only the custom analysis rule supports nested data types.

**Note**
Nested data types (ARRAY, MAP, and STRUCT) are not supported for Amazon Athena data sources. If a configured table that uses an Amazon Athena data source contains a nested-type column, queries fail during table setup. This occurs even when the query doesn't reference that column. To work around this limitation, exclude the nested-type columns from the view, or cast them to a supported type such as STRING.

Notably, nested data types don't conform to the rigid, tabular structure of the relational data model of SQL databases.

Nested data types contains tags that reference distinct entities within the data. They can contain complex values such as arrays, nested structures, and other complex structures that are associated with serialization formats, such as JSON. Nested data types support up to 1 MB of data for an individual nested data type field or object.

**Topics**
+ [ARRAY type](array_type.md)
+ [MAP type](map_type.md)
+ [STRUCT type](struct_type.md)
+ [Examples of nested data types](s_nested-data-type-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
