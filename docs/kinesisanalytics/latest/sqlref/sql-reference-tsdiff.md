---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-tsdiff.html
---

# TSDIFF
<a name="sql-reference-tsdiff"></a>

Returns NULL if any of the arguments is null.

 Otherwise returns the difference between the two timestamps in milliseconds.

## Syntax
<a name="sql-reference-tsdiff-syntax"></a>

```
TSDIFF(startTime, endTime)
```

## Parameters
<a name="sql-reference-tsdiff-parameters"></a>

*startTime*

A Unix timestamp in the format milliseconds since '1970-01-01 00:00:00' UTC, expressed as a BIGINT.

*endTime*

A Unix timestamp in the format milliseconds since '1970-01-01 00:00:00' UTC, expressed as a BIGINT.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
