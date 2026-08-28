---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-extract.html
---

# EXTRACT
<a name="sql-reference-extract"></a>

```
EXTRACT(YEAR|MONTH|DAY|HOUR|MINUTE|SECOND FROM <datetime expression>|<interval expression>)
```

The EXTRACT function extracts one field from a DATE, TIME, TIMESTAMP or INTERVAL expression. Returns BIGINT for all fields other than SECOND. For SECOND it returns DECIMAL(5,3) and includes milliseconds.

## Syntax
<a name="sql-reference-extract-syntax"></a>

### Examples
<a name="sql-reference-extract-examples"></a>

| Function | Result |
| --- | --- |
|  <pre>EXTRACT(DAY FROM INTERVAL '2 3:4:5.678' DAY TO SECOND)</pre>  | 2 |
|  <pre>EXTRACT(HOUR FROM INTERVAL '2 3:4:5.678' DAY TO SECOND)</pre>  | 3 |
|  <pre>EXTRACT(MINUTE FROM INTERVAL '2 3:4:5.678' DAY TO SECOND)</pre>  | 4 |
|  <pre>EXTRACT(SECOND FROM INTERVAL '2 3:4:5.678' DAY TO SECOND)</pre>  | 5.678 |
|  <pre>EXTRACT(MINUTE FROM CURRENT_ROW_TIMESTAMP)<br />where CURRENT_ROW_TIMESTAMP is 2016-09-23 04:29:26.234</pre>  | 29 |
| <pre>EXTRACT (HOUR FROM CURRENT_ROW_TIMESTAMP)</pre>where CURRENT\_ROW\_TIMESTAMP is 2016-09-23 04:29:26.234 | 4 |

### Use in Function
<a name="sql-ref-extract-use"></a>

EXTRACT can be used for conditioning data, as in the following function which returns a 30 minute floor when [CURRENT\_ROW\_TIMESTAMP](sql-reference-current-row-timestamp.md) is input for p\_time.

```
CREATE or replace FUNCTION FLOOR30MIN( p_time TIMESTAMP )
RETURNS  TIMESTAMP
CONTAINS SQL
RETURNS NULL ON NULL INPUT
RETURN  floor(p_time to HOUR) + (( EXTRACT (  MINUTE FROM p_time  ) / 30)* INTERVAL '30' MINUTE ) ;
```

You would implement this function using code along the following lines:

```
SELECT stream FLOOR30MIN( CURRENT_ROW_TIMESTAMP ) as ROWTIME , * from "MyStream" ) over (range current row ) as r
```

**Note**
The code above assumes that you have previously created a stream called "MyStream."

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
