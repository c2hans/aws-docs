---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateRepository.html
---

# CreateRepository
<a name="API_CreateRepository"></a>

 Creates a repository.

## Request Syntax
<a name="API_CreateRepository_RequestSyntax"></a>

```
POST /v1/repository?domain={{domain}}&domain-owner={{domainOwner}}&repository={{repository}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "upstreams": [
      {
         "repositoryName": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateRepository_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_CreateRepository_RequestSyntax) **   <a name="codeartifact-CreateRepository-request-uri-domain"></a>
 The name of the domain that contains the created repository.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_CreateRepository_RequestSyntax) **   <a name="codeartifact-CreateRepository-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [repository](#API_CreateRepository_RequestSyntax) **   <a name="codeartifact-CreateRepository-request-uri-repository"></a>
The name of the repository to create.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_CreateRepository_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateRepository_RequestSyntax) **   <a name="codeartifact-CreateRepository-request-description"></a>
 A description of the created repository.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** [tags](#API_CreateRepository_RequestSyntax) **   <a name="codeartifact-CreateRepository-request-tags"></a>
One or more tag key-value pairs for the repository.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [upstreams](#API_CreateRepository_RequestSyntax) **   <a name="codeartifact-CreateRepository-request-upstreams"></a>
 A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when AWS CodeArtifact looks for a requested package version. For more information, see [Working with upstream repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html).
Type: Array of [UpstreamRepository](API_UpstreamRepository.md) objects
Required: No

## Response Syntax
<a name="API_CreateRepository_ResponseSyntax"></a>

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
<a name="API_CreateRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [repository](#API_CreateRepository_ResponseSyntax) **   <a name="codeartifact-CreateRepository-response-repository"></a>
 Information about the created repository after processing the request.
Type: [RepositoryDescription](API_RepositoryDescription.md) object

## Errors
<a name="API_CreateRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The operation did not succeed because of an unauthorized access attempt.
HTTP Status Code: 403

 ** ConflictException **
 The operation did not succeed because prerequisites are not met.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
 The operation did not succeed because it would have exceeded a service limit for your account.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
HTTP Status Code: 402

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
<a name="API_CreateRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/CreateRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/CreateRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/CreateRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/CreateRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/CreateRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/CreateRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/CreateRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/CreateRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/CreateRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/CreateRepository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
