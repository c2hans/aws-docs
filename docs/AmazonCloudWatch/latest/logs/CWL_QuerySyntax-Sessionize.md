---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Sessionize.html
---

# sessionize
<a name="CWL_QuerySyntax-Sessionize"></a>

Use the `sessionize` command to group events into sessions by identity fields and an inactivity gap. The command emits a session identifier field.

**Syntax**

```
| sessionize {{field}}[, {{field}} ...] [maxspan {{duration}}] [AS {{out}}]
```

The command uses the following arguments:
+ `{{field}}` – One or more identity fields to group by.
+ `maxspan {{duration}}` (Optional) – The maximum inactivity gap before starting a new session. Default: `30m`.
+ `AS {{out}}` (Optional) – The output field name. Default: `session_id`.

**Example**
The following query groups events into sessions by user and device with a 1-hour inactivity gap.

```
fields @timestamp, userId, deviceId
| sessionize userId, deviceId maxspan 1h as my_session
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
