---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Autoregress.html
---

# autoregress
<a name="CWL_QuerySyntax-Autoregress"></a>

Use the `autoregress` command to create lagged (previous-row) copies of a field's values. This is the lag/lead equivalent for CloudWatch Logs Insights.

**Syntax**

```
| autoregress {{field}} [AS {{alias}}] [p={{start}}[-{{end}}]]
```

The command uses the following arguments:
+ `{{field}}` – The field to create lag values for.
+ `AS {{alias}}` (Optional) – An alias for the output field.
+ `p={{N}}` (Optional) – Single lag depth (default 1). Use `p={{N}}-{{M}}` for a range of lags.

**Example**
The following query creates four lag fields (`bytes_p1` through `bytes_p4`).

```
fields @timestamp, bytes
| autoregress bytes p=1-4
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
