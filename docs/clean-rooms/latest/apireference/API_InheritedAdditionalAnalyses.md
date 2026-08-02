---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_InheritedAdditionalAnalyses.html
---

# InheritedAdditionalAnalyses
<a name="API_InheritedAdditionalAnalyses"></a>

Contains the inherited additional analyses constraint and its sources from parent tables.

## Contents
<a name="API_InheritedAdditionalAnalyses_Contents"></a>

 ** sources **   <a name="API-Type-InheritedAdditionalAnalyses-sources"></a>
The list of parent tables that contribute to this inherited constraint.
Type: Array of [InheritedAdditionalAnalysesSource](API_InheritedAdditionalAnalysesSource.md) objects
Required: Yes

 ** value **   <a name="API-Type-InheritedAdditionalAnalyses-value"></a>
The effective additional analyses setting inherited from parent tables.
Type: String
Valid Values: `ALLOWED | REQUIRED | NOT_ALLOWED`
Required: Yes

## See Also
<a name="API_InheritedAdditionalAnalyses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/InheritedAdditionalAnalyses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/InheritedAdditionalAnalyses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/InheritedAdditionalAnalyses)
