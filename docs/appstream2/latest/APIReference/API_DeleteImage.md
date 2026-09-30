---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteImage.html
---

# DeleteImage
<a name="API_DeleteImage"></a>

Deletes the specified image. You cannot delete an image when it is in use. After you delete an image, you cannot provision new capacity using the image.

## Request Syntax
<a name="API_DeleteImage_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DeleteImage_RequestSyntax) **   <a name="WorkSpacesApplications-DeleteImage-request-Name"></a>
The name of the image.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_DeleteImage_ResponseSyntax"></a>

```
{
   "Image": {
      "Applications": [
         {
            "AppBlockArn": "string",
            "Arn": "string",
            "CreatedTime": number,
            "Description": "string",
            "DisplayName": "string",
            "Enabled": boolean,
            "IconS3Location": {
               "S3Bucket": "string",
               "S3Key": "string"
            },
            "IconURL": "string",
            "InstanceFamilies": [ "string" ],
            "LaunchParameters": "string",
            "LaunchPath": "string",
            "Metadata": {
               "string" : "string"
            },
            "Name": "string",
            "Platforms": [ "string" ],
            "WorkingDirectory": "string"
         }
      ],
      "AppstreamAgentVersion": "string",
      "Arn": "string",
      "BaseImageArn": "string",
      "CreatedTime": number,
      "Description": "string",
      "DisplayName": "string",
      "DynamicAppProvidersEnabled": "string",
      "ImageBuilderName": "string",
      "ImageBuilderSupported": boolean,
      "ImageErrors": [
         {
            "ErrorCode": "string",
            "ErrorMessage": "string",
            "ErrorTimestamp": number
         }
      ],
      "ImagePermissions": {
         "allowFleet": boolean,
         "allowImageBuilder": boolean
      },
      "ImageSharedWithOthers": "string",
      "ImageSoftwareMetadata": {
         "nvidiaGridDriverVersion": "string"
      },
      "ImageType": "string",
      "LatestAppstreamAgentVersion": "string",
      "ManagedSoftwareIncluded": boolean,
      "Name": "string",
      "Platform": "string",
      "PublicBaseImageReleasedDate": number,
      "State": "string",
      "StateChangeReason": {
         "Code": "string",
         "Message": "string"
      },
      "SupportedInstanceFamilies": [ "string" ],
      "Visibility": "string"
   }
}
```

## Response Elements
<a name="API_DeleteImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Image](#API_DeleteImage_ResponseSyntax) **   <a name="WorkSpacesApplications-DeleteImage-response-Image"></a>
Information about the image.
Type: [Image](API_Image.md) object

## Errors
<a name="API_DeleteImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is in use.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DeleteImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DeleteImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DeleteImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DeleteImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DeleteImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DeleteImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DeleteImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DeleteImage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DeleteImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DeleteImage)
