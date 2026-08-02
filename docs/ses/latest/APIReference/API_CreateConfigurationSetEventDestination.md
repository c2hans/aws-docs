---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSetEventDestination.html
---

# CreateConfigurationSetEventDestination
<a name="API_CreateConfigurationSetEventDestination"></a>

Creates a configuration set event destination.

**Note**
When you create or update an event destination, you must provide one, and only one, destination. The destination can be CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).

An event destination is the AWS service to which Amazon SES publishes the email sending events associated with a configuration set. For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_CreateConfigurationSetEventDestination_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ConfigurationSetName **
The name of the configuration set that the event destination should be associated with.
Type: String
Required: Yes

 ** EventDestination **
An object that describes the AWS service that email sending event where information is published.
Type: [EventDestination](API_EventDestination.md) object
Required: Yes

## Errors
<a name="API_CreateConfigurationSetEventDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConfigurationSetDoesNotExist **
Indicates that the configuration set does not exist.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
HTTP Status Code: 400

 ** EventDestinationAlreadyExists **
Indicates that the event destination could not be created because of a naming conflict.
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

 ** LimitExceeded **
Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html).
HTTP Status Code: 400

## See Also
<a name="API_CreateConfigurationSetEventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/CreateConfigurationSetEventDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/CreateConfigurationSetEventDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/CreateConfigurationSetEventDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/CreateConfigurationSetEventDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/CreateConfigurationSetEventDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/CreateConfigurationSetEventDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/CreateConfigurationSetEventDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/CreateConfigurationSetEventDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/CreateConfigurationSetEventDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/CreateConfigurationSetEventDestination)
