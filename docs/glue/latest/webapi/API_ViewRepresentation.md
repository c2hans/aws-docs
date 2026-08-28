---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ViewRepresentation.html
---

# ViewRepresentation
<a name="API_ViewRepresentation"></a>

A structure that contains the dialect of the view, and the query that defines the view.

## Contents
<a name="API_ViewRepresentation_Contents"></a>

 ** Dialect **   <a name="Glue-Type-ViewRepresentation-Dialect"></a>
The dialect of the query engine.
Type: String
Valid Values: `REDSHIFT | ATHENA | SPARK`
Required: No

 ** DialectVersion **   <a name="Glue-Type-ViewRepresentation-DialectVersion"></a>
The version of the dialect of the query engine. For example, 3.0.0.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** IsStale **   <a name="Glue-Type-ViewRepresentation-IsStale"></a>
Dialects marked as stale are no longer valid and must be updated before they can be queried in their respective query engines.
Type: Boolean
Required: No

 ** ValidationConnection **   <a name="Glue-Type-ViewRepresentation-ValidationConnection"></a>
The name of the connection to be used to validate the specific representation of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ViewExpandedText **   <a name="Glue-Type-ViewRepresentation-ViewExpandedText"></a>
The expanded SQL for the view. This SQL is used by engines while processing a query on a view. Engines may perform operations during view creation to transform `ViewOriginalText` to `ViewExpandedText`. For example:
+ Fully qualified identifiers: `SELECT * from table1 -> SELECT * from db1.table1`
Type: String
Length Constraints: Maximum length of 409600.
Required: No

 ** ViewOriginalText **   <a name="Glue-Type-ViewRepresentation-ViewOriginalText"></a>
The `SELECT` query provided by the customer during `CREATE VIEW DDL`. This SQL is not used during a query on a view (`ViewExpandedText` is used instead). `ViewOriginalText` is used for cases like `SHOW CREATE VIEW` where users want to see the original DDL command that created the view.
Type: String
Length Constraints: Maximum length of 409600.
Required: No

## See Also
<a name="API_ViewRepresentation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ViewRepresentation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ViewRepresentation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ViewRepresentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
