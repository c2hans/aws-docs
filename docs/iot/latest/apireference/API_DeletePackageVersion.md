---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePackageVersion.html
---

# DeletePackageVersion
<a name="API_DeletePackageVersion"></a>

Deletes a specific version from a software package.

 **Note:** If a package version is designated as default, you must remove the designation from the software package using the [UpdatePackage](API_UpdatePackage.md) action.

## Request Syntax
<a name="API_DeletePackageVersion_RequestSyntax"></a>

```
DELETE /packages/{{packageName}}/versions/{{versionName}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePackageVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeletePackageVersion_RequestSyntax) **   <a name="iot-DeletePackageVersion-request-uri-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

 ** [packageName](#API_DeletePackageVersion_RequestSyntax) **   <a name="iot-DeletePackageVersion-request-uri-packageName"></a>
The name of the associated software package.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

 ** [versionName](#API_DeletePackageVersion_RequestSyntax) **   <a name="iot-DeletePackageVersion-request-uri-versionName"></a>
The name of the target package version.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

## Request Body
<a name="API_DeletePackageVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePackageVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeletePackageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePackageVersion_Errors"></a>

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeletePackageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeletePackageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeletePackageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeletePackageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeletePackageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeletePackageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeletePackageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeletePackageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeletePackageVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeletePackageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeletePackageVersion)
