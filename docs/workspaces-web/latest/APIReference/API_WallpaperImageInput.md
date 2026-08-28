---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_WallpaperImageInput.html
---

# WallpaperImageInput
<a name="API_WallpaperImageInput"></a>

The input for a wallpaper image. Provide the image as either a binary image file or an S3 URI. Maximum 5 MB in JPEG or PNG format.

## Contents
<a name="API_WallpaperImageInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** blob **   <a name="workspacesweb-Type-WallpaperImageInput-blob"></a>
The image provided as a binary image file.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 5242880.
Required: No

 ** s3Uri **   <a name="workspacesweb-Type-WallpaperImageInput-s3Uri"></a>
The S3 URI pointing to the image file. The URI must use the format `s3://bucket-name/key-name`. You must have read access to the S3 object.
Type: String
Pattern: `s3://[a-z0-9][a-z0-9\.\-]{1,61}[a-z0-9]/.+`
Required: No

## See Also
<a name="API_WallpaperImageInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/WallpaperImageInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/WallpaperImageInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/WallpaperImageInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
