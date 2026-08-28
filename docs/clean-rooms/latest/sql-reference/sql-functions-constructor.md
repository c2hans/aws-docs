---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-functions-constructor.html
---

# Constructor functions
<a name="sql-functions-constructor"></a>

A SQL constructor function is a function that is used to create new data structures, such as arrays or maps.

 They take some input values and return a new data structure object. Constructor functions are typically named after the data type they create, such as ARRAY or MAP.

Constructor functions are different from scalar functions or aggregate functions, which operate on existing data and return a single value. Constructor functions are used to create new data structures that can then be used in further data processing or analysis.

AWS Clean Rooms supports the following constructor functions:

**Topics**
+ [MAP constructor function](map_function.md)
+ [NAMED\_STRUCT constructor function](named-struct_function.md)
+ [STRUCT constructor function](struct_function.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
