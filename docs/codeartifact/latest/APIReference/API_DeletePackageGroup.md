---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageGroup.html
---

# DeletePackageGroup
<a name="API_DeletePackageGroup"></a>

Deletes a package group. Deleting a package group does not delete packages or package versions associated with the package group. When a package group is deleted, the direct child package groups will become children of the package group's direct parent package group. Therefore, if any of the child groups are inheriting any settings from the parent, those settings could change.

## Request Syntax
<a name="API_DeletePackageGroup_RequestSyntax"></a>

```
DELETE /v1/package-group?domain={{domain}}&domain-owner={{domainOwner}}&package-group={{packageGroup}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePackageGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_DeletePackageGroup_RequestSyntax) **   <a name="codeartifact-DeletePackageGroup-request-uri-domain"></a>
 The domain that contains the package group to be deleted.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_DeletePackageGroup_RequestSyntax) **   <a name="codeartifact-DeletePackageGroup-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [packageGroup](#API_DeletePackageGroup_RequestSyntax) **   <a name="codeartifact-DeletePackageGroup-request-uri-packageGroup"></a>
The pattern of the package group to be deleted.
Required: Yes

## Request Body
<a name="API_DeletePackageGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePackageGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
<a name="API_DeletePackageGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [packageGroup](#API_DeletePackageGroup_ResponseSyntax) **   <a name="codeartifact-DeletePackageGroup-response-packageGroup"></a>
 Information about the deleted package group after processing the request.
Type: [PackageGroupDescription](API_PackageGroupDescription.md) object

## Errors
<a name="API_DeletePackageGroup_Errors"></a>

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
<a name="API_DeletePackageGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/DeletePackageGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/DeletePackageGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/DeletePackageGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/DeletePackageGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/DeletePackageGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/DeletePackageGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/DeletePackageGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/DeletePackageGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/DeletePackageGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/DeletePackageGroup)
