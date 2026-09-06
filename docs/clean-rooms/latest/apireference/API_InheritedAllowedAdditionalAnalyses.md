---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_InheritedAllowedAdditionalAnalyses.html
---

# InheritedAllowedAdditionalAnalyses
<a name="API_InheritedAllowedAdditionalAnalyses"></a>

Contains the inherited allowed additional analyses constraint and its sources from parent tables.

## Contents
<a name="API_InheritedAllowedAdditionalAnalyses_Contents"></a>

 ** sources **   <a name="API-Type-InheritedAllowedAdditionalAnalyses-sources"></a>
The list of parent tables that contribute to this inherited constraint.
Type: Array of [InheritedAllowedAdditionalAnalysesSource](API_InheritedAllowedAdditionalAnalysesSource.md) objects
Required: Yes

 ** value **   <a name="API-Type-InheritedAllowedAdditionalAnalyses-value"></a>
The effective list of allowed additional analyses inherited from parent tables.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:([\d]{12}|\*):membership\/[\*\d\w-]+\/configuredaudiencemodelassociation\/[\*\d\w-]+$|^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:([0-9]{12}|\*):membership\/[\*\d\w-]+\/configured-model-algorithm-association\/([-a-zA-Z0-9_\/.]+|\*)`
Required: Yes

## See Also
<a name="API_InheritedAllowedAdditionalAnalyses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/InheritedAllowedAdditionalAnalyses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/InheritedAllowedAdditionalAnalyses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/InheritedAllowedAdditionalAnalyses)
