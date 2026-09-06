---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredTableAssociationAnalysisRuleCustom.html
---

# ConfiguredTableAssociationAnalysisRuleCustom
<a name="API_ConfiguredTableAssociationAnalysisRuleCustom"></a>

 The configured table association analysis rule applied to a configured table with the custom analysis rule.

## Contents
<a name="API_ConfiguredTableAssociationAnalysisRuleCustom_Contents"></a>

 ** allowedAdditionalAnalyses **   <a name="API-Type-ConfiguredTableAssociationAnalysisRuleCustom-allowedAdditionalAnalyses"></a>
 The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:([\d]{12}|\*):membership\/[\*\d\w-]+\/configuredaudiencemodelassociation\/[\*\d\w-]+$|^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:([0-9]{12}|\*):membership\/[\*\d\w-]+\/configured-model-algorithm-association\/([-a-zA-Z0-9_\/.]+|\*)`
Required: No

 ** allowedResultReceivers **   <a name="API-Type-ConfiguredTableAssociationAnalysisRuleCustom-allowedResultReceivers"></a>
 The list of collaboration members who are allowed to receive results of queries run with this configured table.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

## See Also
<a name="API_ConfiguredTableAssociationAnalysisRuleCustom_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRuleCustom)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRuleCustom)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRuleCustom)
