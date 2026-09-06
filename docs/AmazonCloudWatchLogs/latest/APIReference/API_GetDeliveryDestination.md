---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetDeliveryDestination.html
---

# GetDeliveryDestination
<a name="API_GetDeliveryDestination"></a>

Retrieves complete information about one delivery destination.

## Request Syntax
<a name="API_GetDeliveryDestination_RequestSyntax"></a>

```
{
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDeliveryDestination_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetDeliveryDestination_RequestSyntax) **   <a name="CWL-GetDeliveryDestination-request-name"></a>
The name of the delivery destination that you want to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w-]*`
Required: Yes

## Response Syntax
<a name="API_GetDeliveryDestination_ResponseSyntax"></a>

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
<a name="API_GetDeliveryDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deliveryDestination](#API_GetDeliveryDestination_ResponseSyntax) **   <a name="CWL-GetDeliveryDestination-response-deliveryDestination"></a>
A structure containing information about the delivery destination.
Type: [DeliveryDestination](API_DeliveryDestination.md) object

## Errors
<a name="API_GetDeliveryDestination_Errors"></a>

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
<a name="API_GetDeliveryDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetDeliveryDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetDeliveryDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetDeliveryDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetDeliveryDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetDeliveryDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetDeliveryDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetDeliveryDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetDeliveryDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetDeliveryDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetDeliveryDestination)
