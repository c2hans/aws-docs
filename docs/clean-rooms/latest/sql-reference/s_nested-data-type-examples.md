---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_nested-data-type-examples.html
---

# Examples of nested data types
<a name="s_nested-data-type-examples"></a>

For the `struct<given:varchar, family:varchar>` type, there are two attribute names: `given`, and `family`, each corresponding to a `varchar` value.

For the `array<varchar>` type, the array is specified as a list of `varchar`.

The `array<struct<shipdate:timestamp, price:double>>` type refers to a list of elements with `struct<shipdate:timestamp, price:double>` type.

The `map` data type behaves like an `array` of `structs`, where the attribute name for each element in the array is denoted by `key` and it maps to a `value`.

**Example**
For example, the `map<varchar(20), varchar(20)>` type is treated as `array<struct<key:varchar(20), value:varchar(20)>>`, where `key` and `value` refer to the attributes of the map in the underlying data.
For information about how AWS Clean Rooms enables navigation into arrays and structures, see [Navigation](query-nested-data.md#navigation).
For information about how AWS Clean Rooms enables iteration over arrays by navigating the array using the FROM clause of a query, see [Unnesting queries](query-nested-data.md#unnesting-queries).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
