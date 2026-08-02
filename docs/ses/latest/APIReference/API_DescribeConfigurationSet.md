---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeConfigurationSet.html
---

# DescribeConfigurationSet
<a name="API_DescribeConfigurationSet"></a>

Returns the details of the specified configuration set. For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_DescribeConfigurationSet_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ConfigurationSetAttributeNames.member.N**
A list of configuration set attributes to return.
Type: Array of strings
Valid Values: `eventDestinations | trackingOptions | deliveryOptions | reputationOptions`
Required: No

 ** ConfigurationSetName **
The name of the configuration set to describe.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeConfigurationSet_ResponseElements"></a>

The following elements are returned by the service.

 ** ConfigurationSet **
The configuration set object associated with the specified configuration set.
Type: [ConfigurationSet](API_ConfigurationSet.md) object

 ** DeliveryOptions **
Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).
Type: [DeliveryOptions](API_DeliveryOptions.md) object

 **EventDestinations.member.N**
A list of event destinations associated with the configuration set.
Type: Array of [EventDestination](API_EventDestination.md) objects

 ** ReputationOptions **
An object that represents the reputation settings for the configuration set.
Type: [ReputationOptions](API_ReputationOptions.md) object

 ** TrackingOptions **
The name of the custom open and click tracking domain associated with the configuration set.
Type: [TrackingOptions](API_TrackingOptions.md) object

## Errors
<a name="API_DescribeConfigurationSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConfigurationSetDoesNotExist **
Indicates that the configuration set does not exist.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConfigurationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/DescribeConfigurationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/DescribeConfigurationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/DescribeConfigurationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/DescribeConfigurationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/DescribeConfigurationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/DescribeConfigurationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/DescribeConfigurationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/DescribeConfigurationSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/DescribeConfigurationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/DescribeConfigurationSet)
