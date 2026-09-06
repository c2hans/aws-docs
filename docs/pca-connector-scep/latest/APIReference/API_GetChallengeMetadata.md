---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_GetChallengeMetadata.html
---

# GetChallengeMetadata
<a name="API_GetChallengeMetadata"></a>

Retrieves the metadata for the specified [Challenge](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html).

## Request Syntax
<a name="API_GetChallengeMetadata_RequestSyntax"></a>

```
GET /challengeMetadata/{{ChallengeArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetChallengeMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChallengeArn](#API_GetChallengeMetadata_RequestSyntax) **   <a name="pcaconnectorscep-GetChallengeMetadata-request-uri-ChallengeArn"></a>
The Amazon Resource Name (ARN) of the challenge.
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\/challenge\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_GetChallengeMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetChallengeMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChallengeMetadata": {
      "Arn": "string",
      "ConnectorArn": "string",
      "CreatedAt": number,
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_GetChallengeMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChallengeMetadata](#API_GetChallengeMetadata_ResponseSyntax) **   <a name="pcaconnectorscep-GetChallengeMetadata-response-ChallengeMetadata"></a>
The metadata for the challenge.
Type: [ChallengeMetadata](API_ChallengeMetadata.md) object

## Errors
<a name="API_GetChallengeMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your AWS Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an AWS Organizations service control policy (SCP) that affects your AWS account.
HTTP Status Code: 403

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

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.
 ** Reason **
The reason for the validation error, if available. The service doesn't return a reason for every validation exception.
HTTP Status Code: 400

## See Also
<a name="API_GetChallengeMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pca-connector-scep-2018-05-10/GetChallengeMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pca-connector-scep-2018-05-10/GetChallengeMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/GetChallengeMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pca-connector-scep-2018-05-10/GetChallengeMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/GetChallengeMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pca-connector-scep-2018-05-10/GetChallengeMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pca-connector-scep-2018-05-10/GetChallengeMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pca-connector-scep-2018-05-10/GetChallengeMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pca-connector-scep-2018-05-10/GetChallengeMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/GetChallengeMetadata)
