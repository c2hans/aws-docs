---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/now-function.html
---

# Now
<a name="now-function"></a>

For database datasets that directly query the database, `now` returns the current date and time using the settings and format specified by the database server. For SPICE and Salesforce data sets, `now` returns the UTC date and time, in the format `yyyy-MM-ddTkk:mm:ss:SSSZ` (for example, 2015-10-15T19:11:51:003Z).

## Syntax
<a name="now-function-syntax"></a>

```
now()
```

## Return type
<a name="now-function-return-type"></a>

Date

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
