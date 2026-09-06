---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteRepositoryPermissionsPolicy.html
---

# DeleteRepositoryPermissionsPolicy
<a name="API_DeleteRepositoryPermissionsPolicy"></a>

 Deletes the resource policy that is set on a repository. After a resource policy is deleted, the permissions allowed and denied by the deleted policy are removed. The effect of deleting a resource policy might not be immediate.

**Important**
 Use `DeleteRepositoryPermissionsPolicy` with caution. After a policy is deleted, AWS users, roles, and accounts lose permissions to perform the repository actions granted by the deleted policy.

## Request Syntax
<a name="API_DeleteRepositoryPermissionsPolicy_RequestSyntax"></a>

```
DELETE /v1/repository/permissions/policies?domain={{domain}}&domain-owner={{domainOwner}}&policy-revision={{policyRevision}}&repository={{repository}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRepositoryPermissionsPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_DeleteRepositoryPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-DeleteRepositoryPermissionsPolicy-request-uri-domain"></a>
 The name of the domain that contains the repository associated with the resource policy to be deleted.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_DeleteRepositoryPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-DeleteRepositoryPermissionsPolicy-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [policyRevision](#API_DeleteRepositoryPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-DeleteRepositoryPermissionsPolicy-request-uri-policyRevision"></a>
 The revision of the repository's resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository's resource policy.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `\S+`

 ** [repository](#API_DeleteRepositoryPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-DeleteRepositoryPermissionsPolicy-request-uri-repository"></a>
 The name of the repository that is associated with the resource policy to be deleted
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_DeleteRepositoryPermissionsPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRepositoryPermissionsPolicy_ResponseSyntax"></a>

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
<a name="API_DeleteRepositoryPermissionsPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_DeleteRepositoryPermissionsPolicy_ResponseSyntax) **   <a name="codeartifact-DeleteRepositoryPermissionsPolicy-response-policy"></a>
 Information about the deleted policy after processing the request.
Type: [ResourcePolicy](API_ResourcePolicy.md) object

## Errors
<a name="API_DeleteRepositoryPermissionsPolicy_Errors"></a>

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
<a name="API_DeleteRepositoryPermissionsPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/DeleteRepositoryPermissionsPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/DeleteRepositoryPermissionsPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/DeleteRepositoryPermissionsPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/DeleteRepositoryPermissionsPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/DeleteRepositoryPermissionsPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/DeleteRepositoryPermissionsPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/DeleteRepositoryPermissionsPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/DeleteRepositoryPermissionsPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/DeleteRepositoryPermissionsPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/DeleteRepositoryPermissionsPolicy)
