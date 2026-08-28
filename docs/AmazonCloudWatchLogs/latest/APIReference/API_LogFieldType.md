---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogFieldType.html
---

# LogFieldType
<a name="API_LogFieldType"></a>

Defines the data type structure for a log field, including the type, element information, and nested fields for complex types.

## Contents
<a name="API_LogFieldType_Contents"></a>

 ** element **   <a name="CWL-Type-LogFieldType-element"></a>
For array or collection types, specifies the element type information.
Type: [LogFieldType](#API_LogFieldType) object
Required: No

 ** fields **   <a name="CWL-Type-LogFieldType-fields"></a>
For complex types, contains the nested field definitions.
Type: Array of [LogFieldsListItem](API_LogFieldsListItem.md) objects
Required: No

 ** type **   <a name="CWL-Type-LogFieldType-type"></a>
The data type of the log field.
Type: String
Required: No

## See Also
<a name="API_LogFieldType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LogFieldType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LogFieldType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LogFieldType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
