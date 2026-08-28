---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/struct_function.html
---

# STRUCT constructor function
<a name="struct_function"></a>

The STRUCT constructor function creates a struct with the given field values.

Constructor functions like STRUCT are useful when you need to create new data structures programmatically within your SQL queries. They allow you to build complex data structures, such as structs or records, that can be used in further data processing or analysis.

## Syntax
<a name="struct_function-syntax"></a>

```
struct(col1, col2, col3, ...)
```

## Arguments
<a name="struct_function-arguments"></a>

 *col1*
A column name or any valid expression.

## Returns
<a name="struct_function-returns"></a>

The STRUCT function returns a struct with *field1* matching the type of *expr1*.

If the arguments are named references, the names are used to name the field. Otherwise, the fields are named *colN*, where N is the position of the field in the struct.

## Examples
<a name="struct_function-examples"></a>

The following example creates a new struct with three fields: The first field is assigned the value 1. The second field is assigned the value 2. The third field is assigned the value 3. By default, the fields in the resulting struct are named `col1`, `col2`, and `col3`, based on their position in the argument list. The resulting struct is then returned as the output of the SQL statement.

```
SELECT struct(1, 2, 3);
 {"col1":1,"col2":2,"col3":3}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
