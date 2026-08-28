---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena-invalid-data.html
---

# Invalid data when using Athena with Amazon Quick Sight
<a name="troubleshoot-athena-invalid-data"></a>

An invalid data error can occur when you use any operator or function in a calculated field. To address this, verify that the data in the table is consistent with the format that you supplied to the function.

For example, suppose that you are using the function `parseDate(expression, [‘format’], [‘time_zone’])` as **parseDate(date\_column, ‘MM/dd/yyyy’)**. In this case, all values in `date_column` must conform to `'MM/dd/yyyy'` format (`’05/12/2016’`). Any value that isn't in this format (**‘2016/12/05’**) can cause an error.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
