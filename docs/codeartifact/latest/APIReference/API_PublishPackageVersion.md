---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PublishPackageVersion.html
---

# PublishPackageVersion
<a name="API_PublishPackageVersion"></a>

Creates a new package version containing one or more assets (or files).

The `unfinished` flag can be used to keep the package version in the `Unfinished` state until all of its assets have been uploaded (see [Package version status](https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status) in the *CodeArtifact user guide*). To set the package version’s status to `Published`, omit the `unfinished` flag when uploading the final asset, or set the status using [UpdatePackageVersionStatus](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html). Once a package version’s status is set to `Published`, it cannot change back to `Unfinished`.

**Note**
Only generic packages can be published using this API. For more information, see [Using generic packages](https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html) in the * AWS CodeArtifact User Guide*.

## Request Syntax
<a name="API_PublishPackageVersion_RequestSyntax"></a>

```
POST /v1/package/version/publish?asset={{assetName}}&domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&namespace={{namespace}}&package={{package}}&repository={{repository}}&unfinished={{unfinished}}&version={{packageVersion}} HTTP/1.1
x-amz-content-sha256: {{assetSHA256}}

{{assetContent}}
```

## URI Request Parameters
<a name="API_PublishPackageVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetName](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-uri-assetName"></a>
The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: `~ ! @ ^ & ( ) - ` _ + [ ] { } ; , . ``
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\P{C}+`
Required: Yes

 ** [assetSHA256](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-assetSHA256"></a>
The SHA256 hash of the `assetContent` to publish. This value must be calculated by the caller and provided with the request (see [Publishing a generic package](https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages) in the * AWS CodeArtifact User Guide*).
This value is used as an integrity check to verify that the `assetContent` has not changed after it was originally sent.
Length Constraints: Fixed length of 64.
Pattern: `[0-9a-f]+`
Required: Yes

 ** [domain](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-uri-domain"></a>
The name of the domain that contains the repository that contains the package version to publish.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-uri-domainOwner"></a>
The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-uri-format"></a>
A format that specifies the type of the package version with the requested asset file.
Valid Values: `generic`
Required: Yes

 ** [namespace](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-uri-namespace"></a>
The namespace of the package version to publish.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-uri-package"></a>
The name of the package version to publish.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [packageVersion](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-uri-packageVersion"></a>
The package version to publish (for example, `3.5.2`).
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [repository](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-uri-repository"></a>
The name of the repository that the package version will be published to.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

 ** [unfinished](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-uri-unfinished"></a>
Specifies whether the package version should remain in the `unfinished` state. If omitted, the package version status will be set to `Published` (see [Package version status](https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status) in the *CodeArtifact User Guide*).
Valid values: `unfinished`

## Request Body
<a name="API_PublishPackageVersion_RequestBody"></a>

The request accepts the following binary data.

 ** [assetContent](#API_PublishPackageVersion_RequestSyntax) **   <a name="codeartifact-PublishPackageVersion-request-assetContent"></a>
The content of the asset to publish.
Required: Yes

## Response Syntax
<a name="API_PublishPackageVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "asset": {
      "hashes": {
         "string" : "string"
      },
      "name": "string",
      "size": number
   },
   "format": "string",
   "namespace": "string",
   "package": "string",
   "status": "string",
   "version": "string",
   "versionRevision": "string"
}
```

## Response Elements
<a name="API_PublishPackageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [asset](#API_PublishPackageVersion_ResponseSyntax) **   <a name="codeartifact-PublishPackageVersion-response-asset"></a>
An [AssetSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html) for the published asset.
Type: [AssetSummary](API_AssetSummary.md) object

 ** [format](#API_PublishPackageVersion_ResponseSyntax) **   <a name="codeartifact-PublishPackageVersion-response-format"></a>
The format of the package version.
Type: String
Valid Values: `generic`

 ** [namespace](#API_PublishPackageVersion_ResponseSyntax) **   <a name="codeartifact-PublishPackageVersion-response-namespace"></a>
The namespace of the package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_PublishPackageVersion_ResponseSyntax) **   <a name="codeartifact-PublishPackageVersion-response-package"></a>
The name of the package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [status](#API_PublishPackageVersion_ResponseSyntax) **   <a name="codeartifact-PublishPackageVersion-response-status"></a>
A string that contains the status of the package version. For more information, see [Package version status](https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status) in the *CodeArtifact User Guide*.
Type: String
Valid Values: `Published | Unfinished | Unlisted | Archived | Disposed | Deleted`

 ** [version](#API_PublishPackageVersion_ResponseSyntax) **   <a name="codeartifact-PublishPackageVersion-response-version"></a>
The version of the package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [versionRevision](#API_PublishPackageVersion_ResponseSyntax) **   <a name="codeartifact-PublishPackageVersion-response-versionRevision"></a>
The revision of the package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `\S+`

## Errors
<a name="API_PublishPackageVersion_Errors"></a>

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
<a name="API_PublishPackageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/PublishPackageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/PublishPackageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PublishPackageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/PublishPackageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PublishPackageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/PublishPackageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/PublishPackageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/PublishPackageVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/PublishPackageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PublishPackageVersion)
