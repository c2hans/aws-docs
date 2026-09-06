---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeRepository.html
---

# DescribeRepository
<a name="API_DescribeRepository"></a>

 Returns a `RepositoryDescription` object that contains detailed information about the requested repository.

## Request Syntax
<a name="API_DescribeRepository_RequestSyntax"></a>

```
GET /v1/repository?domain={{domain}}&domain-owner={{domainOwner}}&repository={{repository}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeRepository_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_DescribeRepository_RequestSyntax) **   <a name="codeartifact-DescribeRepository-request-uri-domain"></a>
 The name of the domain that contains the repository to describe.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_DescribeRepository_RequestSyntax) **   <a name="codeartifact-DescribeRepository-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [repository](#API_DescribeRepository_RequestSyntax) **   <a name="codeartifact-DescribeRepository-request-uri-repository"></a>
 A string that specifies the name of the requested repository.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_DescribeRepository_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeRepository_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "repository": {
      "administratorAccount": "string",
      "arn": "string",
      "createdTime": number,
      "description": "string",
      "domainName": "string",
      "domainOwner": "string",
      "externalConnections": [
         {
            "externalConnectionName": "string",
            "packageFormat": "string",
            "status": "string"
         }
      ],
      "name": "string",
      "upstreams": [
         {
            "repositoryName": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [repository](#API_DescribeRepository_ResponseSyntax) **   <a name="codeartifact-DescribeRepository-response-repository"></a>
 A `RepositoryDescription` object that contains the requested repository information.
Type: [RepositoryDescription](API_RepositoryDescription.md) object

## Errors
<a name="API_DescribeRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The operation did not succeed because of an unauthorized access attempt.
HTTP Status Code: 403

 ** InternalServerException **
 The operation did not succeed because of an error that occurred inside AWS CodeArtifact.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The operation did not succeed because the resource requested is not found in the service.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The operation did not succeed because too many requests are sent to the service.
 ** retryAfterSeconds **
 The time period, in seconds, to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
 The operation did not succeed because a parameter in the request was sent with an invalid value.
 ** reason **

HTTP Status Code: 400

## See Also
<a name="API_DescribeRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/DescribeRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/DescribeRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/DescribeRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/DescribeRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/DescribeRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/DescribeRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/DescribeRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/DescribeRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/DescribeRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/DescribeRepository)
