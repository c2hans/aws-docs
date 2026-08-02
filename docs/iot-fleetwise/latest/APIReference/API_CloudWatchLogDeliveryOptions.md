---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CloudWatchLogDeliveryOptions.html
---

# CloudWatchLogDeliveryOptions
<a name="API_CloudWatchLogDeliveryOptions"></a>

The log delivery option to send data to Amazon CloudWatch Logs.

## Contents
<a name="API_CloudWatchLogDeliveryOptions_Contents"></a>

 ** logType **   <a name="iotfleetwise-Type-CloudWatchLogDeliveryOptions-logType"></a>
The type of log to send data to Amazon CloudWatch Logs.
Type: String
Valid Values: `OFF | ERROR`
Required: Yes

 ** logGroupName **   <a name="iotfleetwise-Type-CloudWatchLogDeliveryOptions-logGroupName"></a>
The Amazon CloudWatch Logs group the operation sends data to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_\/#A-Za-z0-9]+`
Required: No

## See Also
<a name="API_CloudWatchLogDeliveryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CloudWatchLogDeliveryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CloudWatchLogDeliveryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CloudWatchLogDeliveryOptions)
