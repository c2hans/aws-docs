---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateConnector.html
---

# UpdateConnector
<a name="API_UpdateConnector"></a>

Updates the description or provider-specific configuration details of an existing connector.

## Request Syntax
<a name="API_UpdateConnector_RequestSyntax"></a>

```
POST /connector/update HTTP/1.1
Content-type: application/json

{
   "connectorArn": "{{string}}",
   "description": "{{string}}",
   "providerDetail": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [connectorArn](#API_UpdateConnector_RequestSyntax) **   <a name="inspector2-UpdateConnector-request-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws(-[a-z]+)*:inspector2:[a-z0-9-]+:[0-9]{12}:connector/([a-f0-9-]+|aws-service-connector/.+/[a-f0-9-]+)`
Required: Yes

 ** [description](#API_UpdateConnector_RequestSyntax) **   <a name="inspector2-UpdateConnector-request-description"></a>
The updated description of the connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[^\p{C}]*`
Required: No

 ** [providerDetail](#API_UpdateConnector_RequestSyntax) **   <a name="inspector2-UpdateConnector-request-providerDetail"></a>
The updated provider-specific configuration details for the connector.
Type: [ProviderDetailUpdate](API_ProviderDetailUpdate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_UpdateConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorArn": "string"
}
```

## Response Elements
<a name="API_UpdateConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectorArn](#API_UpdateConnector_ResponseSyntax) **   <a name="inspector2-UpdateConnector-response-connectorArn"></a>
The Amazon Resource Name (ARN) of the updated connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws(-[a-z]+)*:inspector2:[a-z0-9-]+:[0-9]{12}:connector/([a-f0-9-]+|aws-service-connector/.+/[a-f0-9-]+)`

## Errors
<a name="API_UpdateConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred. This exception occurs when the same resource is being modified by concurrent requests.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/UpdateConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/UpdateConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/UpdateConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/UpdateConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/UpdateConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/UpdateConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/UpdateConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateConnector)
