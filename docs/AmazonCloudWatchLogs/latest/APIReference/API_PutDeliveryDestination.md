---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html
---

# PutDeliveryDestination
<a name="API_PutDeliveryDestination"></a>

Creates or updates a logical *delivery destination*. A delivery destination is an AWS resource that represents an AWS service that logs can be sent to. CloudWatch Logs, Amazon S3, and Firehose are supported as logs delivery destinations and X-Ray as the trace delivery destination.

To configure logs delivery between a supported AWS service and a destination, you must do the following:
+ Create a delivery source, which is a logical object that represents the resource that is actually sending the logs. For more information, see [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html).
+ Use `PutDeliveryDestination` to create a *delivery destination* in the same account of the actual delivery destination. The delivery destination that you create is a logical object that represents the actual delivery destination.
+ If you are delivering logs cross-account, you must use [PutDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html) in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination.
+ Use `CreateDelivery` to create a *delivery* by pairing exactly one delivery source and one delivery destination. For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).

You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

Only some AWS services support being configured as a delivery source. These services are listed as **Supported [V2 Permissions]** in the table at [Enabling logging from AWS services.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)

If you use this operation to update an existing delivery destination, all the current delivery destination parameters are overwritten with the new parameter values that you specify.

## Request Syntax
<a name="API_PutDeliveryDestination_RequestSyntax"></a>

```
{
   "deliveryDestinationConfiguration": {
      "destinationResourceArn": "{{string}}"
   },
   "deliveryDestinationType": "{{string}}",
   "name": "{{string}}",
   "outputFormat": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_PutDeliveryDestination_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deliveryDestinationConfiguration](#API_PutDeliveryDestination_RequestSyntax) **   <a name="CWL-PutDeliveryDestination-request-deliveryDestinationConfiguration"></a>
A structure that contains the ARN of the AWS resource that will receive the logs.
 `deliveryDestinationConfiguration` is required for CloudWatch Logs, Amazon S3, Firehose log delivery destinations and not required for X-Ray trace delivery destinations. `deliveryDestinationType` is needed for X-Ray trace delivery destinations but not required for other logs delivery destinations.
Type: [DeliveryDestinationConfiguration](API_DeliveryDestinationConfiguration.md) object
Required: No

 ** [deliveryDestinationType](#API_PutDeliveryDestination_RequestSyntax) **   <a name="CWL-PutDeliveryDestination-request-deliveryDestinationType"></a>
The type of delivery destination. This parameter specifies the target service where log data will be delivered. Valid values include:
+  `S3` - Amazon S3 for long-term storage and analytics
+  `CWL` - CloudWatch Logs for centralized log management
+  `FH` - Amazon Kinesis Data Firehose for real-time data streaming
+  `XRAY` - AWS X-Ray for distributed tracing and application monitoring
The delivery destination type determines the format and configuration options available for log delivery.
Type: String
Valid Values: `S3 | CWL | FH | XRAY`
Required: No

 ** [name](#API_PutDeliveryDestination_RequestSyntax) **   <a name="CWL-PutDeliveryDestination-request-name"></a>
A name for this delivery destination. This name must be unique for all delivery destinations in your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w-]*`
Required: Yes

 ** [outputFormat](#API_PutDeliveryDestination_RequestSyntax) **   <a name="CWL-PutDeliveryDestination-request-outputFormat"></a>
The format for the logs that this delivery destination will receive.
Type: String
Valid Values: `json | plain | w3c | raw | parquet`
Required: No

 ** [tags](#API_PutDeliveryDestination_RequestSyntax) **   <a name="CWL-PutDeliveryDestination-request-tags"></a>
An optional list of key-value pairs to associate with the resource.
For more information about tagging, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_PutDeliveryDestination_ResponseSyntax"></a>

```
{
   "deliveryDestination": {
      "arn": "string",
      "deliveryDestinationConfiguration": {
         "destinationResourceArn": "string"
      },
      "deliveryDestinationType": "string",
      "name": "string",
      "outputFormat": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_PutDeliveryDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deliveryDestination](#API_PutDeliveryDestination_ResponseSyntax) **   <a name="CWL-PutDeliveryDestination-response-deliveryDestination"></a>
A structure containing information about the delivery destination that you just created or updated.
Type: [DeliveryDestination](API_DeliveryDestination.md) object

## Errors
<a name="API_PutDeliveryDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_PutDeliveryDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutDeliveryDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutDeliveryDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutDeliveryDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutDeliveryDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutDeliveryDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutDeliveryDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutDeliveryDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutDeliveryDestination)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutDeliveryDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutDeliveryDestination)
