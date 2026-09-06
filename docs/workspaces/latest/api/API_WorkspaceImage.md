---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceImage.html
---

# WorkspaceImage
<a name="API_WorkspaceImage"></a>

Describes a WorkSpace image.

## Contents
<a name="API_WorkspaceImage_Contents"></a>

 ** Created **   <a name="WorkSpaces-Type-WorkspaceImage-Created"></a>
The date when the image was created. If the image has been shared, the AWS account that the image has been shared with sees the original creation date of the image.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpaces-Type-WorkspaceImage-Description"></a>
The description of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: No

 ** ErrorCode **   <a name="WorkSpaces-Type-WorkspaceImage-ErrorCode"></a>
The error code that is returned for the image.
Type: String
Required: No

 ** ErrorDetails **   <a name="WorkSpaces-Type-WorkspaceImage-ErrorDetails"></a>
Additional details of the error returned for the image, including the possible causes of the errors and troubleshooting information.
Type: Array of [ErrorDetails](API_ErrorDetails.md) objects
Required: No

 ** ErrorMessage **   <a name="WorkSpaces-Type-WorkspaceImage-ErrorMessage"></a>
The text of the error message that is returned for the image.
Type: String
Required: No

 ** ImageId **   <a name="WorkSpaces-Type-WorkspaceImage-ImageId"></a>
The identifier of the image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: No

 ** Name **   <a name="WorkSpaces-Type-WorkspaceImage-Name"></a>
The name of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_./()\\-]+$`
Required: No

 ** OperatingSystem **   <a name="WorkSpaces-Type-WorkspaceImage-OperatingSystem"></a>
The operating system that the image is running.
Type: [OperatingSystem](API_OperatingSystem.md) object
Required: No

 ** OwnerAccountId **   <a name="WorkSpaces-Type-WorkspaceImage-OwnerAccountId"></a>
The identifier of the AWS account that owns the image.
Type: String
Pattern: `^\d{12}$`
Required: No

 ** RequiredTenancy **   <a name="WorkSpaces-Type-WorkspaceImage-RequiredTenancy"></a>
Specifies whether the image is running on dedicated hardware. When Bring Your Own License (BYOL) is enabled, this value is set to `DEDICATED`. For more information, see [Bring Your Own Windows Desktop Images](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html).
Type: String
Valid Values: `DEFAULT | DEDICATED`
Required: No

 ** State **   <a name="WorkSpaces-Type-WorkspaceImage-State"></a>
The status of the image.
Type: String
Valid Values: `AVAILABLE | PENDING | ERROR`
Required: No

 ** Updates **   <a name="WorkSpaces-Type-WorkspaceImage-Updates"></a>
The updates (if any) that are available for the specified image.
Type: [UpdateResult](API_UpdateResult.md) object
Required: No

## See Also
<a name="API_WorkspaceImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspaceImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspaceImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspaceImage)
