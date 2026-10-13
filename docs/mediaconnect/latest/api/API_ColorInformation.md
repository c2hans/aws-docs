---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ColorInformation.html
---

# ColorInformation
<a name="API_ColorInformation"></a>

The color signaling of the video stream.

## Contents
<a name="API_ColorInformation_Contents"></a>

 ** colorimetry **   <a name="mediaconnect-Type-ColorInformation-colorimetry"></a>
The color primaries that the video stream uses (for example, `BT709` or `BT2020`).
Type: String
Valid Values: `BT709 | BT470M | BT470BG | BT601 | SMPTE240M | GENERIC_FILM | BT2020 | SMPTE428 | SMPTE431 | SMPTE432`
Required: No

 ** matrixCoefficients **   <a name="mediaconnect-Type-ColorInformation-matrixCoefficients"></a>
The YCbCr matrix coefficients that the video stream uses (for example, `BT709` or `BT2020_NCL`).
Type: String
Valid Values: `IDENTITY | BT709 | FCC | BT470BG | BT601 | SMPTE240M | YCGCO | BT2020_NCL | BT2020_CL | SMPTE2085 | CHROMATICITY_DERIVED_NCL | CHROMATICITY_DERIVED_CL | BT2100_ICTCP | IPT_C2`
Required: No

 ** transferCharacteristics **   <a name="mediaconnect-Type-ColorInformation-transferCharacteristics"></a>
The transfer characteristics that the video stream uses (for example, `BT601`, `BT709`, `BT2100_PQ`, or `BT2100_HLG`).
Type: String
Valid Values: `BT709 | BT470M | BT470BG | BT601 | SMPTE240M | LINEAR | LOG100 | LOG316 | IEC61966_2_4 | BT1361_ECG | IEC61966_2_1 | BT2020_10 | BT2020_12 | BT2100_PQ | SMPTE428 | BT2100_HLG`
Required: No

## See Also
<a name="API_ColorInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ColorInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ColorInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ColorInformation)
