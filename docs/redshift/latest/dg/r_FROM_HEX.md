---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_FROM_HEX.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# FROM\_HEX function
<a name="r_FROM_HEX"></a>

FROM\_HEX converts a hexadecimal to a binary value.

## Syntax
<a name="r_FROM_HEX-synopsis"></a>

```
FROM_HEX(hex_string)
```

## Arguments
<a name="r_FROM_HEX-arguments"></a>

 *hex\_string*
Hexadecimal string of data type `VARCHAR` or `TEXT` to be converted. The format must be a literal value.

## Return type
<a name="r_FROM_HEX-return-type"></a>

`VARBYTE`

## Examples
<a name="r_FROM_HEX-examples"></a>

To convert the hexadecimal representation of `'6162'` to a binary value, use the following example. The result is automatically shown as the hexadecimal representation of the binary value.

```
SELECT FROM_HEX('6162');

+----------+
| from_hex |
+----------+
|     6162 |
+----------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
