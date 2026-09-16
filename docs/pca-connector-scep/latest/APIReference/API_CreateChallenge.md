---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html
---

# CreateChallenge
<a name="API_CreateChallenge"></a>

For general-purpose connectors. Creates a *challenge password* for the specified connector. The SCEP protocol uses a challenge password to authenticate a request before issuing a certificate from a certificate authority (CA). Your SCEP clients include the challenge password as part of their certificate request to Connector for SCEP. To retrieve the connector Amazon Resource Names (ARNs) for the connectors in your account, call [ListConnectors](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html).

To create additional challenge passwords for the connector, call `CreateChallenge` again. We recommend frequently rotating your challenge passwords.

## Request Syntax
<a name="API_CreateChallenge_RequestSyntax"></a>

```
POST /challenges HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ConnectorArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateChallenge_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateChallenge_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateChallenge_RequestSyntax) **   <a name="pcaconnectorscep-CreateChallenge-request-ClientToken"></a>
Custom string that can be used to distinguish between calls to the [CreateChallenge](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html) action. Client tokens for `CreateChallenge` time out after five minutes. Therefore, if you call `CreateChallenge` multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [ConnectorArn](#API_CreateChallenge_RequestSyntax) **   <a name="pcaconnectorscep-CreateChallenge-request-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connector that you want to create a challenge for.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: Yes

 ** [Tags](#API_CreateChallenge_RequestSyntax) **   <a name="pcaconnectorscep-CreateChallenge-request-Tags"></a>
The key-value pairs to associate with the resource.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateChallenge_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "Challenge": {
      "Arn": "string",
      "ConnectorArn": "string",
      "CreatedAt": number,
      "Password": "string",
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_CreateChallenge_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [Challenge](#API_CreateChallenge_ResponseSyntax) **   <a name="pcaconnectorscep-CreateChallenge-response-Challenge"></a>
Returns the challenge details for the specified connector.
Type: [Challenge](API_Challenge.md) object

## Errors
<a name="API_CreateChallenge_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your AWS Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an AWS Organizations service control policy (SCP) that affects your AWS account.
HTTP Status Code: 403

 ** BadRequestException **
The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.
HTTP Status Code: 400

 ** ConflictException **
This request can't be completed for one of the following reasons because the requested resource was being concurrently modified by another request.
 ** ResourceId **
The identifier of the AWS resource.
 ** ResourceType **
The resource type, which can be either `Connector` or `Challenge`.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than `ACTIVE`.
 ** ResourceId **
The identifier of the AWS resource.
 ** ResourceType **
The resource type, which can be either `Connector` or `Challenge`.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** QuotaCode **
The quota identifier.
 ** ResourceType **
The resource type, which can be either `Connector` or `Challenge`.
 ** ServiceCode **
Identifies the originating service.
HTTP Status Code: 402

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.
 ** Reason **
The reason for the validation error, if available. The service doesn't return a reason for every validation exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateChallenge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pca-connector-scep-2018-05-10/CreateChallenge)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pca-connector-scep-2018-05-10/CreateChallenge)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/CreateChallenge)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pca-connector-scep-2018-05-10/CreateChallenge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/CreateChallenge)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pca-connector-scep-2018-05-10/CreateChallenge)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pca-connector-scep-2018-05-10/CreateChallenge)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pca-connector-scep-2018-05-10/CreateChallenge)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pca-connector-scep-2018-05-10/CreateChallenge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/CreateChallenge)
