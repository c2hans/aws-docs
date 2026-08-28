---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/struct_type.html
---

# STRUCT type
<a name="struct_type"></a>

Use the STRUCT type to represent values with the structure described by a sequence of StructFields (fields).

```
struct(name, dataType, nullable)
```

StructField(name, dataType, nullable): Represents a field in a StructType.

`dataType`: the data type a field

`name`: the name of a field

Use `nullable` to indicate if values of these fields can have `null` values.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
