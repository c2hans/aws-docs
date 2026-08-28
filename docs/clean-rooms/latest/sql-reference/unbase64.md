---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/unbase64.html
---

# UNBASE64 function
<a name="unbase64"></a>

The UNBASE64 function converts an argument from a base 64 string to a binary.

Base64 encoding is commonly used to represent binary data (such as images, files, or encrypted information) in a textual format that is safe for transmission over various communication channels (such as email, URL parameters, or database storage).

The UNBASE64 function allows you to reverse this process and recover the original binary data. This type of functionality can be useful in scenarios where you need to work with data that has been encoded in Base64 format, such as when integrating with external systems or APIs that use Base64 as a data transfer mechanism.

## Syntax
<a name="bunase64-syntax"></a>

```
unbase64(expr)
```

## Arguments
<a name="unbase64-arguments"></a>

 *expr*
A STRING expression in a base64 format.

## Return type
<a name="unbase64-return-type"></a>

`BINARY`

## Example
<a name="unbase64-example"></a>

In the following example, the Base64-encoded string `'U3BhcmsgU1FM'` is converted back to the original string `'Spark SQL'`.

```
SELECT unbase64('U3BhcmsgU1FM');
 Spark SQL
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
