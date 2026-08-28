---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-every.html
---

# EVERY
<a name="sql-reference-every"></a>

```
EVERY ( <boolean_expression> )
```

EVERY returns true if the supplied boolean\_expression is true in all of the selected rows. Returns false if the supplied boolean\_expression is false in any of the selected rows.

**Example**
The following SQL snippet returns 'true' if the price for every ticker in the stream of trades is below 1. Returns 'false' if any price is 1 or greater.

```
 SELECT STREAM EVERY (price < 1) FROM trades
  GROUP BY (FLOOR trades.rowtime to hour)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
