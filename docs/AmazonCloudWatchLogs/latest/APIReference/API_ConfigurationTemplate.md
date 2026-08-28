---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ConfigurationTemplate.html
---

# ConfigurationTemplate
<a name="API_ConfigurationTemplate"></a>

A structure containing information about the deafult settings and available settings that you can use to configure a [delivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Delivery.html) or a [delivery destination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeliveryDestination.html).

## Contents
<a name="API_ConfigurationTemplate_Contents"></a>

 ** allowedActionForAllowVendedLogsDeliveryForResource **   <a name="CWL-Type-ConfigurationTemplate-allowedActionForAllowVendedLogsDeliveryForResource"></a>
The action permissions that a caller needs to have to be able to successfully create a delivery source on the desired resource type when calling [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html).
Type: String
Required: No

 ** allowedFieldDelimiters **   <a name="CWL-Type-ConfigurationTemplate-allowedFieldDelimiters"></a>
The valid values that a caller can use as field delimiters when calling [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) or [UpdateDeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html) on a delivery that delivers in `Plain`, `W3C`, or `Raw` format.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 5.
Required: No

 ** allowedFields **   <a name="CWL-Type-ConfigurationTemplate-allowedFields"></a>
The allowed fields that a caller can use in the `recordFields` parameter of a [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) or [UpdateDeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html) operation.
Type: Array of [RecordField](API_RecordField.md) objects
Required: No

 ** allowedOutputFormats **   <a name="CWL-Type-ConfigurationTemplate-allowedOutputFormats"></a>
The list of delivery destination output formats that are supported by this log source.
Type: Array of strings
Valid Values: `json | plain | w3c | raw | parquet`
Required: No

 ** allowedSuffixPathFields **   <a name="CWL-Type-ConfigurationTemplate-allowedSuffixPathFields"></a>
The list of variable fields that can be used in the suffix path of a delivery that delivers to an S3 bucket.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 128 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** defaultDeliveryConfigValues **   <a name="CWL-Type-ConfigurationTemplate-defaultDeliveryConfigValues"></a>
A mapping that displays the default value of each property within a delivery's configuration, if it is not specified in the request.
Type: [ConfigurationTemplateDeliveryConfigValues](API_ConfigurationTemplateDeliveryConfigValues.md) object
Required: No

 ** deliveryDestinationType **   <a name="CWL-Type-ConfigurationTemplate-deliveryDestinationType"></a>
A string specifying which destination type this configuration template applies to.
Type: String
Valid Values: `S3 | CWL | FH | XRAY`
Required: No

 ** deliverySourceConfiguration **   <a name="CWL-Type-ConfigurationTemplate-deliverySourceConfiguration"></a>
The schema of the delivery source configuration that is available for this log type. Each element describes a configuration that can be set when calling [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html), including the configuration name, type, and default value.
Type: Array of [DeliverySourceConfigurationSchema](API_DeliverySourceConfigurationSchema.md) objects
Required: No

 ** logType **   <a name="CWL-Type-ConfigurationTemplate-logType"></a>
A string specifying which log type this configuration template applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w]*`
Required: No

 ** resourceType **   <a name="CWL-Type-ConfigurationTemplate-resourceType"></a>
A string specifying which resource type this configuration template applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-_]*`
Required: No

 ** s3TablesIntegration **   <a name="CWL-Type-ConfigurationTemplate-s3TablesIntegration"></a>
The S3 Tables integration configuration for this configuration template, including the datasource name and type.
Type: [S3TablesIntegration](API_S3TablesIntegration.md) object
Required: No

 ** service **   <a name="CWL-Type-ConfigurationTemplate-service"></a>
A string specifying which service this configuration template applies to. For more information about supported services see [Enable logging from AWS services.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w_-]*`
Required: No

## See Also
<a name="API_ConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ConfigurationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
