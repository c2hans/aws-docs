---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UtteranceLevelTestResultItem.html
---

# UtteranceLevelTestResultItem
<a name="API_UtteranceLevelTestResultItem"></a>

Contains information about multiple utterances in the results of a test set execution.

## Contents
<a name="API_UtteranceLevelTestResultItem_Contents"></a>

 ** recordNumber **   <a name="lexv2-Type-UtteranceLevelTestResultItem-recordNumber"></a>
The record number of the result.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 200000.
Required: Yes

 ** turnResult **   <a name="lexv2-Type-UtteranceLevelTestResultItem-turnResult"></a>
Contains information about the turn associated with the result.
Type: [TestSetTurnResult](API_TestSetTurnResult.md) object
Required: Yes

 ** conversationId **   <a name="lexv2-Type-UtteranceLevelTestResultItem-conversationId"></a>
The unique identifier for the conversation associated with the result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^([0-9a-zA-Z][_-]?)+$`
Required: No

## See Also
<a name="API_UtteranceLevelTestResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UtteranceLevelTestResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UtteranceLevelTestResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UtteranceLevelTestResultItem)
