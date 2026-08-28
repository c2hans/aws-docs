---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-any.html
---

# ANY
<a name="sql-reference-any"></a>

```
ANY ( <boolean_expression> )
```

ANY returns true if the supplied boolean\_expression is true in any of the selected rows. Returns false if the supplied boolean\_expression is true in none of the selected rows.

**Example**
The following SQL snippet returns 'true' if the price for any ticker in the stream of trades is below 1. Returns 'false' if every price in the stream is 1 or greater.

```
 SELECT STREAM ANY (price < 1) FROM trades
  GROUP BY (FLOOR trades.rowtime to hour)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
