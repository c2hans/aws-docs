---
source_url: https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-grokLog-home.html
---

# Using the grokLog format in AWS Glue
<a name="aws-glue-programming-etl-format-grokLog-home"></a>

AWS Glue retrieves data from sources and writes data to targets stored and transported in various data formats. If your data is stored or transported in a loosely structured plaintext format, this document introduces you available features for using your data in AWS Glue through Grok patterns.

AWS Glue supports using Grok patterns. Grok patterns are similar to regular expression capture groups. They recognize patterns of character sequences in a plaintext file and give them a type and purpose. In AWS Glue, their primary purpose is to read logs. For an introduction to the Grok by the authors, see [Logstash Reference: Grok filter plugin](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html).

| Read | Write | Streaming read | Group small files | Job bookmarks |
| --- | --- | --- | --- | --- |
| Supported | Not Applicable | Supported | Supported | Unsupported |

## grokLog configuration reference
<a name="aws-glue-programming-etl-format-groklog-reference"></a>

You can use the following `format_options` values with `format="grokLog"`:
+ `logFormat` — Specifies the Grok pattern that matches the log's format.
+ `customPatterns` — Specifies additional Grok patterns used here.
+ `MISSING` — Specifies the signal to use in identifying missing values. The default is `'-'`.
+ `LineCount` — Specifies the number of lines in each log record. The default is `'1'`, and currently only single-line records are supported.
+ `StrictMode` — A Boolean value that specifies whether strict mode is turned on. In strict mode, the reader doesn't do automatic type conversion or recovery. The default value is `"false"`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
