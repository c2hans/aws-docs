---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetDeliverySource.html
---

# GetDeliverySource
<a name="API_GetDeliverySource"></a>

Retrieves complete information about one delivery source.

## Request Syntax
<a name="API_GetDeliverySource_RequestSyntax"></a>

```
{
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDeliverySource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetDeliverySource_RequestSyntax) **   <a name="CWL-GetDeliverySource-request-name"></a>
The name of the delivery source that you want to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w-]*`
Required: Yes

## Response Syntax
<a name="API_GetDeliverySource_ResponseSyntax"></a>

```
{
   "deliverySource": {
      "arn": "string",
      "deliverySourceConfiguration": {
         "string" : "string"
      },
      "logType": "string",
      "name": "string",
      "resourceArns": [ "string" ],
      "service": "string",
      "status": "string",
      "statusReason": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_GetDeliverySource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deliverySource](#API_GetDeliverySource_ResponseSyntax) **   <a name="CWL-GetDeliverySource-response-deliverySource"></a>
A structure containing information about the delivery source.
Type: [DeliverySource](API_DeliverySource.md) object

## Errors
<a name="API_GetDeliverySource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetDeliverySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetDeliverySource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetDeliverySource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetDeliverySource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetDeliverySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetDeliverySource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetDeliverySource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetDeliverySource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetDeliverySource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetDeliverySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetDeliverySource)
