---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/base64.html
---

# BASE64 function
<a name="base64"></a>

The BASE64 function converts an expression to a base 64 string using [RFC2045 Base64 transfer encoding for MIME](https://datatracker.ietf.org/doc/html/rfc2045).

## Syntax
<a name="base64-syntax"></a>

```
base64(expr)
```

## Arguments
<a name="base64-arguments"></a>

 *expr*
A BINARY expression or a STRING which the function will interpret as BINARY.

## Return type
<a name="base64-return-type"></a>

`STRING`

## Example
<a name="base64-example"></a>

To convert the given string input into its Base64 encoded representation. use the following example. The result is the Base64 encoded representation of the input string 'Spark SQL', which is 'U3BhcmsgU1FM'.

```
SELECT base64('Spark SQL');
 U3BhcmsgU1FM
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
