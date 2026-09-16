---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_RegisterCustomEndpoint.html
---

# RegisterCustomEndpoint
<a name="API_RegisterCustomEndpoint"></a>

Customers can request IoT managed integrations to manage the server trust for them or bring their own external server trusts for the custom domain. Returns an IoT managed integrations endpoint.

## Request Syntax
<a name="API_RegisterCustomEndpoint_RequestSyntax"></a>

```
POST /custom-endpoint HTTP/1.1
```

## URI Request Parameters
<a name="API_RegisterCustomEndpoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterCustomEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RegisterCustomEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "EndpointAddress": "string"
}
```

## Response Elements
<a name="API_RegisterCustomEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [EndpointAddress](#API_RegisterCustomEndpoint_ResponseSyntax) **   <a name="managedintegrations-RegisterCustomEndpoint-response-EndpointAddress"></a>
The IoT managed integrations dedicated, custom endpoint for the device to route traffic through.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9._@-]+`

## Errors
<a name="API_RegisterCustomEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict with the request.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
HTTP Status Code: 401

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_RegisterCustomEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/RegisterCustomEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/RegisterCustomEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/RegisterCustomEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/RegisterCustomEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/RegisterCustomEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/RegisterCustomEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/RegisterCustomEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/RegisterCustomEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/RegisterCustomEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/RegisterCustomEndpoint)
