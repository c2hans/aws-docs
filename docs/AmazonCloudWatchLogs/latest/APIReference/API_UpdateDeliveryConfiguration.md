---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html
---

# UpdateDeliveryConfiguration
<a name="API_UpdateDeliveryConfiguration"></a>

Use this operation to update the configuration of a [delivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Delivery.html) to change either the S3 path pattern or the format of the delivered logs. You can't use this operation to change the source or destination of the delivery.

## Request Syntax
<a name="API_UpdateDeliveryConfiguration_RequestSyntax"></a>

```
{
   "fieldDelimiter": "{{string}}",
   "id": "{{string}}",
   "recordFields": [ "{{string}}" ],
   "s3DeliveryConfiguration": {
      "enableHiveCompatiblePath": {{boolean}},
      "suffixPath": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateDeliveryConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [fieldDelimiter](#API_UpdateDeliveryConfiguration_RequestSyntax) **   <a name="CWL-UpdateDeliveryConfiguration-request-fieldDelimiter"></a>
The field delimiter to use between record fields when the final output format of a delivery is in `Plain`, `W3C`, or `Raw` format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5.
Required: No

 ** [id](#API_UpdateDeliveryConfiguration_RequestSyntax) **   <a name="CWL-UpdateDeliveryConfiguration-request-id"></a>
The ID of the delivery to be updated by this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9A-Za-z]+$`
Required: Yes

 ** [recordFields](#API_UpdateDeliveryConfiguration_RequestSyntax) **   <a name="CWL-UpdateDeliveryConfiguration-request-recordFields"></a>
The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 128 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [s3DeliveryConfiguration](#API_UpdateDeliveryConfiguration_RequestSyntax) **   <a name="CWL-UpdateDeliveryConfiguration-request-s3DeliveryConfiguration"></a>
This structure contains parameters that are valid only when the delivery's delivery destination is an S3 bucket.
Type: [S3DeliveryConfiguration](API_S3DeliveryConfiguration.md) object
Required: No

## Response Elements
<a name="API_UpdateDeliveryConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDeliveryConfiguration_Errors"></a>

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
<a name="API_UpdateDeliveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/UpdateDeliveryConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/UpdateDeliveryConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/UpdateDeliveryConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/UpdateDeliveryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/UpdateDeliveryConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/UpdateDeliveryConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/UpdateDeliveryConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/UpdateDeliveryConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/UpdateDeliveryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/UpdateDeliveryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
