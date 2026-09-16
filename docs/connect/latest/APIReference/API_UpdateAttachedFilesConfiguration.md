---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateAttachedFilesConfiguration.html
---

# UpdateAttachedFilesConfiguration
<a name="API_UpdateAttachedFilesConfiguration"></a>

Updates the attached files configuration for the specified Connect Customer instance and attachment scope.

If no instance-specific configuration exists, this operation creates one. Partial updates are supported—only specified fields are updated, while unspecified fields retain their current values.

## Request Syntax
<a name="API_UpdateAttachedFilesConfiguration_RequestSyntax"></a>

```
POST /attached-files-configurations/{{InstanceId}}/{{AttachmentScope}} HTTP/1.1
Content-type: application/json

{
   "ExtensionConfiguration": {
      "AllowedExtensions": [
         {
            "Extension": "{{string}}"
         }
      ]
   },
   "MaximumSizeLimitInBytes": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateAttachedFilesConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttachmentScope](#API_UpdateAttachedFilesConfiguration_RequestSyntax) **   <a name="connect-UpdateAttachedFilesConfiguration-request-uri-AttachmentScope"></a>
The scope of the attachment. Valid values are `EMAIL`, `CHAT`, `CASE`, and `TASK`.
Valid Values: `EMAIL | CHAT | CASE | TASK`
Required: Yes

 ** [InstanceId](#API_UpdateAttachedFilesConfiguration_RequestSyntax) **   <a name="connect-UpdateAttachedFilesConfiguration-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateAttachedFilesConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExtensionConfiguration](#API_UpdateAttachedFilesConfiguration_RequestSyntax) **   <a name="connect-UpdateAttachedFilesConfiguration-request-ExtensionConfiguration"></a>
The configuration for allowed file extensions.
Type: [ExtensionConfiguration](API_ExtensionConfiguration.md) object
Required: No

 ** [MaximumSizeLimitInBytes](#API_UpdateAttachedFilesConfiguration_RequestSyntax) **   <a name="connect-UpdateAttachedFilesConfiguration-request-MaximumSizeLimitInBytes"></a>
The maximum size limit for attached files in bytes. The minimum value is 1 and the maximum value is 104857600 (100 MB).
Type: Long
Valid Range: Minimum value of 1. Maximum value of 104857600.
Required: No

## Response Syntax
<a name="API_UpdateAttachedFilesConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttachmentScope": "string",
   "ExtensionConfiguration": {
      "AllowedExtensions": [
         {
            "Extension": "string"
         }
      ]
   },
   "InstanceId": "string",
   "LastModifiedTime": number,
   "MaximumSizeLimitInBytes": number
}
```

## Response Elements
<a name="API_UpdateAttachedFilesConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentScope](#API_UpdateAttachedFilesConfiguration_ResponseSyntax) **   <a name="connect-UpdateAttachedFilesConfiguration-response-AttachmentScope"></a>
The scope of the attachment.
Type: String
Valid Values: `EMAIL | CHAT | CASE | TASK`

 ** [ExtensionConfiguration](#API_UpdateAttachedFilesConfiguration_ResponseSyntax) **   <a name="connect-UpdateAttachedFilesConfiguration-response-ExtensionConfiguration"></a>
The configuration for allowed file extensions.
Type: [ExtensionConfiguration](API_ExtensionConfiguration.md) object

 ** [InstanceId](#API_UpdateAttachedFilesConfiguration_ResponseSyntax) **   <a name="connect-UpdateAttachedFilesConfiguration-response-InstanceId"></a>
The identifier of the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [LastModifiedTime](#API_UpdateAttachedFilesConfiguration_ResponseSyntax) **   <a name="connect-UpdateAttachedFilesConfiguration-response-LastModifiedTime"></a>
The timestamp when the configuration was last modified.
Type: Timestamp

 ** [MaximumSizeLimitInBytes](#API_UpdateAttachedFilesConfiguration_ResponseSyntax) **   <a name="connect-UpdateAttachedFilesConfiguration-response-MaximumSizeLimitInBytes"></a>
The maximum size limit for attached files in bytes.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 104857600.

## Errors
<a name="API_UpdateAttachedFilesConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateAttachedFilesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateAttachedFilesConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateAttachedFilesConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateAttachedFilesConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateAttachedFilesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateAttachedFilesConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateAttachedFilesConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateAttachedFilesConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateAttachedFilesConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateAttachedFilesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateAttachedFilesConfiguration)
