---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_IntentLevelSlotResolutionTestResultItem.html
---

# IntentLevelSlotResolutionTestResultItem
<a name="API_IntentLevelSlotResolutionTestResultItem"></a>

Information about intent-level slot resolution in a test result.

## Contents
<a name="API_IntentLevelSlotResolutionTestResultItem_Contents"></a>

 ** intentName **   <a name="lexv2-Type-IntentLevelSlotResolutionTestResultItem-intentName"></a>
The name of the intent that was recognized.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** multiTurnConversation **   <a name="lexv2-Type-IntentLevelSlotResolutionTestResultItem-multiTurnConversation"></a>
Indicates whether the conversation involves multiple turns or not.
Type: Boolean
Required: Yes

 ** slotResolutionResults **   <a name="lexv2-Type-IntentLevelSlotResolutionTestResultItem-slotResolutionResults"></a>
The results for the slot resolution in the test execution result.
Type: Array of [SlotResolutionTestResultItem](API_SlotResolutionTestResultItem.md) objects
Required: Yes

## See Also
<a name="API_IntentLevelSlotResolutionTestResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/IntentLevelSlotResolutionTestResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/IntentLevelSlotResolutionTestResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/IntentLevelSlotResolutionTestResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
