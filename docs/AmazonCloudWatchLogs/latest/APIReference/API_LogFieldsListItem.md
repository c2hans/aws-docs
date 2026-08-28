---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogFieldsListItem.html
---

# LogFieldsListItem
<a name="API_LogFieldsListItem"></a>

Represents a log field with its name and data type information for a specific data source.

## Contents
<a name="API_LogFieldsListItem_Contents"></a>

 ** logFieldName **   <a name="CWL-Type-LogFieldsListItem-logFieldName"></a>
The name of the log field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** logFieldType **   <a name="CWL-Type-LogFieldsListItem-logFieldType"></a>
The data type information for the log field.
Type: [LogFieldType](API_LogFieldType.md) object
Required: No

## See Also
<a name="API_LogFieldsListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LogFieldsListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LogFieldsListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LogFieldsListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
