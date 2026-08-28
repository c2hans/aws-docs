---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FieldsData.html
---

# FieldsData
<a name="API_FieldsData"></a>

A structure containing the extracted fields from a log event. These fields are extracted based on the log format and can be used for structured querying and analysis.

## Contents
<a name="API_FieldsData_Contents"></a>

 ** data **   <a name="CWL-Type-FieldsData-data"></a>
The actual log data content returned in the streaming response. This contains the fields and values of the log event in a structured format that can be parsed and processed by the client.
Type: Base64-encoded binary data object
Required: No

## See Also
<a name="API_FieldsData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/FieldsData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/FieldsData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/FieldsData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
