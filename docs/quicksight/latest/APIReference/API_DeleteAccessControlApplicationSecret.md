---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteAccessControlApplicationSecret.html
---

# DeleteAccessControlApplicationSecret

Deletes a client secret from an access control application.

## Request Syntax
<a name="API_DeleteAccessControlApplicationSecret_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/access-control-applications/{{ApplicationId}}/client-secrets/{{ClientSecretId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAccessControlApplicationSecret_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_DeleteAccessControlApplicationSecret_RequestSyntax) **   <a name="QS-DeleteAccessControlApplicationSecret-request-uri-ApplicationId"></a>
The ID of the access control application.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [AwsAccountId](#API_DeleteAccessControlApplicationSecret_RequestSyntax) **   <a name="QS-DeleteAccessControlApplicationSecret-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the Quick Sight account.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [ClientSecretId](#API_DeleteAccessControlApplicationSecret_RequestSyntax) **   <a name="QS-DeleteAccessControlApplicationSecret-request-uri-ClientSecretId"></a>
The ID of the client secret.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_DeleteAccessControlApplicationSecret_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAccessControlApplicationSecret_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DeleteAccessControlApplicationSecret_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteAccessControlApplicationSecret_ResponseSyntax) **   <a name="QS-DeleteAccessControlApplicationSecret-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_DeleteAccessControlApplicationSecret_ResponseSyntax) **   <a name="QS-DeleteAccessControlApplicationSecret-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_DeleteAccessControlApplicationSecret_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DeleteAccessControlApplicationSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteAccessControlApplicationSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteAccessControlApplicationSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteAccessControlApplicationSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteAccessControlApplicationSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteAccessControlApplicationSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteAccessControlApplicationSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteAccessControlApplicationSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteAccessControlApplicationSecret)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteAccessControlApplicationSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteAccessControlApplicationSecret)
