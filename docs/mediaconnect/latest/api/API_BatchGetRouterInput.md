---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BatchGetRouterInput.html
---

# BatchGetRouterInput
<a name="API_BatchGetRouterInput"></a>

Retrieves information about multiple router inputs in AWS Elemental MediaConnect.

## Request Syntax
<a name="API_BatchGetRouterInput_RequestSyntax"></a>

```
GET /v1/routerInputs?arns={{arns}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BatchGetRouterInput_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arns](#API_BatchGetRouterInput_RequestSyntax) **   <a name="mediaconnect-BatchGetRouterInput-request-uri-arns"></a>
The Amazon Resource Names (ARNs) of the router inputs you want to retrieve information about.
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`
Required: Yes

## Request Body
<a name="API_BatchGetRouterInput_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BatchGetRouterInput_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "arn": "string",
         "code": "string",
         "message": "string"
      }
   ],
   "routerInputs": [
      {
         "arn": "string",
         "availabilityZone": "string",
         "configuration": { ... },
         "contentQualityAnalysisConfiguration": { ... },
         "contentQualityAnalysisType": "string",
         "createdAt": "string",
         "id": "string",
         "inputType": "string",
         "ipAddress": "string",
         "maintenanceConfiguration": { ... },
         "maintenanceSchedule": { ... },
         "maintenanceScheduleType": "string",
         "maintenanceType": "string",
         "maximumBitrate": number,
         "maximumRoutedOutputs": number,
         "messages": [
            {
               "code": "string",
               "message": "string"
            }
         ],
         "name": "string",
         "regionName": "string",
         "routedOutputs": number,
         "routingScope": "string",
         "state": "string",
         "streamDetails": { ... },
         "tags": {
            "string" : "string"
         },
         "tier": "string",
         "transitEncryption": {
            "encryptionKeyConfiguration": { ... },
            "encryptionKeyType": "string"
         },
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetRouterInput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetRouterInput_ResponseSyntax) **   <a name="mediaconnect-BatchGetRouterInput-response-errors"></a>
An array of errors that occurred when retrieving the requested router inputs.
Type: Array of [BatchGetRouterInputError](API_BatchGetRouterInputError.md) objects

 ** [routerInputs](#API_BatchGetRouterInput_ResponseSyntax) **   <a name="mediaconnect-BatchGetRouterInput-response-routerInputs"></a>
An array of router inputs that were successfully retrieved.
Type: Array of [RouterInput](API_RouterInput.md) objects

## Errors
<a name="API_BatchGetRouterInput_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_BatchGetRouterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/BatchGetRouterInput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/BatchGetRouterInput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BatchGetRouterInput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/BatchGetRouterInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BatchGetRouterInput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/BatchGetRouterInput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/BatchGetRouterInput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/BatchGetRouterInput)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/BatchGetRouterInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BatchGetRouterInput)
