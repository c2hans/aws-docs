---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html
---

# CreateDelivery
<a name="API_CreateDelivery"></a>

Creates a *delivery*. A delivery is a connection between a logical *delivery source* and a logical *delivery destination* that you have already created.

Only some AWS services support being configured as a delivery source using this operation. These services are listed as **Supported [V2 Permissions]** in the table at [Enabling logging from AWS services.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)

A delivery destination can represent a log group in CloudWatch Logs, an Amazon S3 bucket, a delivery stream in Firehose, or X-Ray.

To configure logs delivery between a supported AWS service and a destination, you must do the following:
+ Create a delivery source, which is a logical object that represents the resource that is actually sending the logs. For more information, see [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html).
+ Create a *delivery destination*, which is a logical object that represents the actual delivery destination. For more information, see [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html).
+ If you are delivering logs cross-account, you must use [PutDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html) in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination.
+ Use `CreateDelivery` to create a *delivery* by pairing exactly one delivery source and one delivery destination.

You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

To update an existing delivery configuration, use [UpdateDeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html).

## Request Syntax
<a name="API_CreateDelivery_RequestSyntax"></a>

```
{
   "deliveryDestinationArn": "{{string}}",
   "deliverySourceName": "{{string}}",
   "fieldDelimiter": "{{string}}",
   "recordFields": [ "{{string}}" ],
   "s3DeliveryConfiguration": {
      "enableHiveCompatiblePath": {{boolean}},
      "suffixPath": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateDelivery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deliveryDestinationArn](#API_CreateDelivery_RequestSyntax) **   <a name="CWL-CreateDelivery-request-deliveryDestinationArn"></a>
The ARN of the delivery destination to use for this delivery.
Type: String
Required: Yes

 ** [deliverySourceName](#API_CreateDelivery_RequestSyntax) **   <a name="CWL-CreateDelivery-request-deliverySourceName"></a>
The name of the delivery source to use for this delivery.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w-]*`
Required: Yes

 ** [fieldDelimiter](#API_CreateDelivery_RequestSyntax) **   <a name="CWL-CreateDelivery-request-fieldDelimiter"></a>
The field delimiter to use between record fields when the final output format of a delivery is in `Plain`, `W3C`, or `Raw` format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5.
Required: No

 ** [recordFields](#API_CreateDelivery_RequestSyntax) **   <a name="CWL-CreateDelivery-request-recordFields"></a>
The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 128 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [s3DeliveryConfiguration](#API_CreateDelivery_RequestSyntax) **   <a name="CWL-CreateDelivery-request-s3DeliveryConfiguration"></a>
This structure contains parameters that are valid only when the delivery's delivery destination is an S3 bucket.
Type: [S3DeliveryConfiguration](API_S3DeliveryConfiguration.md) object
Required: No

 ** [tags](#API_CreateDelivery_RequestSyntax) **   <a name="CWL-CreateDelivery-request-tags"></a>
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
<a name="API_CreateDelivery_ResponseSyntax"></a>

```
{
   "delivery": {
      "arn": "string",
      "deliveryDestinationArn": "string",
      "deliveryDestinationType": "string",
      "deliverySourceName": "string",
      "fieldDelimiter": "string",
      "id": "string",
      "recordFields": [ "string" ],
      "s3DeliveryConfiguration": {
         "enableHiveCompatiblePath": boolean,
         "suffixPath": "string"
      },
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateDelivery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [delivery](#API_CreateDelivery_ResponseSyntax) **   <a name="CWL-CreateDelivery-response-delivery"></a>
A structure that contains information about the delivery that you just created.
Type: [Delivery](API_Delivery.md) object

## Errors
<a name="API_CreateDelivery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

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
<a name="API_CreateDelivery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/CreateDelivery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/CreateDelivery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/CreateDelivery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/CreateDelivery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/CreateDelivery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/CreateDelivery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/CreateDelivery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/CreateDelivery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/CreateDelivery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/CreateDelivery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
