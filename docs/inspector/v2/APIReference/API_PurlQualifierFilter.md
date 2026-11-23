---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_PurlQualifierFilter.html
---

# PurlQualifierFilter

An object that describes the details of a package URL (purl) qualifier filter.

## Contents
<a name="API_PurlQualifierFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-PurlQualifierFilter-comparison"></a>
The operator to use when comparing values in the filter.
Type: String
Valid Values: `EQUALS`
Required: Yes

 ** key **   <a name="inspector2-Type-PurlQualifierFilter-key"></a>
The package URL (purl) qualifier key to filter on.
Type: String
Valid Values: `arch | collector | dev_dependency | distro | epoch | go_toolchain | hardened | private | rust_toolchain | scope | skip_chromium_download | source | stream | transitive_dependency | unresolved | vendor`
Required: Yes

 ** value **   <a name="inspector2-Type-PurlQualifierFilter-value"></a>
The package URL (purl) qualifier value to filter on.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_PurlQualifierFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/PurlQualifierFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/PurlQualifierFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/PurlQualifierFilter)
