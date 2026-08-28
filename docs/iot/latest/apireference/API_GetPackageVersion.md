---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetPackageVersion.html
---

# GetPackageVersion
<a name="API_GetPackageVersion"></a>

Gets information about the specified package version.

Requires permission to access the [GetPackageVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetPackageVersion_RequestSyntax"></a>

```
GET /packages/{{packageName}}/versions/{{versionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPackageVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [packageName](#API_GetPackageVersion_RequestSyntax) **   <a name="iot-GetPackageVersion-request-uri-packageName"></a>
The name of the associated package.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

 ** [versionName](#API_GetPackageVersion_RequestSyntax) **   <a name="iot-GetPackageVersion-request-uri-versionName"></a>
The name of the target package version.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

## Request Body
<a name="API_GetPackageVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPackageVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "artifact": {
      "s3Location": {
         "bucket": "string",
         "key": "string",
         "version": "string"
      }
   },
   "attributes": {
      "string" : "string"
   },
   "creationDate": number,
   "description": "string",
   "errorReason": "string",
   "lastModifiedDate": number,
   "packageName": "string",
   "packageVersionArn": "string",
   "recipe": "string",
   "sbom": {
      "s3Location": {
         "bucket": "string",
         "key": "string",
         "version": "string"
      }
   },
   "sbomValidationStatus": "string",
   "status": "string",
   "versionName": "string"
}
```

## Response Elements
<a name="API_GetPackageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [artifact](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-artifact"></a>
The various components that make up a software package version.
Type: [PackageVersionArtifact](API_PackageVersionArtifact.md) object

 ** [attributes](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-attributes"></a>
Metadata that were added to the package version that can be used to define a package version’s configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Minimum length of 1.
Value Pattern: `[^\p{C}]+`

 ** [creationDate](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-creationDate"></a>
The date when the package version was created.
Type: Timestamp

 ** [description](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-description"></a>
The package version description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\p{C}]+`

 ** [errorReason](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-errorReason"></a>
Error reason for a package version failure during creation or update.
Type: String

 ** [lastModifiedDate](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-lastModifiedDate"></a>
The date when the package version was last updated.
Type: Timestamp

 ** [packageName](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-packageName"></a>
The name of the software package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`

 ** [packageVersionArn](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-packageVersionArn"></a>
The ARN for the package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`

 ** [recipe](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-recipe"></a>
The inline job document associated with a software package version used for a quick job deployment.
Type: String
Length Constraints: Maximum length of 3072.

 ** [sbom](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-sbom"></a>
The software bill of materials for a software package version.
Type: [Sbom](API_Sbom.md) object

 ** [sbomValidationStatus](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-sbomValidationStatus"></a>
The status of the validation for a new software bill of materials added to a software package version.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED`

 ** [status](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-status"></a>
The status associated to the package version. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).
Type: String
Valid Values: `DRAFT | PUBLISHED | DEPRECATED`

 ** [versionName](#API_GetPackageVersion_ResponseSyntax) **   <a name="iot-GetPackageVersion-response-versionName"></a>
The name of the package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`

## Errors
<a name="API_GetPackageVersion_Errors"></a>

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetPackageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetPackageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetPackageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetPackageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetPackageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetPackageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetPackageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetPackageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetPackageVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetPackageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetPackageVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
