---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PutDomainPermissionsPolicy.html
---

# PutDomainPermissionsPolicy
<a name="API_PutDomainPermissionsPolicy"></a>

 Sets a resource policy on a domain that specifies permissions to access it.

 When you call `PutDomainPermissionsPolicy`, the resource policy on the domain is ignored when evaluting permissions. This ensures that the owner of a domain cannot lock themselves out of the domain, which would prevent them from being able to update the resource policy.

## Request Syntax
<a name="API_PutDomainPermissionsPolicy_RequestSyntax"></a>

```
PUT /v1/domain/permissions/policy HTTP/1.1
Content-type: application/json

{
   "domain": "{{string}}",
   "domainOwner": "{{string}}",
   "policyDocument": "{{string}}",
   "policyRevision": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutDomainPermissionsPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutDomainPermissionsPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [domain](#API_PutDomainPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-PutDomainPermissionsPolicy-request-domain"></a>
 The name of the domain on which to set the resource policy.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_PutDomainPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-PutDomainPermissionsPolicy-request-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** [policyDocument](#API_PutDomainPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-PutDomainPermissionsPolicy-request-policyDocument"></a>
 A valid displayable JSON Aspen policy string to be set as the access control resource policy on the provided domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7168.
Pattern: `[\P{C}\s]+`
Required: Yes

 ** [policyRevision](#API_PutDomainPermissionsPolicy_RequestSyntax) **   <a name="codeartifact-PutDomainPermissionsPolicy-request-policyRevision"></a>
 The current revision of the resource policy to be set. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain's resource policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_PutDomainPermissionsPolicy_ResponseSyntax"></a>

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
<a name="API_PutDomainPermissionsPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_PutDomainPermissionsPolicy_ResponseSyntax) **   <a name="codeartifact-PutDomainPermissionsPolicy-response-policy"></a>
 The resource policy that was set after processing the request.
Type: [ResourcePolicy](API_ResourcePolicy.md) object

## Errors
<a name="API_PutDomainPermissionsPolicy_Errors"></a>

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
<a name="API_PutDomainPermissionsPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/PutDomainPermissionsPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/PutDomainPermissionsPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PutDomainPermissionsPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/PutDomainPermissionsPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PutDomainPermissionsPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/PutDomainPermissionsPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/PutDomainPermissionsPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/PutDomainPermissionsPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/PutDomainPermissionsPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PutDomainPermissionsPolicy)
