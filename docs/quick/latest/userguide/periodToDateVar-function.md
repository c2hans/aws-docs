---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/periodToDateVar-function.html
---

# periodToDateVar
<a name="periodToDateVar-function"></a>

The `periodToDateVar` function calculates the sample variance of the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time in that period.

## Syntax
<a name="periodToDateVar-function-syntax"></a>

```
periodToDateVar(
	measure,
	dateTime,
	period,
	endDate (optional))
```

## Arguments
<a name="periodToDateVar-function-arguments"></a>

 *measure*
The argument must be a field. Null values are omitted from the results. Literal values don't work.

 *dateTime*
The Date dimension over which you're computing PeriodToDate aggregations.

 *period*
The time period across which you're computing the computation. Granularity of `YEAR` means `YearToDate` computation, `Quarter` means `QuarterToDate`, and so on. Valid granularities include `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, and `SECONDS`.

 *endDate*
(Optional) The date dimension that you're ending computing periodToDate aggregations. It defaults to `now()` if omitted.

## Example
<a name="periodToDateVar-function-example"></a>

The following example calculates the week-to-date minimum fare amount per payment type, for the week of 06-30-21. For simplicity in the example, we filtered out only a single payment. 06-30-21 is Wednesday. Quick begins the week on Sundays. In our example, that is 06-27-21.

```
periodToDateVar(fare_amount, pickUpDatetime, WEEK, parseDate("06-30-2021", "MM-dd-yyyy"))
```

![This is an image of the results from the example calculation.](http://docs.aws.amazon.com/quick/latest/userguide/images/PTDVarResults.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
