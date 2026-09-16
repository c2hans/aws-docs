---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_PutHubConfiguration.html
---

# PutHubConfiguration
<a name="API_PutHubConfiguration"></a>

Update a hub configuration.

## Request Syntax
<a name="API_PutHubConfiguration_RequestSyntax"></a>

```
PUT /hub-configuration HTTP/1.1
Content-type: application/json

{
   "HubTokenTimerExpirySettingInSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_PutHubConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutHubConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [HubTokenTimerExpirySettingInSeconds](#API_PutHubConfiguration_RequestSyntax) **   <a name="managedintegrations-PutHubConfiguration-request-HubTokenTimerExpirySettingInSeconds"></a>
A user-defined integer value that represents the hub token timer expiry setting in seconds.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## Response Syntax
<a name="API_PutHubConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "HubTokenTimerExpirySettingInSeconds": number
}
```

## Response Elements
<a name="API_PutHubConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [HubTokenTimerExpirySettingInSeconds](#API_PutHubConfiguration_ResponseSyntax) **   <a name="managedintegrations-PutHubConfiguration-response-HubTokenTimerExpirySettingInSeconds"></a>
A user-defined integer value that represents the hub token timer expiry setting in seconds.
Type: Long
Valid Range: Minimum value of 1.

## Errors
<a name="API_PutHubConfiguration_Errors"></a>

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
<a name="API_PutHubConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/PutHubConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/PutHubConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/PutHubConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/PutHubConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/PutHubConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/PutHubConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/PutHubConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/PutHubConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/PutHubConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/PutHubConfiguration)
