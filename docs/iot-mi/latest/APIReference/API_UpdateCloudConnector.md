---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_UpdateCloudConnector.html
---

# UpdateCloudConnector
<a name="API_UpdateCloudConnector"></a>

Update an existing cloud connector.

## Request Syntax
<a name="API_UpdateCloudConnector_RequestSyntax"></a>

```
PUT /cloud-connectors/{{Identifier}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCloudConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_UpdateCloudConnector_RequestSyntax) **   <a name="managedintegrations-UpdateCloudConnector-request-uri-Identifier"></a>
The unique identifier of the cloud connector to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

## Request Body
<a name="API_UpdateCloudConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateCloudConnector_RequestSyntax) **   <a name="managedintegrations-UpdateCloudConnector-request-Description"></a>
The new description to assign to the cloud connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** [Name](#API_UpdateCloudConnector_RequestSyntax) **   <a name="managedintegrations-UpdateCloudConnector-request-Name"></a>
The new display name to assign to the cloud connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

## Response Syntax
<a name="API_UpdateCloudConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateCloudConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCloudConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

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
<a name="API_UpdateCloudConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/UpdateCloudConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/UpdateCloudConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/UpdateCloudConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/UpdateCloudConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/UpdateCloudConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/UpdateCloudConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/UpdateCloudConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/UpdateCloudConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/UpdateCloudConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/UpdateCloudConnector)
