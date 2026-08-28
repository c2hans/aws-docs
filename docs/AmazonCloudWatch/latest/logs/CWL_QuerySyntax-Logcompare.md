---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Logcompare.html
---

# logcompare
<a name="CWL_QuerySyntax-Logcompare"></a>

Use the `logcompare` command to compare the current time window against a baseline window shifted back by a specified duration.

**Syntax**

```
| logcompare timeshift {{duration}}
```

The command uses the following arguments:
+ `timeshift {{duration}}` – The duration to shift back for the baseline window (for example, `7d`).

**Example**
The following query compares the past day's logs against the same period one week earlier.

```
SOURCE lg start=-1d end=now
| logcompare timeshift 7d
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
