---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching-dates.html
---

# Searching for Dates and Times in Amazon CloudSearch
<a name="searching-dates"></a>

You can use structured queries to search any search enabled date field for a particular date and time or a [date-time range](searching-ranges.md). Amazon CloudSearch supports two date field types, `date` and `date-array`. For more information, see [Configuring Index Fields](configuring-index-fields.md).

 Dates and times are specified in UTC (Coordinated Universal Time) according to [IETF RFC3339](http://tools.ietf.org/html/rfc3339): `yyyy-mm-ddTHH:mm:ss.SSSZ`. In UTC, for example, 5:00 PM August 23, 1970 is: `1970-08-23T17:00:00Z`. Note that you can also specify fractional seconds when specifying times in UTC. For example, `1967-01-31T23:20:50.650Z.`

To search for a date (or time) in a `date` field, you must enclose the date string in single quotes. For example, both of the following queries search the movie data for all movies released at midnight on December 25, 2001:

```
q.parser=structured&q=release_date:'2001-12-25T00:00:00Z'
q.parser=structured&q=(term field%3Drelease_date '2001-12-25T00:00:00Z')
```

To search an entire day, see [Searching for a Date Range](searching-ranges.md#searching-ranges-dates).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
