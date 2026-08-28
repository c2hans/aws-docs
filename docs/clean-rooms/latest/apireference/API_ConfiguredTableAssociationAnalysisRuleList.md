---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredTableAssociationAnalysisRuleList.html
---

# ConfiguredTableAssociationAnalysisRuleList
<a name="API_ConfiguredTableAssociationAnalysisRuleList"></a>

 The configured table association analysis rule applied to a configured table with the list analysis rule.

## Contents
<a name="API_ConfiguredTableAssociationAnalysisRuleList_Contents"></a>

 ** allowedAdditionalAnalyses **   <a name="API-Type-ConfiguredTableAssociationAnalysisRuleList-allowedAdditionalAnalyses"></a>
 The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:([\d]{12}|\*):membership\/[\*\d\w-]+\/configuredaudiencemodelassociation\/[\*\d\w-]+$|^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:([0-9]{12}|\*):membership\/[\*\d\w-]+\/configured-model-algorithm-association\/([-a-zA-Z0-9_\/.]+|\*)`
Required: No

 ** allowedResultReceivers **   <a name="API-Type-ConfiguredTableAssociationAnalysisRuleList-allowedResultReceivers"></a>
 The list of collaboration members who are allowed to receive results of queries run with this configured table.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

## See Also
<a name="API_ConfiguredTableAssociationAnalysisRuleList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRuleList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRuleList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredTableAssociationAnalysisRuleList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
