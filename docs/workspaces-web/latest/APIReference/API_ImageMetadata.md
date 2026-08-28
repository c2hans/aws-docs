---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_ImageMetadata.html
---

# ImageMetadata
<a name="API_ImageMetadata"></a>

Metadata information about an uploaded image file.

## Contents
<a name="API_ImageMetadata_Contents"></a>

 ** fileExtension **   <a name="workspacesweb-Type-ImageMetadata-fileExtension"></a>
The file extension of the image.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Pattern: `[\s\S]*`
Required: Yes

 ** lastUploadTimestamp **   <a name="workspacesweb-Type-ImageMetadata-lastUploadTimestamp"></a>
The timestamp when the image was last uploaded.
Type: Timestamp
Required: Yes

 ** mimeType **   <a name="workspacesweb-Type-ImageMetadata-mimeType"></a>
The MIME type of the image.
Type: String
Valid Values: `image/png | image/jpeg | image/x-icon`
Required: Yes

## See Also
<a name="API_ImageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/ImageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/ImageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/ImageMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
