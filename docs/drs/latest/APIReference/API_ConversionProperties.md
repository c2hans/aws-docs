---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_ConversionProperties.html
---

# ConversionProperties
<a name="API_ConversionProperties"></a>

Properties of a conversion job

## Contents
<a name="API_ConversionProperties_Contents"></a>

 ** dataTimestamp **   <a name="drs-Type-ConversionProperties-dataTimestamp"></a>
The timestamp of when the snapshot being converted was taken
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

 ** forceUefi **   <a name="drs-Type-ConversionProperties-forceUefi"></a>
Whether the volume being converted uses UEFI or not
Type: Boolean
Required: No

 ** rootVolumeName **   <a name="drs-Type-ConversionProperties-rootVolumeName"></a>
The root volume name of a conversion job
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

 ** volumeToConversionMap **   <a name="drs-Type-ConversionProperties-volumeToConversionMap"></a>
A mapping between the volumes being converted and the converted snapshot ids
Type: String to string to string map map
Key Length Constraints: Minimum length of 0. Maximum length of 65536.
Key Pattern: `snap-[0-9a-zA-Z]{17}`
Value Pattern: `snap-[0-9a-zA-Z]{17}`
Required: No

 ** volumeToProductCodes **   <a name="drs-Type-ConversionProperties-volumeToProductCodes"></a>
A mapping between the volumes being converted and the product codes associated with them
Type: String to array of [ProductCode](API_ProductCode.md) objects map
Key Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

 ** volumeToVolumeSize **   <a name="drs-Type-ConversionProperties-volumeToVolumeSize"></a>
A mapping between the volumes and their sizes
Type: String to long map
Key Length Constraints: Minimum length of 0. Maximum length of 65536.
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ConversionProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/ConversionProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/ConversionProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/ConversionProperties)
