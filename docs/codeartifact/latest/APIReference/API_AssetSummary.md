---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html
---

# AssetSummary
<a name="API_AssetSummary"></a>

 Contains details about a package version asset.

## Contents
<a name="API_AssetSummary_Contents"></a>

 ** name **   <a name="codeartifact-Type-AssetSummary-name"></a>
 The name of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\P{C}+`
Required: Yes

 ** hashes **   <a name="codeartifact-Type-AssetSummary-hashes"></a>
 The hashes of the asset.
Type: String to string map
Valid Keys: `MD5 | SHA-1 | SHA-256 | SHA-512`
Value Length Constraints: Minimum length of 32. Maximum length of 512.
Value Pattern: `[0-9a-f]+`
Required: No

 ** size **   <a name="codeartifact-Type-AssetSummary-size"></a>
 The size of the asset.
Type: Long
Required: No

## See Also
<a name="API_AssetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/AssetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/AssetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/AssetSummary)
