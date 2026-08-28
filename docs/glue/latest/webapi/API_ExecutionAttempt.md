---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ExecutionAttempt.html
---

# ExecutionAttempt
<a name="API_ExecutionAttempt"></a>

A run attempt for a column statistics task run.

## Contents
<a name="API_ExecutionAttempt_Contents"></a>

 ** ColumnStatisticsTaskRunId **   <a name="Glue-Type-ExecutionAttempt-ColumnStatisticsTaskRunId"></a>
A task run ID for the last column statistics task run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ErrorMessage **   <a name="Glue-Type-ExecutionAttempt-ErrorMessage"></a>
An error message associated with the last column statistics task run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ExecutionTimestamp **   <a name="Glue-Type-ExecutionAttempt-ExecutionTimestamp"></a>
A timestamp when the last column statistics task run occurred.
Type: Timestamp
Required: No

 ** Status **   <a name="Glue-Type-ExecutionAttempt-Status"></a>
The status of the last column statistics task run.
Type: String
Valid Values: `FAILED | STARTED`
Required: No

## See Also
<a name="API_ExecutionAttempt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ExecutionAttempt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ExecutionAttempt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ExecutionAttempt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
