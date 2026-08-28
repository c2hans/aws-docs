---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/datatypes.html
---

# Data types
<a name="datatypes"></a>

The data for each column of your dataset are converted to one of the following data types:
+ **byte** – 1-byte signed integer numbers. The range of numbers is from -128 to 127.
+ **short** – 2-byte signed integer numbers. The range of numbers is from -32768 to 32767.
+ **integer** – 4-byte signed integer numbers. The range of numbers is from -2147483648 to 2147483647.
+ **long** – 8-byte signed integer numbers. The range of numbers is from -9223372036854775808 to 9223372036854775807.
+ **float** – 4-byte single-precision floating point numbers.
+ **double** – 8-byte double-precision floating point numbers.
+ **decimal** – Signed decimal numbers with up to 38 digits total and 18 digits after the decimal point.
+ **string** – Character string values.
+ **boolean** – Boolean type has one of two possible values: `true` and `false` or `yes` and `no`.
+ **timestamp** – Values comprising fields year, month, day, hour, minute, and second.
+ **date** – Values comprising fields year, month and day.

## Advanced data types
<a name="advanced-datatypes"></a>

*Advanced data types* are data types that DataBrew detects within a string column in a project, and therefore are not part of a dataset. For information about advanced data types, see [ Advanced data types](projects.adv-data-types.md#projects.adv-data-types.title).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
