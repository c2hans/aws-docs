---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Delivery.html
---

# Delivery
<a name="API_Delivery"></a>

This structure contains information about one *delivery* in your account.

A delivery is a connection between a logical *delivery source* and a logical *delivery destination*.

For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).

To update an existing delivery configuration, use [UpdateDeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html).

## Contents
<a name="API_Delivery_Contents"></a>

 ** arn **   <a name="CWL-Type-Delivery-arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies this delivery.
Type: String
Required: No

 ** deliveryDestinationArn **   <a name="CWL-Type-Delivery-deliveryDestinationArn"></a>
The ARN of the delivery destination that is associated with this delivery.
Type: String
Required: No

 ** deliveryDestinationType **   <a name="CWL-Type-Delivery-deliveryDestinationType"></a>
Displays whether the delivery destination associated with this delivery is CloudWatch Logs, Amazon S3, Firehose, or X-Ray.
Type: String
Valid Values: `S3 | CWL | FH | XRAY`
Required: No

 ** deliverySourceName **   <a name="CWL-Type-Delivery-deliverySourceName"></a>
The name of the delivery source that is associated with this delivery.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w-]*`
Required: No

 ** fieldDelimiter **   <a name="CWL-Type-Delivery-fieldDelimiter"></a>
The field delimiter that is used between record fields when the final output format of a delivery is in `Plain`, `W3C`, or `Raw` format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5.
Required: No

 ** id **   <a name="CWL-Type-Delivery-id"></a>
The unique ID that identifies this delivery in your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9A-Za-z]+$`
Required: No

 ** recordFields **   <a name="CWL-Type-Delivery-recordFields"></a>
The record fields used in this delivery.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 128 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** s3DeliveryConfiguration **   <a name="CWL-Type-Delivery-s3DeliveryConfiguration"></a>
This structure contains delivery configurations that apply only when the delivery destination resource is an S3 bucket.
Type: [S3DeliveryConfiguration](API_S3DeliveryConfiguration.md) object
Required: No

 ** tags **   <a name="CWL-Type-Delivery-tags"></a>
The tags that have been assigned to this delivery.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_Delivery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/Delivery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/Delivery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/Delivery)
