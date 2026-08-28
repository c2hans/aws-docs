---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_UpdateDeviceMetadata.html
---

# UpdateDeviceMetadata
<a name="API_UpdateDeviceMetadata"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Updates a device's metadata.

## Request Syntax
<a name="API_UpdateDeviceMetadata_RequestSyntax"></a>

```
PUT /devices/{{DeviceId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDeviceMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeviceId](#API_UpdateDeviceMetadata_RequestSyntax) **   <a name="panorama-UpdateDeviceMetadata-request-uri-DeviceId"></a>
The device's ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

## Request Body
<a name="API_UpdateDeviceMetadata_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateDeviceMetadata_RequestSyntax) **   <a name="panorama-UpdateDeviceMetadata-request-Description"></a>
A description for the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_UpdateDeviceMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DeviceId": "string"
}
```

## Response Elements
<a name="API_UpdateDeviceMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeviceId](#API_UpdateDeviceMetadata_ResponseSyntax) **   <a name="panorama-UpdateDeviceMetadata-response-DeviceId"></a>
The device's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

## Errors
<a name="API_UpdateDeviceMetadata_Errors"></a>

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
<a name="API_UpdateDeviceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/UpdateDeviceMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/UpdateDeviceMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/UpdateDeviceMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/UpdateDeviceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/UpdateDeviceMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/UpdateDeviceMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/UpdateDeviceMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/UpdateDeviceMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/UpdateDeviceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/UpdateDeviceMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
