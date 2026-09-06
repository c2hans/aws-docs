---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigStreamDeliveryInfo.html
---

# ConfigStreamDeliveryInfo
<a name="API_ConfigStreamDeliveryInfo"></a>

A list that contains the status of the delivery of the configuration stream notification to the Amazon SNS topic.

## Contents
<a name="API_ConfigStreamDeliveryInfo_Contents"></a>

 ** lastErrorCode **   <a name="config-Type-ConfigStreamDeliveryInfo-lastErrorCode"></a>
The error code from the last attempted delivery.
Type: String
Required: No

 ** lastErrorMessage **   <a name="config-Type-ConfigStreamDeliveryInfo-lastErrorMessage"></a>
The error message from the last attempted delivery.
Type: String
Required: No

 ** lastStatus **   <a name="config-Type-ConfigStreamDeliveryInfo-lastStatus"></a>
Status of the last attempted delivery.
 **Note** Providing an SNS topic on a [DeliveryChannel](https://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannel.html) for AWS Config is optional. If the SNS delivery is turned off, the last status will be **Not\_Applicable**.
Type: String
Valid Values: `Success | Failure | Not_Applicable`
Required: No

 ** lastStatusChangeTime **   <a name="config-Type-ConfigStreamDeliveryInfo-lastStatusChangeTime"></a>
The time from the last status change.
Type: Timestamp
Required: No

## See Also
<a name="API_ConfigStreamDeliveryInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigStreamDeliveryInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigStreamDeliveryInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigStreamDeliveryInfo)
