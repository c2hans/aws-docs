---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PutFunction.html
---

# PutFunction
<a name="API_PutFunction"></a>

Creates or updates a function. A function defines reusable logic that MediaTailor executes at lifecycle hooks during ad insertion. For more information about functions, see [Working with functions](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_PutFunction_RequestSyntax"></a>

```
PUT /function/{{FunctionId}} HTTP/1.1
Content-type: application/json

{
   "CustomOutputConfiguration": {
      "Output": {
         "{{string}}" : "{{string}}"
      },
      "Runtime": "{{string}}"
   },
   "Description": "{{string}}",
   "FunctionType": "{{string}}",
   "HttpRequestConfiguration": {
      "Body": "{{string}}",
      "Headers": {
         "{{string}}" : "{{string}}"
      },
      "MethodType": "{{string}}",
      "Output": {
         "{{string}}" : "{{string}}"
      },
      "RequestTimeoutMilliseconds": {{number}},
      "Runtime": "{{string}}",
      "Url": "{{string}}"
   },
   "SequentialExecutorConfiguration": {
      "FunctionList": [
         {
            "FunctionId": "{{string}}",
            "RunCondition": "{{string}}"
         }
      ],
      "Output": {
         "{{string}}" : "{{string}}"
      },
      "Runtime": "{{string}}",
      "TimeoutMilliseconds": {{number}}
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_PutFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionId](#API_PutFunction_RequestSyntax) **   <a name="mediatailor-PutFunction-request-uri-FunctionId"></a>
The identifier of the function. The identifier must be unique within your account.
Required: Yes

## Request Body
<a name="API_PutFunction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CustomOutputConfiguration](#API_PutFunction_RequestSyntax) **   <a name="mediatailor-PutFunction-request-CustomOutputConfiguration"></a>
The configuration for a `CUSTOM_OUTPUT` function. Specifies the runtime and output expressions. Required when `FunctionType` is `CUSTOM_OUTPUT`.
Type: [CustomOutputConfiguration](API_CustomOutputConfiguration.md) object
Required: No

 ** [Description](#API_PutFunction_RequestSyntax) **   <a name="mediatailor-PutFunction-request-Description"></a>
A description of the function.
Type: String
Required: No

 ** [FunctionType](#API_PutFunction_RequestSyntax) **   <a name="mediatailor-PutFunction-request-FunctionType"></a>
The type of the function. The function type determines what the function can do at runtime. Valid values: `CUSTOM_OUTPUT` evaluates expressions and produces output bindings with no external calls. `HTTP_REQUEST` makes an HTTP call to an external service and evaluates output expressions that can reference the response. `SEQUENTIAL_EXECUTOR` runs a sequence of child functions in order, passing data between steps through temporary data. For more information, see [Function types and composition](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types.html) in the *MediaTailor User Guide*.
Type: String
Valid Values: `HTTP_REQUEST | CUSTOM_OUTPUT | SEQUENTIAL_EXECUTOR`
Required: Yes

 ** [HttpRequestConfiguration](#API_PutFunction_RequestSyntax) **   <a name="mediatailor-PutFunction-request-HttpRequestConfiguration"></a>
The configuration for an `HTTP_REQUEST` function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when `FunctionType` is `HTTP_REQUEST`.
Type: [HttpRequestConfiguration](API_HttpRequestConfiguration.md) object
Required: No

 ** [SequentialExecutorConfiguration](#API_PutFunction_RequestSyntax) **   <a name="mediatailor-PutFunction-request-SequentialExecutorConfiguration"></a>
The configuration for a `SEQUENTIAL_EXECUTOR` function. Specifies the ordered list of child functions to execute, an optional output block, and a timeout. Required when `FunctionType` is `SEQUENTIAL_EXECUTOR`.
Type: [SequentialExecutorConfiguration](API_SequentialExecutorConfiguration.md) object
Required: No

 ** [tags](#API_PutFunction_RequestSyntax) **   <a name="mediatailor-PutFunction-request-tags"></a>
The tags to assign to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

## Response Syntax
<a name="API_PutFunction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
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
<a name="API_PutFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_PutFunction_ResponseSyntax) **   <a name="mediatailor-PutFunction-response-Arn"></a>
The Amazon Resource Name (ARN) of the function.
Type: String

 ** [CustomOutputConfiguration](#API_PutFunction_ResponseSyntax) **   <a name="mediatailor-PutFunction-response-CustomOutputConfiguration"></a>
The configuration for a `CUSTOM_OUTPUT` function.
Type: [CustomOutputConfiguration](API_CustomOutputConfiguration.md) object

 ** [Description](#API_PutFunction_ResponseSyntax) **   <a name="mediatailor-PutFunction-response-Description"></a>
A description of the function.
Type: String

 ** [FunctionId](#API_PutFunction_ResponseSyntax) **   <a name="mediatailor-PutFunction-response-FunctionId"></a>
The identifier of the function.
Type: String

 ** [FunctionType](#API_PutFunction_ResponseSyntax) **   <a name="mediatailor-PutFunction-response-FunctionType"></a>
The type of the function.
Type: String
Valid Values: `HTTP_REQUEST | CUSTOM_OUTPUT | SEQUENTIAL_EXECUTOR`

 ** [HttpRequestConfiguration](#API_PutFunction_ResponseSyntax) **   <a name="mediatailor-PutFunction-response-HttpRequestConfiguration"></a>
The configuration for an `HTTP_REQUEST` function.
Type: [HttpRequestConfiguration](API_HttpRequestConfiguration.md) object

 ** [SequentialExecutorConfiguration](#API_PutFunction_ResponseSyntax) **   <a name="mediatailor-PutFunction-response-SequentialExecutorConfiguration"></a>
The configuration for a `SEQUENTIAL_EXECUTOR` function.
Type: [SequentialExecutorConfiguration](API_SequentialExecutorConfiguration.md) object

 ** [tags](#API_PutFunction_ResponseSyntax) **   <a name="mediatailor-PutFunction-response-tags"></a>
The tags assigned to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

## Errors
<a name="API_PutFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_PutFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/PutFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/PutFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/PutFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/PutFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/PutFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/PutFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/PutFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/PutFunction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/PutFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/PutFunction)
