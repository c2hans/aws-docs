---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_SequenceInformation.html
---

# SequenceInformation
<a name="API_SequenceInformation"></a>

Details about a sequence.

## Contents
<a name="API_SequenceInformation_Contents"></a>

 ** alignment **   <a name="omics-Type-SequenceInformation-alignment"></a>
The sequence's alignment setting.
Type: String
Required: No

 ** generatedFrom **   <a name="omics-Type-SequenceInformation-generatedFrom"></a>
Where the sequence originated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** totalBaseCount **   <a name="omics-Type-SequenceInformation-totalBaseCount"></a>
The sequence's total base count.
Type: Long
Required: No

 ** totalReadCount **   <a name="omics-Type-SequenceInformation-totalReadCount"></a>
The sequence's total read count.
Type: Long
Required: No

## See Also
<a name="API_SequenceInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/SequenceInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/SequenceInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/SequenceInformation)
