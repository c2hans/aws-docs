---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/periodToDateMaxOverTime-function.html
---

# periodToDateMaxOverTime
<a name="periodToDateMaxOverTime-function"></a>

The `periodToDateMaxOverTime` function calculates the maximum of a measure for a given time granularity (for instance, a quarter) up to a point in time.

## Syntax
<a name="periodToDateMaxOverTime-function-syntax"></a>

```
periodToDateMaxOverTime(
	measure,
	dateTime,
	period)
```

## Arguments
<a name="periodToDateMaxOverTime-function-arguments"></a>

 *measure*
An aggregated measure that you want to do the calculation

 *dateTime*
The date dimension over which you're computing PeriodOverTime calculations.

 *period*
(Optional) The time period across which you're computing the computation. Granularity of `YEAR` means `YearToDate` computation, `Quarter` means `QuarterToDate`, and so on. Valid granularities include `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, and `SECONDS`.
The default value is the visual's date dimension granularity.

## Example
<a name="periodToDateMaxOverTime-function-example"></a>

The following example calculates the maximum fare amount month over month.

```
periodToDatemaxOverTime(max({fare_amount}), pickupDatetime, MONTH)
```

![This is an image of the results of the example calculation with illustrations.](http://docs.aws.amazon.com/quick/latest/userguide/images/PTDMaxOverTimeResults.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
