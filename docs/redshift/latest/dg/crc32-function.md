---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/crc32-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# CRC32 function
<a name="crc32-function"></a>

CRC32 is a function used for error detection. The function uses a CRC32 algorithm to detect changes between source and target data. The CRC32 function converts a variable-length string into an 8-character string that is a text representation of the hexadecimal value of a 32 bit-binary sequence. To detect changes between source and target data, use the CRC32 function on the source data and store the output. Then, use the CRC32 function on the target data and compare that output to the output from the source data. The outputs will be the same if the data was not modified, and the outputs will be different if the data was modified.

## Syntax
<a name="crc32-function-syntax"></a>

```
CRC32(string)
```

## Arguments
<a name="crc32-function-arguments"></a>

 *string*
A `CHAR` string, a `VARCHAR` string, or an expression that implicitly evaluates to a `CHAR` or `VARCHAR` type.

## Return type
<a name="crc32-function-return-type"></a>

The CRC32 function returns an 8-character string that is a text representation of the hexadecimal value of a 32-bit binary sequence. The Amazon Redshift CRC32 function is based on the CRC-32C polynomial.

## Examples
<a name="crc32-function-example"></a>

To show the 8-bit value for the string `Amazon Redshift`.

```
SELECT CRC32('Amazon Redshift');

+----------+
|  crc32   |
+----------+
| f2726906 |
+----------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
