---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-hash-functions.html
---

# Hashing functions
<a name="CWL_QuerySyntax-hash-functions"></a>

You can use hashing functions in `fields` and `filter` commands.

|  Function |  Result type |  Description |
| --- | --- | --- |
| `md5(fieldName: string)` | string | Computes the MD5 hash of the string value. |
| `sha256(fieldName: string)` | string | Computes the SHA-256 hash of the string value. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
