---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetSinkPolicy.html
---

# GetSinkPolicy
<a name="API_GetSinkPolicy"></a>

Returns the current sink policy attached to this sink. The sink policy specifies what accounts can attach to this sink as source accounts, and what types of data they can share.

## Request Syntax
<a name="API_GetSinkPolicy_RequestSyntax"></a>

```
POST /GetSinkPolicy HTTP/1.1
Content-type: application/json

{
   "SinkIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetSinkPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetSinkPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SinkIdentifier](#API_GetSinkPolicy_RequestSyntax) **   <a name="OAM-GetSinkPolicy-request-SinkIdentifier"></a>
The ARN of the sink to retrieve the policy of.
Type: String
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_:\.\-\/]{0,2047}`
Required: Yes

## Response Syntax
<a name="API_GetSinkPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": "string",
   "SinkArn": "string",
   "SinkId": "string"
}
```

## Response Elements
<a name="API_GetSinkPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_GetSinkPolicy_ResponseSyntax) **   <a name="OAM-GetSinkPolicy-response-Policy"></a>
The policy that you specified, in JSON format.
Type: String

 ** [SinkArn](#API_GetSinkPolicy_ResponseSyntax) **   <a name="OAM-GetSinkPolicy-response-SinkArn"></a>
The ARN of the sink.
Type: String

 ** [SinkId](#API_GetSinkPolicy_ResponseSyntax) **   <a name="OAM-GetSinkPolicy-response-SinkId"></a>
The random ID string that AWS generated as part of the sink ARN.
Type: String

## Errors
<a name="API_GetSinkPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceFault **
Unexpected error while processing the request. Retry the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 500

 ** InvalidParameterException **
A parameter is specified incorrectly.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** MissingRequiredParameterException **
A required parameter is missing from the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 404

## See Also
<a name="API_GetSinkPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/GetSinkPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/GetSinkPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/GetSinkPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/GetSinkPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/GetSinkPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/GetSinkPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/GetSinkPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/GetSinkPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/GetSinkPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/GetSinkPolicy)
