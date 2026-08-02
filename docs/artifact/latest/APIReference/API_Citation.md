---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_Citation.html
---

# Citation
<a name="API_Citation"></a>

Citation information for AI-generated responses.

## Contents
<a name="API_Citation_Contents"></a>

 ** sourceContent **   <a name="artifact-Type-Citation-sourceContent"></a>
Content text from the compliance source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** sourceLabel **   <a name="artifact-Type-Citation-sourceLabel"></a>
Label identifying the compliance source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** sourceLink **   <a name="artifact-Type-Citation-sourceLink"></a>
Link to the compliance source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

## See Also
<a name="API_Citation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/Citation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/Citation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/Citation)
