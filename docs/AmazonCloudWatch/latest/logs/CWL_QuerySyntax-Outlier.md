---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Outlier.html
---

# outlier
<a name="CWL_QuerySyntax-Outlier"></a>

Use the `outlier` command to detect statistical outliers in numeric fields based on the interquartile range (IQR). You can remove or clamp outlier rows.

**Syntax**

```
| outlier [action=remove|transform] [param={{n}}] [uselower=true|false] [mark=true|false] {{field}} [{{field}} ...]
```

The command uses the following arguments:
+ `action` (Optional) – Either `remove` (drops outlier rows) or `transform` (clamps to boundary). Default: `transform`.
+ `param` (Optional) – The IQR multiplier. Default: `2.5`.
+ `uselower` (Optional) – Whether to detect lower-bound outliers. Default: `false`.
+ `mark` (Optional) – Whether to add a boolean marker field. Default: `false`.
+ `{{field}}` – One or more numeric fields to check for outliers.

**Example**
The following query removes rows where cpu or memory are outliers, using a 3.0 IQR multiplier with lower-bound detection and marking.

```
fields @timestamp, cpu, memory
| outlier action=remove param=3.0 uselower=true mark=true cpu memory
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
