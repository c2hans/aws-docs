---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ImageSoftwareMetadata.html
---

# ImageSoftwareMetadata
<a name="API_ImageSoftwareMetadata"></a>

Describes the software metadata for an image, such as the installed NVIDIA GRID driver version.

## Contents
<a name="API_ImageSoftwareMetadata_Contents"></a>

 ** nvidiaGridDriverVersion **   <a name="WorkSpacesApplications-Type-ImageSoftwareMetadata-nvidiaGridDriverVersion"></a>
The version of the NVIDIA GRID driver installed on the image. This field is empty if no NVIDIA GRID driver is installed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[0-9]+(\.[0-9]+){1,2}$`
Required: No

## See Also
<a name="API_ImageSoftwareMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ImageSoftwareMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ImageSoftwareMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ImageSoftwareMetadata)
