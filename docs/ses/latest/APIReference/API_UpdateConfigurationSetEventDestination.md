---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetEventDestination.html
---

# UpdateConfigurationSetEventDestination
<a name="API_UpdateConfigurationSetEventDestination"></a>

Updates the event destination of a configuration set. Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see [Monitoring Your Amazon SES Sending Activity](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html) in the *Amazon SES Developer Guide.*

**Note**
When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_UpdateConfigurationSetEventDestination_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ConfigurationSetName **
The name of the configuration set that contains the event destination.
Type: String
Required: Yes

 ** EventDestination **
The event destination object.
Type: [EventDestination](API_EventDestination.md) object
Required: Yes

## Errors
<a name="API_UpdateConfigurationSetEventDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConfigurationSetDoesNotExist **
Indicates that the configuration set does not exist.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
HTTP Status Code: 400

 ** EventDestinationDoesNotExist **
Indicates that the event destination does not exist.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
 ** EventDestinationName **
Indicates that the event destination does not exist.
HTTP Status Code: 400

 ** InvalidCloudWatchDestination **
Indicates that the Amazon CloudWatch destination is invalid. See the error message for details.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
 ** EventDestinationName **
Indicates that the event destination does not exist.
HTTP Status Code: 400

 ** InvalidFirehoseDestination **
Indicates that the Amazon Kinesis Firehose destination is invalid. See the error message for details.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
 ** EventDestinationName **
Indicates that the event destination does not exist.
HTTP Status Code: 400

 ** InvalidSNSDestination **
Indicates that the Amazon Simple Notification Service (Amazon SNS) destination is invalid. See the error message for details.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
 ** EventDestinationName **
Indicates that the event destination does not exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConfigurationSetEventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/UpdateConfigurationSetEventDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/UpdateConfigurationSetEventDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/UpdateConfigurationSetEventDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/UpdateConfigurationSetEventDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/UpdateConfigurationSetEventDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/UpdateConfigurationSetEventDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/UpdateConfigurationSetEventDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/UpdateConfigurationSetEventDestination)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/UpdateConfigurationSetEventDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/UpdateConfigurationSetEventDestination)
