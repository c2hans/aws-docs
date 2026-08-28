---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ConfigurationTemplateDeliveryConfigValues.html
---

# ConfigurationTemplateDeliveryConfigValues
<a name="API_ConfigurationTemplateDeliveryConfigValues"></a>

This structure contains the default values that are used for each configuration parameter when you use [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) to create a deliver under the current service type, resource type, and log type.

## Contents
<a name="API_ConfigurationTemplateDeliveryConfigValues_Contents"></a>

 ** fieldDelimiter **   <a name="CWL-Type-ConfigurationTemplateDeliveryConfigValues-fieldDelimiter"></a>
The default field delimiter that is used in a [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) operation when the field delimiter is not specified in that operation. The field delimiter is used only when the final output delivery is in `Plain`, `W3C`, or `Raw` format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5.
Required: No

 ** recordFields **   <a name="CWL-Type-ConfigurationTemplateDeliveryConfigValues-recordFields"></a>
The default record fields that will be delivered when a list of record fields is not provided in a [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) operation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 128 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** s3DeliveryConfiguration **   <a name="CWL-Type-ConfigurationTemplateDeliveryConfigValues-s3DeliveryConfiguration"></a>
The delivery parameters that are used when you create a delivery to a delivery destination that is an S3 Bucket.
Type: [S3DeliveryConfiguration](API_S3DeliveryConfiguration.md) object
Required: No

## See Also
<a name="API_ConfigurationTemplateDeliveryConfigValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ConfigurationTemplateDeliveryConfigValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ConfigurationTemplateDeliveryConfigValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ConfigurationTemplateDeliveryConfigValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
