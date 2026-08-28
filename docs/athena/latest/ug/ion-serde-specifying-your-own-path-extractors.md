---
source_url: https://docs.aws.amazon.com/athena/latest/ug/ion-serde-specifying-your-own-path-extractors.html
---

# Specify your own path extractors
<a name="ion-serde-specifying-your-own-path-extractors"></a>

If your Amazon Ion fields do not map neatly to Hive columns, you can specify your own path extractors. In the `WITH SERDEPROPERTIES` clause of your `CREATE TABLE` statement, use the following syntax.

```
WITH SERDEPROPERTIES (
   "ion.path_extractor.case_sensitive" = "{{<Boolean>}}",
   "ion.{{<column_name>}}.path_extractor" = "{{<path_extractor_expression>}}"
)
```

**Note**
By default, path extractors are case insensitive. To override this setting, set the [ion.path_extractor.case_sensitive](ion-serde-using-ion-serde-properties.md#ioncase) SerDe property to `true`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
