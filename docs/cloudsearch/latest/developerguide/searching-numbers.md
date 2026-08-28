---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching-numbers.html
---

# Searching for Numbers in Amazon CloudSearch
<a name="searching-numbers"></a>

You can use structured queries to search any search enabled numeric field for a particular value or [range of values](searching-ranges.md). Amazon CloudSearch supports four numeric field types: `double`, `double-array`, `int`, and `int-array`. For more information, see [Configuring Index Fields](configuring-index-fields.md).

The basic syntax for searching a field for a single value is **FIELD**:**VALUE**. For example, `year:2010` searches the sample movie data for movies released in 2010.

You must use the structured query parser to use the field syntax. Note that numeric values are *not* enclosed in quotes—quotes designate a value as a string. To search for a range of values, use a comma (,) to separate the upper and lower bounds, and enclose the range using brackets or braces. For more information, see [Searching for a Range of Values](searching-ranges.md).

In a compound query, you use the `term` operator syntax to search for a single value: `(term field=year 2010)`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
