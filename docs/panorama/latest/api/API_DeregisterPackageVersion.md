---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_DeregisterPackageVersion.html
---

# DeregisterPackageVersion
<a name="API_DeregisterPackageVersion"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Deregisters a package version.

## Request Syntax
<a name="API_DeregisterPackageVersion_RequestSyntax"></a>

```
DELETE /packages/{{PackageId}}/versions/{{PackageVersion}}/patch/{{PatchVersion}}?OwnerAccount={{OwnerAccount}}&UpdatedLatestPatchVersion={{UpdatedLatestPatchVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeregisterPackageVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [OwnerAccount](#API_DeregisterPackageVersion_RequestSyntax) **   <a name="panorama-DeregisterPackageVersion-request-uri-OwnerAccount"></a>
An owner account.
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9a-z\_]+`

 ** [PackageId](#API_DeregisterPackageVersion_RequestSyntax) **   <a name="panorama-DeregisterPackageVersion-request-uri-PackageId"></a>
A package ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\/]+`
Required: Yes

 ** [PackageVersion](#API_DeregisterPackageVersion_RequestSyntax) **   <a name="panorama-DeregisterPackageVersion-request-uri-PackageVersion"></a>
A package version.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([0-9]+)\.([0-9]+)`
Required: Yes

 ** [PatchVersion](#API_DeregisterPackageVersion_RequestSyntax) **   <a name="panorama-DeregisterPackageVersion-request-uri-PatchVersion"></a>
A patch version.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9]+`
Required: Yes

 ** [UpdatedLatestPatchVersion](#API_DeregisterPackageVersion_RequestSyntax) **   <a name="panorama-DeregisterPackageVersion-request-uri-UpdatedLatestPatchVersion"></a>
If the version was marked latest, the new version to maker as latest.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9]+`

## Request Body
<a name="API_DeregisterPackageVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeregisterPackageVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeregisterPackageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeregisterPackageVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** ConflictException **
The target resource is in use.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 404

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_DeregisterPackageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/DeregisterPackageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/DeregisterPackageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/DeregisterPackageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/DeregisterPackageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/DeregisterPackageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/DeregisterPackageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/DeregisterPackageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/DeregisterPackageVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/DeregisterPackageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/DeregisterPackageVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
