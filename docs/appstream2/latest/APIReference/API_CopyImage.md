---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CopyImage.html
---

# CopyImage
<a name="API_CopyImage"></a>

Copies the image within the same region or to a new region within the same AWS account. Note that any tags you added to the image will not be copied.

## Request Syntax
<a name="API_CopyImage_RequestSyntax"></a>

```
{
   "DestinationImageDescription": "{{string}}",
   "DestinationImageName": "{{string}}",
   "DestinationRegion": "{{string}}",
   "SourceImageName": "{{string}}"
}
```

## Request Parameters
<a name="API_CopyImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationImageDescription](#API_CopyImage_RequestSyntax) **   <a name="WorkSpacesApplications-CopyImage-request-DestinationImageDescription"></a>
The description that the image will have when it is copied to the destination.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DestinationImageName](#API_CopyImage_RequestSyntax) **   <a name="WorkSpacesApplications-CopyImage-request-DestinationImageName"></a>
The name that the image will have when it is copied to the destination.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [DestinationRegion](#API_CopyImage_RequestSyntax) **   <a name="WorkSpacesApplications-CopyImage-request-DestinationRegion"></a>
The destination region to which the image will be copied. This parameter is required, even if you are copying an image within the same region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [SourceImageName](#API_CopyImage_RequestSyntax) **   <a name="WorkSpacesApplications-CopyImage-request-SourceImageName"></a>
The name of the image to copy.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_CopyImage_ResponseSyntax"></a>

```
{
   "DestinationImageName": "string"
}
```

## Response Elements
<a name="API_CopyImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DestinationImageName](#API_CopyImage_ResponseSyntax) **   <a name="WorkSpacesApplications-CopyImage-response-DestinationImageName"></a>
The name of the destination image.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`

## Errors
<a name="API_CopyImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IncompatibleImageException **
The image can't be updated because it's not compatible for updates.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidAccountStatusException **
The resource cannot be created because your AWS account is suspended. For assistance, contact AWS Support.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotAvailableException **
The specified resource exists and is not in use, but isn't available.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CopyImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CopyImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CopyImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CopyImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CopyImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CopyImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CopyImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CopyImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CopyImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CopyImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CopyImage)
