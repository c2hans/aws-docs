---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_Bandwidths.html
---

# Bandwidths
<a name="API_Bandwidths"></a>

Contains the details about the available and supported bandwidths.

## Contents
<a name="API_Bandwidths_Contents"></a>

 ** available **   <a name="interconnect-Type-Bandwidths-available"></a>
The list of currently available bandwidths.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 8.
Pattern: `\d+[MG]bps`
Required: No

 ** supported **   <a name="interconnect-Type-Bandwidths-supported"></a>
The list of all bandwidths that this environment plans to support
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 8.
Pattern: `\d+[MG]bps`
Required: No

## See Also
<a name="API_Bandwidths_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/Bandwidths)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/Bandwidths)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/Bandwidths)
