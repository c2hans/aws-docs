---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/map_type.html
---

# MAP type
<a name="map_type"></a>

Use the MAP type to represent values comprising a set of key-value pairs.

```
map(keyType, valueType, valueContainsNull)
```

`keyType`: the data type of keys

`valueType`: the data type of values

Keys aren't allowed to have `null` values. Use `valueContainsNull` to indicate if values of a MAP type value can have `null` values.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
