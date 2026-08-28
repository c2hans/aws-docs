---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssociateExternalConnection.html
---

# AssociateExternalConnection
<a name="API_AssociateExternalConnection"></a>

Adds an existing external connection to a repository. One external connection is allowed per repository.

**Note**
A repository can have one or more upstream repositories, or an external connection.

## Request Syntax
<a name="API_AssociateExternalConnection_RequestSyntax"></a>

```
POST /v1/repository/external-connection?domain={{domain}}&domain-owner={{domainOwner}}&external-connection={{externalConnection}}&repository={{repository}} HTTP/1.1
```

## URI Request Parameters
<a name="API_AssociateExternalConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_AssociateExternalConnection_RequestSyntax) **   <a name="codeartifact-AssociateExternalConnection-request-uri-domain"></a>
The name of the domain that contains the repository.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_AssociateExternalConnection_RequestSyntax) **   <a name="codeartifact-AssociateExternalConnection-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [externalConnection](#API_AssociateExternalConnection_RequestSyntax) **   <a name="codeartifact-AssociateExternalConnection-request-uri-externalConnection"></a>
 The name of the external connection to add to the repository. The following values are supported:
+  `public:npmjs` - for the npm public repository.
+  `public:nuget-org` - for the NuGet Gallery.
+  `public:pypi` - for the Python Package Index.
+  `public:maven-central` - for Maven Central.
+  `public:maven-googleandroid` - for the Google Android repository.
+  `public:maven-gradleplugins` - for the Gradle plugins repository.
+  `public:maven-commonsware` - for the CommonsWare Android repository.
+  `public:maven-clojars` - for the Clojars repository.
+  `public:ruby-gems-org` - for RubyGems.org.
+  `public:crates-io` - for Crates.io.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-:]{1,99}`
Required: Yes

 ** [repository](#API_AssociateExternalConnection_RequestSyntax) **   <a name="codeartifact-AssociateExternalConnection-request-uri-repository"></a>
 The name of the repository to which the external connection is added.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_AssociateExternalConnection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_AssociateExternalConnection_ResponseSyntax"></a>

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
<a name="API_AssociateExternalConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [repository](#API_AssociateExternalConnection_ResponseSyntax) **   <a name="codeartifact-AssociateExternalConnection-response-repository"></a>
 Information about the connected repository after processing the request.
Type: [RepositoryDescription](API_RepositoryDescription.md) object

## Errors
<a name="API_AssociateExternalConnection_Errors"></a>

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
<a name="API_AssociateExternalConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/AssociateExternalConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/AssociateExternalConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/AssociateExternalConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/AssociateExternalConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/AssociateExternalConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/AssociateExternalConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/AssociateExternalConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/AssociateExternalConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/AssociateExternalConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/AssociateExternalConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
