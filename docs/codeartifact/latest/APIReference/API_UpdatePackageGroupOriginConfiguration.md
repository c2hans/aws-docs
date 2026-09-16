---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageGroupOriginConfiguration.html
---

# UpdatePackageGroupOriginConfiguration
<a name="API_UpdatePackageGroupOriginConfiguration"></a>

Updates the package origin configuration for a package group.

The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package group origin controls and configuration, see [Package group origin controls](https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-origin-controls.html) in the *CodeArtifact User Guide*.

## Request Syntax
<a name="API_UpdatePackageGroupOriginConfiguration_RequestSyntax"></a>

```
PUT /v1/package-group-origin-configuration?domain={{domain}}&domain-owner={{domainOwner}}&package-group={{packageGroup}} HTTP/1.1
Content-type: application/json

{
   "addAllowedRepositories": [
      {
         "originRestrictionType": "{{string}}",
         "repositoryName": "{{string}}"
      }
   ],
   "removeAllowedRepositories": [
      {
         "originRestrictionType": "{{string}}",
         "repositoryName": "{{string}}"
      }
   ],
   "restrictions": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdatePackageGroupOriginConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_UpdatePackageGroupOriginConfiguration_RequestSyntax) **   <a name="codeartifact-UpdatePackageGroupOriginConfiguration-request-uri-domain"></a>
 The name of the domain which contains the package group for which to update the origin configuration.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_UpdatePackageGroupOriginConfiguration_RequestSyntax) **   <a name="codeartifact-UpdatePackageGroupOriginConfiguration-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [packageGroup](#API_UpdatePackageGroupOriginConfiguration_RequestSyntax) **   <a name="codeartifact-UpdatePackageGroupOriginConfiguration-request-uri-packageGroup"></a>
 The pattern of the package group for which to update the origin configuration.
Length Constraints: Minimum length of 2. Maximum length of 520.
Pattern: `[^\p{C}\p{IsWhitespace}]+`
Required: Yes

## Request Body
<a name="API_UpdatePackageGroupOriginConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [addAllowedRepositories](#API_UpdatePackageGroupOriginConfiguration_RequestSyntax) **   <a name="codeartifact-UpdatePackageGroupOriginConfiguration-request-addAllowedRepositories"></a>
The repository name and restrictions to add to the allowed repository list of the specified package group.
Type: Array of [PackageGroupAllowedRepository](API_PackageGroupAllowedRepository.md) objects
Required: No

 ** [removeAllowedRepositories](#API_UpdatePackageGroupOriginConfiguration_RequestSyntax) **   <a name="codeartifact-UpdatePackageGroupOriginConfiguration-request-removeAllowedRepositories"></a>
The repository name and restrictions to remove from the allowed repository list of the specified package group.
Type: Array of [PackageGroupAllowedRepository](API_PackageGroupAllowedRepository.md) objects
Required: No

 ** [restrictions](#API_UpdatePackageGroupOriginConfiguration_RequestSyntax) **   <a name="codeartifact-UpdatePackageGroupOriginConfiguration-request-restrictions"></a>
 The origin configuration settings that determine how package versions can enter repositories.
Type: String to string map
Valid Keys: `EXTERNAL_UPSTREAM | INTERNAL_UPSTREAM | PUBLISH`
Valid Values: `ALLOW | ALLOW_SPECIFIC_REPOSITORIES | BLOCK | INHERIT`
Required: No

## Response Syntax
<a name="API_UpdatePackageGroupOriginConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "allowedRepositoryUpdates": {
      "string" : {
         "string" : [ "string" ]
      }
   },
   "packageGroup": {
      "arn": "string",
      "contactInfo": "string",
      "createdTime": number,
      "description": "string",
      "domainName": "string",
      "domainOwner": "string",
      "originConfiguration": {
         "restrictions": {
            "string" : {
               "effectiveMode": "string",
               "inheritedFrom": {
                  "arn": "string",
                  "pattern": "string"
               },
               "mode": "string",
               "repositoriesCount": number
            }
         }
      },
      "parent": {
         "arn": "string",
         "pattern": "string"
      },
      "pattern": "string"
   }
}
```

## Response Elements
<a name="API_UpdatePackageGroupOriginConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowedRepositoryUpdates](#API_UpdatePackageGroupOriginConfiguration_ResponseSyntax) **   <a name="codeartifact-UpdatePackageGroupOriginConfiguration-response-allowedRepositoryUpdates"></a>
Information about the updated allowed repositories after processing the request.
Type: String to string to array of strings map map
Valid Keys: `EXTERNAL_UPSTREAM | INTERNAL_UPSTREAM | PUBLISH`
Valid Keys: `ADDED | REMOVED`
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`

 ** [packageGroup](#API_UpdatePackageGroupOriginConfiguration_ResponseSyntax) **   <a name="codeartifact-UpdatePackageGroupOriginConfiguration-response-packageGroup"></a>
 The package group and information about it after processing the request.
Type: [PackageGroupDescription](API_PackageGroupDescription.md) object

## Errors
<a name="API_UpdatePackageGroupOriginConfiguration_Errors"></a>

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
<a name="API_UpdatePackageGroupOriginConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)
