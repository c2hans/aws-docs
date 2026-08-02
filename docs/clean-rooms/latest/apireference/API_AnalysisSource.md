---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisSource.html
---

# AnalysisSource
<a name="API_AnalysisSource"></a>

The structure that defines the body of the analysis template.

## Contents
<a name="API_AnalysisSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** artifacts **   <a name="API-Type-AnalysisSource-artifacts"></a>
 The artifacts of the analysis source.
Type: [AnalysisTemplateArtifacts](API_AnalysisTemplateArtifacts.md) object
Required: No

 ** text **   <a name="API-Type-AnalysisSource-text"></a>
The query text.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500000.
Required: No

## See Also
<a name="API_AnalysisSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisSource)
