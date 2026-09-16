---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AssociateSbomWithPackageVersion.html
---

# AssociateSbomWithPackageVersion
<a name="API_AssociateSbomWithPackageVersion"></a>

Associates the selected software bill of materials (SBOM) with a specific software package version.

Requires permission to access the [AssociateSbomWithPackageVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_AssociateSbomWithPackageVersion_RequestSyntax"></a>

```
PUT /packages/{{packageName}}/versions/{{versionName}}/sbom?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "sbom": {
      "s3Location": {
         "bucket": "{{string}}",
         "key": "{{string}}",
         "version": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_AssociateSbomWithPackageVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_AssociateSbomWithPackageVersion_RequestSyntax) **   <a name="iot-AssociateSbomWithPackageVersion-request-uri-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

 ** [packageName](#API_AssociateSbomWithPackageVersion_RequestSyntax) **   <a name="iot-AssociateSbomWithPackageVersion-request-uri-packageName"></a>
The name of the new software package.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

 ** [versionName](#API_AssociateSbomWithPackageVersion_RequestSyntax) **   <a name="iot-AssociateSbomWithPackageVersion-request-uri-versionName"></a>
The name of the new package version.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

## Request Body
<a name="API_AssociateSbomWithPackageVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sbom](#API_AssociateSbomWithPackageVersion_RequestSyntax) **   <a name="iot-AssociateSbomWithPackageVersion-request-sbom"></a>
A specific software bill of matrerials associated with a software package version.
Type: [Sbom](API_Sbom.md) object
Required: Yes

## Response Syntax
<a name="API_AssociateSbomWithPackageVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "packageName": "string",
   "sbom": {
      "s3Location": {
         "bucket": "string",
         "key": "string",
         "version": "string"
      }
   },
   "sbomValidationStatus": "string",
   "versionName": "string"
}
```

## Response Elements
<a name="API_AssociateSbomWithPackageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [packageName](#API_AssociateSbomWithPackageVersion_ResponseSyntax) **   <a name="iot-AssociateSbomWithPackageVersion-response-packageName"></a>
The name of the new software package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`

 ** [sbom](#API_AssociateSbomWithPackageVersion_ResponseSyntax) **   <a name="iot-AssociateSbomWithPackageVersion-response-sbom"></a>
A specific software bill of matrerials associated with a software package version.
Type: [Sbom](API_Sbom.md) object

 ** [sbomValidationStatus](#API_AssociateSbomWithPackageVersion_ResponseSyntax) **   <a name="iot-AssociateSbomWithPackageVersion-response-sbomValidationStatus"></a>
The status of the initial validation for the software bill of materials against the Software Package Data Exchange (SPDX) and CycloneDX industry standard formats.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED`

 ** [versionName](#API_AssociateSbomWithPackageVersion_ResponseSyntax) **   <a name="iot-AssociateSbomWithPackageVersion-response-versionName"></a>
The name of the new package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`

## Errors
<a name="API_AssociateSbomWithPackageVersion_Errors"></a>

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

 ** ServiceQuotaExceededException **
Service quota has been exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_AssociateSbomWithPackageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/AssociateSbomWithPackageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/AssociateSbomWithPackageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AssociateSbomWithPackageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/AssociateSbomWithPackageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AssociateSbomWithPackageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/AssociateSbomWithPackageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/AssociateSbomWithPackageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/AssociateSbomWithPackageVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/AssociateSbomWithPackageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AssociateSbomWithPackageVersion)
