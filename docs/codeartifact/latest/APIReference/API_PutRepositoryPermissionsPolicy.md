---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PutRepositoryPermissionsPolicy.html
---

# PutRepositoryPermissionsPolicy
<a name="API_PutRepositoryPermissionsPolicy"></a>

 Sets the resource policy on a repository that specifies permissions to access it.

 When you call `PutRepositoryPermissionsPolicy`, the resource policy on the repository is ignored when evaluting permissions. This ensures that the owner of a repository cannot lock themselves out of the repository, which would prevent them from being able to update the resource policy.

## Request Syntax
<a name="API_PutRepositoryPermissionsPolicy_RequestSyntax"></a>

```
PUT /v1/repository/permissions/policy?domain={{domain}}&domain-owner={{domainOwner}}&repository={{repository}} HTTP/1.1
Content-type: application/json

{
   "policyDocument": "{{string}}",
   "policyRevision": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutRepositoryPermissionsPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_PutRepositoryPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-PutRepositoryPermissionsPolicy-request-uri-domain"></a>
 The name of the domain containing the repository to set the resource policy on.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_PutRepositoryPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-PutRepositoryPermissionsPolicy-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [repository](#API_PutRepositoryPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-PutRepositoryPermissionsPolicy-request-uri-repository"></a>
 The name of the repository to set the resource policy on.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_PutRepositoryPermissionsPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policyDocument](#API_PutRepositoryPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-PutRepositoryPermissionsPolicy-request-policyDocument"></a>
 A valid displayable JSON Aspen policy string to be set as the access control resource policy on the provided repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7168.
Pattern: `[\P{C}\s]+`
Required: Yes

 ** [policyRevision](#API_PutRepositoryPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-PutRepositoryPermissionsPolicy-request-policyRevision"></a>
 Sets the revision of the resource policy that specifies permissions to access the repository. This revision is used for optimistic locking, which prevents others from overwriting your changes to the repository's resource policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_PutRepositoryPermissionsPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": {
      "document": "string",
      "resourceArn": "string",
      "revision": "string"
   }
}
```

## Response Elements
<a name="API_PutRepositoryPermissionsPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_PutRepositoryPermissionsPolicy_ResponseSyntax) **   <a name="codeartifact-PutRepositoryPermissionsPolicy-response-policy"></a>
 The resource policy that was set after processing the request.
Type: [ResourcePolicy](API_ResourcePolicy.md) object

## Errors
<a name="API_PutRepositoryPermissionsPolicy_Errors"></a>

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
<a name="API_PutRepositoryPermissionsPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/PutRepositoryPermissionsPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/PutRepositoryPermissionsPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PutRepositoryPermissionsPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/PutRepositoryPermissionsPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PutRepositoryPermissionsPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/PutRepositoryPermissionsPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/PutRepositoryPermissionsPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/PutRepositoryPermissionsPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/PutRepositoryPermissionsPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PutRepositoryPermissionsPolicy)
