---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageConfiguration.html
---

# UpdatePackageConfiguration
<a name="API_UpdatePackageConfiguration"></a>

Updates the software package configuration.

Requires permission to access the [UpdatePackageConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) and [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) actions.

## Request Syntax
<a name="API_UpdatePackageConfiguration_RequestSyntax"></a>

```
PATCH /package-configuration?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "versionUpdateByJobsConfig": {
      "enabled": {{boolean}},
      "roleArn": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdatePackageConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_UpdatePackageConfiguration_RequestSyntax) **   <a name="iot-UpdatePackageConfiguration-request-uri-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

## Request Body
<a name="API_UpdatePackageConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [versionUpdateByJobsConfig](#API_UpdatePackageConfiguration_RequestSyntax) **   <a name="iot-UpdatePackageConfiguration-request-versionUpdateByJobsConfig"></a>
Configuration to manage job's package version reporting. This updates the thing's reserved named shadow that the job targets.
Type: [VersionUpdateByJobsConfig](API_VersionUpdateByJobsConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdatePackageConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdatePackageConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdatePackageConfiguration_Errors"></a>

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
A resource with the same name already exists.
HTTP Status Code: 409

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
<a name="API_UpdatePackageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdatePackageConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdatePackageConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdatePackageConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdatePackageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdatePackageConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdatePackageConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdatePackageConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdatePackageConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdatePackageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdatePackageConfiguration)
