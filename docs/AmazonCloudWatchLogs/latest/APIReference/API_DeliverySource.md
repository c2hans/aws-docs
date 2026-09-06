---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeliverySource.html
---

# DeliverySource
<a name="API_DeliverySource"></a>

This structure contains information about one *delivery source* in your account. A delivery source is an AWS resource that sends logs to an AWS destination. The destination can be CloudWatch Logs, Amazon S3, or Firehose.

Only some AWS services support being configured as a delivery source. These services are listed as **Supported [V2 Permissions]** in the table at [Enabling logging from AWS services.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)

To configure logs delivery between a supported AWS service and a destination, you must do the following:
+ Create a delivery source, which is a logical object that represents the resource that is actually sending the logs. For more information, see [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html).
+ Create a *delivery destination*, which is a logical object that represents the actual delivery destination. For more information, see [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html).
+ If you are delivering logs cross-account, you must use [PutDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html) in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination.
+ Create a *delivery* by pairing exactly one delivery source and one delivery destination. For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).

You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

## Contents
<a name="API_DeliverySource_Contents"></a>

 ** arn **   <a name="CWL-Type-DeliverySource-arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies this delivery source.
Type: String
Required: No

 ** deliverySourceConfiguration **   <a name="CWL-Type-DeliverySource-deliverySourceConfiguration"></a>
The map of key-value pairs that configure the delivery source.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** logType **   <a name="CWL-Type-DeliverySource-logType"></a>
The type of log that the source is sending. For valid values for this parameter, see the documentation for the source service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w]*`
Required: No

 ** name **   <a name="CWL-Type-DeliverySource-name"></a>
The unique name of the delivery source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w-]*`
Required: No

 ** resourceArns **   <a name="CWL-Type-DeliverySource-resourceArns"></a>
This array contains the ARN of the AWS resource that sends logs and is represented by this delivery source. Currently, only one ARN can be in the array.
Type: Array of strings
Required: No

 ** service **   <a name="CWL-Type-DeliverySource-service"></a>
The AWS service that is sending logs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w_-]*`
Required: No

 ** status **   <a name="CWL-Type-DeliverySource-status"></a>
The status of the delivery source. A delivery source can have the status `ACTIVE` or `INACTIVE`. Note: This value is defined for selective log types.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** statusReason **   <a name="CWL-Type-DeliverySource-statusReason"></a>
The reason for the status of the delivery source. A status reason of `RESOURCE_DELETED` indicates that the resource associated with the delivery source has been deleted. Note: This value is defined for selective log types.
Type: String
Valid Values: `RESOURCE_DELETED`
Required: No

 ** tags **   <a name="CWL-Type-DeliverySource-tags"></a>
The tags that have been assigned to this delivery source.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_DeliverySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DeliverySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DeliverySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DeliverySource)
