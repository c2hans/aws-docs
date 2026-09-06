---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListChallengeMetadata.html
---

# ListChallengeMetadata
<a name="API_ListChallengeMetadata"></a>

Retrieves the challenge metadata for the specified ARN.

## Request Syntax
<a name="API_ListChallengeMetadata_RequestSyntax"></a>

```
GET /challengeMetadata?ConnectorArn={{ConnectorArn}}&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListChallengeMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectorArn](#API_ListChallengeMetadata_RequestSyntax) **   <a name="pcaconnectorscep-ListChallengeMetadata-request-uri-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connector.
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: Yes

 ** [MaxResults](#API_ListChallengeMetadata_RequestSyntax) **   <a name="pcaconnectorscep-ListChallengeMetadata-request-uri-MaxResults"></a>
The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListChallengeMetadata_RequestSyntax) **   <a name="pcaconnectorscep-ListChallengeMetadata-request-uri-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:[A-Za-z0-9_-]{4})*(?:[A-Za-z0-9_-]{2}==|[A-Za-z0-9_-]{3}=)?`

## Request Body
<a name="API_ListChallengeMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListChallengeMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Challenges": [
      {
         "Arn": "string",
         "ConnectorArn": "string",
         "CreatedAt": number,
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListChallengeMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Challenges](#API_ListChallengeMetadata_ResponseSyntax) **   <a name="pcaconnectorscep-ListChallengeMetadata-response-Challenges"></a>
The challenge metadata for the challenges belonging to your AWS account.
Type: Array of [ChallengeMetadataSummary](API_ChallengeMetadataSummary.md) objects

 ** [NextToken](#API_ListChallengeMetadata_ResponseSyntax) **   <a name="pcaconnectorscep-ListChallengeMetadata-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:[A-Za-z0-9_-]{4})*(?:[A-Za-z0-9_-]{2}==|[A-Za-z0-9_-]{3}=)?`

## Errors
<a name="API_ListChallengeMetadata_Errors"></a>

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
<a name="API_ListChallengeMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pca-connector-scep-2018-05-10/ListChallengeMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pca-connector-scep-2018-05-10/ListChallengeMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/ListChallengeMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pca-connector-scep-2018-05-10/ListChallengeMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/ListChallengeMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pca-connector-scep-2018-05-10/ListChallengeMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pca-connector-scep-2018-05-10/ListChallengeMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pca-connector-scep-2018-05-10/ListChallengeMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pca-connector-scep-2018-05-10/ListChallengeMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/ListChallengeMetadata)
