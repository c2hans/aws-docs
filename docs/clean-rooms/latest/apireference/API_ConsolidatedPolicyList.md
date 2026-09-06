---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConsolidatedPolicyList.html
---

# ConsolidatedPolicyList
<a name="API_ConsolidatedPolicyList"></a>

Controls on the analysis specifications that can be run on a configured table.

## Contents
<a name="API_ConsolidatedPolicyList_Contents"></a>

 ** joinColumns **   <a name="API-Type-ConsolidatedPolicyList-joinColumns"></a>
 The columns to join on.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** listColumns **   <a name="API-Type-ConsolidatedPolicyList-listColumns"></a>
 The columns in the consolidated policy list.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** additionalAnalyses **   <a name="API-Type-ConsolidatedPolicyList-additionalAnalyses"></a>
 Additional analyses for the consolidated policy list.
Type: String
Valid Values: `ALLOWED | REQUIRED | NOT_ALLOWED`
Required: No

 ** allowedAdditionalAnalyses **   <a name="API-Type-ConsolidatedPolicyList-allowedAdditionalAnalyses"></a>
 The additional analyses allowed by the consolidated policy list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:([\d]{12}|\*):membership\/[\*\d\w-]+\/configuredaudiencemodelassociation\/[\*\d\w-]+$|^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:([0-9]{12}|\*):membership\/[\*\d\w-]+\/configured-model-algorithm-association\/([-a-zA-Z0-9_\/.]+|\*)`
Required: No

 ** allowedJoinOperators **   <a name="API-Type-ConsolidatedPolicyList-allowedJoinOperators"></a>
 The allowed join operators in the consolidated policy list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `OR | AND`
Required: No

 ** allowedResultReceivers **   <a name="API-Type-ConsolidatedPolicyList-allowedResultReceivers"></a>
 The allowed result receivers.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

## See Also
<a name="API_ConsolidatedPolicyList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConsolidatedPolicyList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConsolidatedPolicyList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConsolidatedPolicyList)
