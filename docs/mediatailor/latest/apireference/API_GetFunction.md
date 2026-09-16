---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_GetFunction.html
---

# GetFunction
<a name="API_GetFunction"></a>

Retrieves the configuration and metadata for a function. For more information about functions, see [Working with functions](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_GetFunction_RequestSyntax"></a>

```
GET /function/{{FunctionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionId](#API_GetFunction_RequestSyntax) **   <a name="mediatailor-GetFunction-request-uri-FunctionId"></a>
The identifier of the function.
Required: Yes

## Request Body
<a name="API_GetFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFunction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "ConcurrentExecutorConfiguration": {
      "FunctionList": [
         {
            "Alias": "string",
            "FunctionId": "string",
            "RunCondition": "string"
         }
      ],
      "MaxConcurrency": number,
      "Output": {
         "string" : "string"
      },
      "Runtime": "string",
      "TimeoutMilliseconds": number
   },
   "CustomOutputConfiguration": {
      "Output": {
         "string" : "string"
      },
      "Runtime": "string"
   },
   "Description": "string",
   "FunctionId": "string",
   "FunctionType": "string",
   "HttpRequestConfiguration": {
      "Body": "string",
      "Headers": {
         "string" : "string"
      },
      "MethodType": "string",
      "Output": {
         "string" : "string"
      },
      "RequestTimeoutMilliseconds": number,
      "Runtime": "string",
      "Url": "string"
   },
   "SequentialExecutorConfiguration": {
      "FunctionList": [
         {
            "Alias": "string",
            "FunctionId": "string",
            "RunCondition": "string"
         }
      ],
      "Output": {
         "string" : "string"
      },
      "Runtime": "string",
      "TimeoutMilliseconds": number
   },
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetFunction_ResponseSyntax) **   <a name="mediatailor-GetFunction-response-Arn"></a>
The Amazon Resource Name (ARN) of the function.
Type: String

 ** [ConcurrentExecutorConfiguration](#API_GetFunction_ResponseSyntax) **   <a name="mediatailor-GetFunction-response-ConcurrentExecutorConfiguration"></a>
The configuration for a `CONCURRENT_EXECUTOR` function.
Type: [ConcurrentExecutorConfiguration](API_ConcurrentExecutorConfiguration.md) object

 ** [CustomOutputConfiguration](#API_GetFunction_ResponseSyntax) **   <a name="mediatailor-GetFunction-response-CustomOutputConfiguration"></a>
The configuration for a `CUSTOM_OUTPUT` function.
Type: [CustomOutputConfiguration](API_CustomOutputConfiguration.md) object

 ** [Description](#API_GetFunction_ResponseSyntax) **   <a name="mediatailor-GetFunction-response-Description"></a>
A description of the function.
Type: String

 ** [FunctionId](#API_GetFunction_ResponseSyntax) **   <a name="mediatailor-GetFunction-response-FunctionId"></a>
The identifier of the function.
Type: String

 ** [FunctionType](#API_GetFunction_ResponseSyntax) **   <a name="mediatailor-GetFunction-response-FunctionType"></a>
The type of the function.
Type: String
Valid Values: `HTTP_REQUEST | CUSTOM_OUTPUT | CONCURRENT_EXECUTOR | SEQUENTIAL_EXECUTOR`

 ** [HttpRequestConfiguration](#API_GetFunction_ResponseSyntax) **   <a name="mediatailor-GetFunction-response-HttpRequestConfiguration"></a>
The configuration for an `HTTP_REQUEST` function.
Type: [HttpRequestConfiguration](API_HttpRequestConfiguration.md) object

 ** [SequentialExecutorConfiguration](#API_GetFunction_ResponseSyntax) **   <a name="mediatailor-GetFunction-response-SequentialExecutorConfiguration"></a>
The configuration for a `SEQUENTIAL_EXECUTOR` function.
Type: [SequentialExecutorConfiguration](API_SequentialExecutorConfiguration.md) object

 ** [tags](#API_GetFunction_ResponseSyntax) **   <a name="mediatailor-GetFunction-response-tags"></a>
The tags assigned to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

## Errors
<a name="API_GetFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/GetFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/GetFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/GetFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/GetFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/GetFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/GetFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/GetFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/GetFunction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/GetFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/GetFunction)
