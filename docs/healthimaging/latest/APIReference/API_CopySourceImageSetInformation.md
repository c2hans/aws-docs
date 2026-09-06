---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_CopySourceImageSetInformation.html
---

# CopySourceImageSetInformation
<a name="API_CopySourceImageSetInformation"></a>

Copy source image set information.

## Contents
<a name="API_CopySourceImageSetInformation_Contents"></a>

 ** latestVersionId **   <a name="healthimaging-Type-CopySourceImageSetInformation-latestVersionId"></a>
The latest version identifier for the source image set.
Type: String
Pattern: `\d+`
Required: Yes

 ** DICOMCopies **   <a name="healthimaging-Type-CopySourceImageSetInformation-DICOMCopies"></a>
Contains `MetadataCopies` structure and wraps information related to specific copy use cases. For example, when copying subsets.
Type: [MetadataCopies](API_MetadataCopies.md) object
Required: No

## See Also
<a name="API_CopySourceImageSetInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/CopySourceImageSetInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/CopySourceImageSetInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/CopySourceImageSetInformation)
