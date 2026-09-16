---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_StartAccountAssociationRefresh.html
---

# StartAccountAssociationRefresh
<a name="API_StartAccountAssociationRefresh"></a>

Initiates a refresh of an existing account association to update its authorization and connection status.

## Request Syntax
<a name="API_StartAccountAssociationRefresh_RequestSyntax"></a>

```
POST /account-associations/{{AccountAssociationId}}/refresh HTTP/1.1
```

## URI Request Parameters
<a name="API_StartAccountAssociationRefresh_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountAssociationId](#API_StartAccountAssociationRefresh_RequestSyntax) **   <a name="managedintegrations-StartAccountAssociationRefresh-request-uri-AccountAssociationId"></a>
The unique identifier of the account association to refresh.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

## Request Body
<a name="API_StartAccountAssociationRefresh_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StartAccountAssociationRefresh_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "OAuthAuthorizationUrl": "string"
}
```

## Response Elements
<a name="API_StartAccountAssociationRefresh_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OAuthAuthorizationUrl](#API_StartAccountAssociationRefresh_ResponseSyntax) **   <a name="managedintegrations-StartAccountAssociationRefresh-response-OAuthAuthorizationUrl"></a>
Third-party IoT platform OAuth authorization server URL with all required parameters to perform end-user authentication during the refresh process. This field will be empty when using General Authorization flows that do not require OAuth.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `$|^(https):\/\/.*`

## Errors
<a name="API_StartAccountAssociationRefresh_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_StartAccountAssociationRefresh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/StartAccountAssociationRefresh)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/StartAccountAssociationRefresh)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/StartAccountAssociationRefresh)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/StartAccountAssociationRefresh)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/StartAccountAssociationRefresh)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/StartAccountAssociationRefresh)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/StartAccountAssociationRefresh)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/StartAccountAssociationRefresh)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/StartAccountAssociationRefresh)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/StartAccountAssociationRefresh)
