---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/cron-expression-reference.html
---

# Cron expression reference
<a name="cron-expression-reference"></a>

This solution uses a subset of the standard 5-field Linux cron format for recurring test schedules. The cron expression consists of five fields separated by spaces.

```
┌───────── minute (0-59)
│ ┌─────── hour (0-23, *, */N, or comma list)
│ │ ┌───── day of month (1-31 or *)
│ │ │ ┌─── month (1-12 or *)
│ │ │ │ ┌─ day of week (0-6, *, range, or list)
│ │ │ │ │
0 9 * * 1-5
```

## Accepted values
<a name="cron-accepted-values"></a>

The following table describes what each field accepts.

| Field | Accepted values | Examples |
| --- | --- | --- |
| Minute | A single value from 0 to 59. |  `0`, `30`, `45`  |
| Hour |  ` ` (every hour), a step value ``, a single value from 0 to 23, or a comma-separated list of values. |  ` `, ``, `9`, `9,17`  |
| Day of month |  `*` (every day) or a single value from 1 to 31. |  `*`, `1`, `15`, `31`  |
| Month |  `*` (every month) or a single value from 1 to 12. |  `*`, `1`, `6`, `12`  |
| Day of week |  `*` (every day), a single value from 0 to 6, a range using a hyphen, or a comma-separated list. |  `*`, `0`, `1-5`, `0,6`  |

Day of week values use the following mapping: 0 = Sunday, 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday.

## Unsupported patterns
<a name="cron-unsupported-patterns"></a>

The following patterns are valid Linux cron syntax but are not supported by this solution.

| Pattern | Example | Reason |
| --- | --- | --- |
| Minute step values |  `*/15 * * * *`  | The minimum scheduling interval is one hour. |
| Minute lists |  `0,30 * * * *`  | The minimum scheduling interval is one hour. |
| Day of month ranges |  `0 9 1-15 * *`  | Only a single day value or wildcard is accepted. |
| Day of month lists |  `0 9 1,15 * *`  | Only a single day value or wildcard is accepted. |
| Month ranges |  `0 9 * 3-9 *`  | Only a single month value or wildcard is accepted. |
| Month lists |  `0 9 1 1,6,12 *`  | Only a single month value or wildcard is accepted. |
| Question mark |  `0 9 ? * ?`  | The question mark character is not valid in standard Linux cron. Use `*` instead. |

## Preset patterns
<a name="cron-preset-patterns"></a>

The web console provides the following preset patterns that you can select directly.

| Pattern name | Expression | Description |
| --- | --- | --- |
| Every hour |  `0 * * * *`  | Runs at minute 0 of every hour. |
| Daily at 9:00 AM |  `0 9 * * *`  | Runs once daily at 9:00 AM in the selected timezone. |
| Weekdays at 8:00 AM |  `0 8 * * 1-5`  | Runs Monday through Friday at 8:00 AM. |
| Every Sunday at 5 PM |  `0 17 * * 0`  | Runs every Sunday at 5:00 PM. |
| 1st of month at 11 AM |  `0 11 1 * *`  | Runs on the first day of every month at 11:00 AM. |

## Scheduling constraints
<a name="cron-scheduling-constraints"></a>
+ The minimum interval between scheduled test runs is one hour. The system validates that the interval between consecutive runs is longer than the estimated test duration.
+ An expiry date is required for all recurring schedules. Tests will not run after the end of the expiry date (UTC).
+ The schedule timezone determines when the cron fires. Daylight Saving Time transitions are handled automatically. If a scheduled time does not exist due to a DST spring-forward transition, that occurrence is skipped.
+ The system validates the cron expression on both the web console and the API. If the expression does not match the accepted format, the test cannot be created.
