---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DicomMetadataMapping.html
---

# DicomMetadataMapping
<a name="API_DicomMetadataMapping"></a>

Maps DCM files to their metadata.

## Contents
<a name="API_DicomMetadataMapping_Contents"></a>

 ** metadataFilePath **   <a name="healthimaging-Type-DicomMetadataMapping-metadataFilePath"></a>
The path to the JSON metadata file relative to inputS3Uri.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9!-~]+([a-zA-Z0-9!-~ ]*[a-zA-Z0-9!-~]+)*`
Required: Yes

 ** studyInstanceUID **   <a name="healthimaging-Type-DicomMetadataMapping-studyInstanceUID"></a>
The Study Instance UID that identifies the study.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[0-9.]+`
Required: Yes

 ** seriesInstanceUID **   <a name="healthimaging-Type-DicomMetadataMapping-seriesInstanceUID"></a>
The Series Instance UID that identifies the series. This parameter is optional because the mapping might be at the study level.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[0-9.]+`
Required: No

## See Also
<a name="API_DicomMetadataMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/DicomMetadataMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DicomMetadataMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/DicomMetadataMapping)
