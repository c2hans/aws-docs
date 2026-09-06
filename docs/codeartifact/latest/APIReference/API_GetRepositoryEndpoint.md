---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetRepositoryEndpoint.html
---

# GetRepositoryEndpoint
<a name="API_GetRepositoryEndpoint"></a>

 Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format:
+  `cargo`
+  `generic`
+  `maven`
+  `npm`
+  `nuget`
+  `pypi`
+  `ruby`
+  `swift`

## Request Syntax
<a name="API_GetRepositoryEndpoint_RequestSyntax"></a>

```
GET /v1/repository/endpoint?domain={{domain}}&domain-owner={{domainOwner}}&endpointType={{endpointType}}&format={{format}}&repository={{repository}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRepositoryEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_GetRepositoryEndpoint_RequestSyntax) **   <a name="codeartifact-GetRepositoryEndpoint-request-uri-domain"></a>
 The name of the domain that contains the repository.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_GetRepositoryEndpoint_RequestSyntax) **   <a name="codeartifact-GetRepositoryEndpoint-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain that contains the repository. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [endpointType](#API_GetRepositoryEndpoint_RequestSyntax) **   <a name="codeartifact-GetRepositoryEndpoint-request-uri-endpointType"></a>
A string that specifies the type of endpoint.
Valid Values: `dualstack | ipv4`

 ** [format](#API_GetRepositoryEndpoint_RequestSyntax) **   <a name="codeartifact-GetRepositoryEndpoint-request-uri-format"></a>
 Returns which endpoint of a repository to return. A repository has one endpoint for each package format.
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: Yes

 ** [repository](#API_GetRepositoryEndpoint_RequestSyntax) **   <a name="codeartifact-GetRepositoryEndpoint-request-uri-repository"></a>
 The name of the repository.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_GetRepositoryEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRepositoryEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "repositoryEndpoint": "string"
}
```

## Response Elements
<a name="API_GetRepositoryEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [repositoryEndpoint](#API_GetRepositoryEndpoint_ResponseSyntax) **   <a name="codeartifact-GetRepositoryEndpoint-response-repositoryEndpoint"></a>
 A string that specifies the URL of the returned endpoint.
Type: String

## Errors
<a name="API_GetRepositoryEndpoint_Errors"></a>

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
<a name="API_GetRepositoryEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/GetRepositoryEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/GetRepositoryEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/GetRepositoryEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/GetRepositoryEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/GetRepositoryEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/GetRepositoryEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/GetRepositoryEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/GetRepositoryEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/GetRepositoryEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/GetRepositoryEndpoint)
