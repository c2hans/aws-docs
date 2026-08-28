---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-nth-value.html
---

# NTH\_VALUE
<a name="sql-reference-nth-value"></a>

```
NTH_VALUE(x, n) [ <from first or last> ] [ <null treatment> ] over w
```

Where:

<null treatment> := RESPECT NULLS \| IGNORE NULL

<from first or last> := FROM FIRST \| FROM LAST

NTH\_VALUE returns the nth value of x from the first or last value in the window. Default is first. If <null treatment> is set to IGNORE NULLS, then function will skip over nulls while counting.

If there aren't enough rows in the window to reach nth value, the function returns NULL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
