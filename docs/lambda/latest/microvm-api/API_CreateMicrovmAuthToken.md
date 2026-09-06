---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_CreateMicrovmAuthToken.html
---

# CreateMicrovmAuthToken
<a name="API_CreateMicrovmAuthToken"></a>

Creates an authentication token for accessing a running MicroVM. The token grants access to the specified ports on the MicroVM endpoint.

## Request Syntax
<a name="API_CreateMicrovmAuthToken_RequestSyntax"></a>

```
POST /2025-09-09/microvms/{{microvmIdentifier}}/auth-token HTTP/1.1
Content-type: application/json

{
   "allowedPorts": [
      { ... }
   ],
   "expirationInMinutes": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateMicrovmAuthToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [microvmIdentifier](#API_CreateMicrovmAuthToken_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmAuthToken-request-uri-microvmIdentifier"></a>
The ID of the MicroVM to create an authentication token for.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_CreateMicrovmAuthToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowedPorts](#API_CreateMicrovmAuthToken_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmAuthToken-request-allowedPorts"></a>
The list of port specifications that the authentication token grants access to on the MicroVM.
Type: Array of [PortSpecification](API_PortSpecification.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [expirationInMinutes](#API_CreateMicrovmAuthToken_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmAuthToken-request-expirationInMinutes"></a>
The duration in minutes before the authentication token expires. Maximum: 60 minutes.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## Response Syntax
<a name="API_CreateMicrovmAuthToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authToken": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateMicrovmAuthToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authToken](#API_CreateMicrovmAuthToken_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmAuthToken-response-authToken"></a>
A map containing the authentication token. Use the value at key "X-aws-proxy-auth" as the header value when connecting to the MicroVM endpoint.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[^\s]+`
Value Length Constraints: Minimum length of 0. Maximum length of 8000.

## Errors
<a name="API_CreateMicrovmAuthToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry the request later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling. Retry the request later.
 ** quotaCode **
The quota code of the throttled service quota.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The service code of the throttled service quota.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_CreateMicrovmAuthToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/CreateMicrovmAuthToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/CreateMicrovmAuthToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/CreateMicrovmAuthToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/CreateMicrovmAuthToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/CreateMicrovmAuthToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/CreateMicrovmAuthToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/CreateMicrovmAuthToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/CreateMicrovmAuthToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/CreateMicrovmAuthToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/CreateMicrovmAuthToken)
