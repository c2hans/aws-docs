---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_DATE_PART_YEAR.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# DATE\_PART\_YEAR function
<a name="r_DATE_PART_YEAR"></a>

The DATE\_PART\_YEAR function extracts the year from a date.

## Syntax
<a name="r_DATE_PART_YEAR-synopsis"></a>

```
DATE_PART_YEAR(date)
```

## Argument
<a name="r_DATE_PART_YEAR-argument"></a>

 *date*
A column of data type `DATE` or an expression that implicitly evaluates to a `DATE` type.

## Return type
<a name="r_DATE_PART_YEAR-return-type"></a>

INTEGER

## Examples
<a name="r_DATE_PART_YEAR-examples"></a>

The following example finds the year from a date literal.

```
SELECT DATE_PART_YEAR(date '20220502 04:05:06.789');

date_part_year
---------------
2022
```

The following example extracts the year from the CALDATE column. The values in the CALDATE column are dates. For more information about the data used in this example, see [Sample database](c_sampledb.md).

```
select caldate, date_part_year(caldate)
from date
order by
dateid limit 10;

 caldate   | date_part_year
-----------+----------------
2008-01-01 |           2008
2008-01-02 |           2008
2008-01-03 |           2008
2008-01-04 |           2008
2008-01-05 |           2008
2008-01-06 |           2008
2008-01-07 |           2008
2008-01-08 |           2008
2008-01-09 |           2008
2008-01-10 |           2008
(10 rows)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
