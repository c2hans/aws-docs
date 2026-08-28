---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_LastUpdate.html
---

# LastUpdate
<a name="API_query_LastUpdate"></a>

Configuration object that contains the most recent account settings update, visible only if settings have been updated previously.

## Contents
<a name="API_query_LastUpdate_Contents"></a>

 ** Status **   <a name="timestream-Type-query_LastUpdate-Status"></a>
The status of the last update. Can be either `PENDING`, `FAILED`, or `SUCCEEDED`.
Type: String
Valid Values: `PENDING | FAILED | SUCCEEDED`
Required: No

 ** StatusMessage **   <a name="timestream-Type-query_LastUpdate-StatusMessage"></a>
Error message describing the last account settings update status, visible only if an error occurred.
Type: String
Required: No

 ** TargetQueryTCU **   <a name="timestream-Type-query_LastUpdate-TargetQueryTCU"></a>
The number of TimeStream Compute Units (TCUs) requested in the last account settings update.
Type: Integer
Required: No

## See Also
<a name="API_query_LastUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/LastUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/LastUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/LastUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
