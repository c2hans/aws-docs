---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageVersion.html
---

# UpdatePackageVersion
<a name="API_UpdatePackageVersion"></a>

Updates the supported fields for a specific package version.

Requires permission to access the [UpdatePackageVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) and [GetIndexingConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) actions.

## Request Syntax
<a name="API_UpdatePackageVersion_RequestSyntax"></a>

```
PATCH /packages/{{packageName}}/versions/{{versionName}}?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}",
   "artifact": {
      "s3Location": {
         "bucket": "{{string}}",
         "key": "{{string}}",
         "version": "{{string}}"
      }
   },
   "attributes": {
      "{{string}}" : "{{string}}"
   },
   "description": "{{string}}",
   "recipe": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePackageVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_UpdatePackageVersion_RequestSyntax) **   <a name="iot-UpdatePackageVersion-request-uri-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

 ** [packageName](#API_UpdatePackageVersion_RequestSyntax) **   <a name="iot-UpdatePackageVersion-request-uri-packageName"></a>
The name of the associated software package.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

 ** [versionName](#API_UpdatePackageVersion_RequestSyntax) **   <a name="iot-UpdatePackageVersion-request-uri-versionName"></a>
The name of the target package version.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

## Request Body
<a name="API_UpdatePackageVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_UpdatePackageVersion_RequestSyntax) **   <a name="iot-UpdatePackageVersion-request-action"></a>
The status that the package version should be assigned. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).
Type: String
Valid Values: `PUBLISH | DEPRECATE`
Required: No

 ** [artifact](#API_UpdatePackageVersion_RequestSyntax) **   <a name="iot-UpdatePackageVersion-request-artifact"></a>
The various components that make up a software package version.
Type: [PackageVersionArtifact](API_PackageVersionArtifact.md) object
Required: No

 ** [attributes](#API_UpdatePackageVersion_RequestSyntax) **   <a name="iot-UpdatePackageVersion-request-attributes"></a>
Metadata that can be used to define a package version’s configuration. For example, the Amazon S3 file location, configuration options that are being sent to the device or fleet.
 **Note:** Attributes can be updated only when the package version is in a draft state.
The combined size of all the attributes on a package version is limited to 3KB.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Minimum length of 1.
Value Pattern: `[^\p{C}]+`
Required: No

 ** [description](#API_UpdatePackageVersion_RequestSyntax) **   <a name="iot-UpdatePackageVersion-request-description"></a>
The package version description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\p{C}]+`
Required: No

 ** [recipe](#API_UpdatePackageVersion_RequestSyntax) **   <a name="iot-UpdatePackageVersion-request-recipe"></a>
The inline job document associated with a software package version used for a quick job deployment.
Type: String
Length Constraints: Maximum length of 3072.
Required: No

## Response Syntax
<a name="API_UpdatePackageVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdatePackageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdatePackageVersion_Errors"></a>

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
A resource with the same name already exists.
HTTP Status Code: 409

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
<a name="API_UpdatePackageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdatePackageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdatePackageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdatePackageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdatePackageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdatePackageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdatePackageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdatePackageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdatePackageVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdatePackageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdatePackageVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
