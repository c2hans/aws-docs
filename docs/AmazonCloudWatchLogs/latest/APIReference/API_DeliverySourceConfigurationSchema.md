---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeliverySourceConfigurationSchema.html
---

# DeliverySourceConfigurationSchema
<a name="API_DeliverySourceConfigurationSchema"></a>

A structure that describes a single configuration for a log type, including its name, value type, default value, and the range of supported values.

## Contents
<a name="API_DeliverySourceConfigurationSchema_Contents"></a>

 ** defaultValue **   <a name="CWL-Type-DeliverySourceConfigurationSchema-defaultValue"></a>
The default value of the configuration that is used when a value is not specified in a [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html) request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** keyName **   <a name="CWL-Type-DeliverySourceConfigurationSchema-keyName"></a>
The name of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** valueType **   <a name="CWL-Type-DeliverySourceConfigurationSchema-valueType"></a>
The data type of the configuration value. Valid values are `string`, `boolean`, `int`, `double`, and `long`.
Type: String
Valid Values: `string | boolean | int | double | long`
Required: Yes

 ** maxValue **   <a name="CWL-Type-DeliverySourceConfigurationSchema-maxValue"></a>
The maximum numeric value allowed for the configuration. This applies only when the `valueType` is a numeric type.
Type: Double
Required: No

 ** minValue **   <a name="CWL-Type-DeliverySourceConfigurationSchema-minValue"></a>
The minimum numeric value allowed for the configuration. This applies only when the `valueType` is a numeric type.
Type: Double
Required: No

 ** supportedValues **   <a name="CWL-Type-DeliverySourceConfigurationSchema-supportedValues"></a>
The list of allowed values for the configuration. Empty for free-form configuration.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_DeliverySourceConfigurationSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DeliverySourceConfigurationSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DeliverySourceConfigurationSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DeliverySourceConfigurationSchema)
