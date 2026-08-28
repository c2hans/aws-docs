---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Accum.html
---

# accum
<a name="CWL_QuerySyntax-Accum"></a>

Use the `accum` command to compute a running cumulative sum of a numeric field.

**Syntax**

```
| accum {{field}} [AS {{out}}]
```

The command uses the following arguments:
+ `{{field}}` – The numeric field to accumulate.
+ `AS {{out}}` (Optional) – An alias for the output field.

**Example**
The following query computes a running total of bytes.

```
fields @timestamp, bytes
| accum bytes AS totalBytes
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
