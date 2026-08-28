---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_IntentClassificationTestResultItem.html
---

# IntentClassificationTestResultItem
<a name="API_IntentClassificationTestResultItem"></a>

Information for an intent that is classified by the test workbench.

## Contents
<a name="API_IntentClassificationTestResultItem_Contents"></a>

 ** intentName **   <a name="lexv2-Type-IntentClassificationTestResultItem-intentName"></a>
The name of the intent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** multiTurnConversation **   <a name="lexv2-Type-IntentClassificationTestResultItem-multiTurnConversation"></a>
Indicates whether the conversation involves multiple turns or not.
Type: Boolean
Required: Yes

 ** resultCounts **   <a name="lexv2-Type-IntentClassificationTestResultItem-resultCounts"></a>
The result of the intent classification test.
Type: [IntentClassificationTestResultItemCounts](API_IntentClassificationTestResultItemCounts.md) object
Required: Yes

## See Also
<a name="API_IntentClassificationTestResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/IntentClassificationTestResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/IntentClassificationTestResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/IntentClassificationTestResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
