---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/FORMAT_STRING.html
---

# FORMAT\_STRING function
<a name="FORMAT_STRING"></a>

The FORMAT\_STRING function creates a formatted string by substituting placeholders in a template string with the provided arguments. It returns a formatted string from printf-style format strings.

The FORMAT\_STRING function works by replacing the placeholders in the template string with the corresponding values passed as arguments. This type of string formatting can be useful when you need to dynamically construct strings that include a mix of static text and dynamic data, such as when generating output messages, reports, or other types of informative text. The FORMAT\_STRING function provides a concise and readable way to create these types of formatted strings, making it easier to maintain and update the code that generates the output.

## Syntax
<a name="FORMAT_STRING-syntax"></a>

```
format_string(strfmt, obj, ...)
```

## Arguments
<a name="FORMAT_STRING-arguments"></a>

 *strfmt*
A STRING expression.

 *obj*
A STRING or numeric expression.

## Return type
<a name="FORMAT_STRING-returns"></a>

FORMAT\_STRING returns a STRING.

## Example
<a name="FORMAT_STRING-examples"></a>

The following example contains a template string that contains two placeholders: `%d` for a decimal (integer) value, and `%s` for a string value. The `%d` placeholder is replaced with the decimal (integer) value (`100`), and the %s placeholder is replaced with the string value (`"days"`). The output is a template string with the placeholders replaced by the provided arguments: `"Hello World 100 days"`.

```
SELECT format_string("Hello World %d %s", 100, "days");
 Hello World 100 days
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
