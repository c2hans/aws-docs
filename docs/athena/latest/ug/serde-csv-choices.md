---
source_url: https://docs.aws.amazon.com/athena/latest/ug/serde-csv-choices.html
---

# CSV SerDe libraries
<a name="serde-csv-choices"></a>

When you create a table for CSV data in Athena, you can use either the Open CSV SerDe or the Lazy Simple SerDe library. To help you decide which to use, consider the following guidelines.
+ If your data contains values enclosed in double quotes (`"`), you can use the [Open CSV SerDe](https://cwiki.apache.org/confluence/display/Hive/CSV+Serde) library to deserialize the values in Athena. If your data does not contain values enclosed in double quotes (`"`), you can omit specifying any SerDe. In this case, Athena uses the default Lazy Simple SerDe. For information, see [Lazy Simple SerDe for CSV, TSV, and custom-delimited files](lazy-simple-serde.md).
+  If your data has UNIX numeric `TIMESTAMP` values (for example, `1579059880000`), use the Open CSV SerDe. If your data uses the `java.sql.Timestamp` format, use the Lazy Simple SerDe.

**Topics**
+ [Lazy Simple SerDe for CSV, TSV, and custom-delimited files](lazy-simple-serde.md)
+ [Open CSV SerDe for processing CSV](csv-serde.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
