---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_PutConfigurationSetDeliveryOptions.html
---

# PutConfigurationSetDeliveryOptions
<a name="API_PutConfigurationSetDeliveryOptions"></a>

Adds or updates the delivery options for a configuration set.

## Request Parameters
<a name="API_PutConfigurationSetDeliveryOptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ConfigurationSetName **
The name of the configuration set.
Type: String
Required: Yes

 ** DeliveryOptions **
Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).
Type: [DeliveryOptions](API_DeliveryOptions.md) object
Required: No

## Errors
<a name="API_PutConfigurationSetDeliveryOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConfigurationSetDoesNotExist **
Indicates that the configuration set does not exist.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
HTTP Status Code: 400

 ** InvalidDeliveryOptions **
Indicates that provided delivery option is invalid.
HTTP Status Code: 400

## See Also
<a name="API_PutConfigurationSetDeliveryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/PutConfigurationSetDeliveryOptions)
