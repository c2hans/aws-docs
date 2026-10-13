---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_NdiSourceSettings.html
---

# NdiSourceSettings
<a name="API_NdiSourceSettings"></a>

 The settings for the NDI® source. This includes the exact name of the upstream NDI sender that you want to connect to your source.

**Note**
When you update the NDI source, include only the members you want to change. MediaConnect leaves the members that you don't specify unchanged.

## Contents
<a name="API_NdiSourceSettings_Contents"></a>

 ** audioReferenceLevel **   <a name="mediaconnect-Type-NdiSourceSettings-audioReferenceLevel"></a>
The audio reference level of the NDI sender, in decibels relative to full scale (dBFS). Common values are `-20` (NDI and SMPTE) and `-18` (EBU). If you don't specify this field, MediaConnect uses `-20`.
Type: Integer
Valid Range: Minimum value of -40. Maximum value of 0.
Required: No

 ** sourceName **   <a name="mediaconnect-Type-NdiSourceSettings-sourceName"></a>
 The exact name of an existing NDI sender that's registered with your discovery server. If included, the format of this name must be `MACHINENAME (ProgramName)`.
Type: String
Required: No

## See Also
<a name="API_NdiSourceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/NdiSourceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/NdiSourceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/NdiSourceSettings)
