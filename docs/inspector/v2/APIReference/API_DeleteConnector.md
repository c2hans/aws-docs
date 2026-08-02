---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteConnector.html
---

# DeleteConnector
<a name="API_DeleteConnector"></a>

Deletes a connector from your account.

## Request Syntax
<a name="API_DeleteConnector_RequestSyntax"></a>

```
POST /connector/delete HTTP/1.1
Content-type: application/json

{
   "connectorArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [connectorArn](#API_DeleteConnector_RequestSyntax) **   <a name="inspector2-DeleteConnector-request-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws(-[a-z]+)*:inspector2:[a-z0-9-]+:[0-9]{12}:connector/([a-f0-9-]+|aws-service-connector/.+/[a-f0-9-]+)`
Required: Yes

## Response Syntax
<a name="API_DeleteConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteConnector_Errors"></a>

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
<a name="API_DeleteConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/DeleteConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/DeleteConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/DeleteConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/DeleteConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/DeleteConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/DeleteConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/DeleteConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/DeleteConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/DeleteConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/DeleteConnector)
