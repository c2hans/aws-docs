---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FailedCustomVocabularyItem.html
---

# FailedCustomVocabularyItem
<a name="API_FailedCustomVocabularyItem"></a>

The unique failed custom vocabulary item from the custom vocabulary list.

## Contents
<a name="API_FailedCustomVocabularyItem_Contents"></a>

 ** errorCode **   <a name="lexv2-Type-FailedCustomVocabularyItem-errorCode"></a>
The unique error code for the failed custom vocabulary item from the custom vocabulary list.
Type: String
Valid Values: `DUPLICATE_INPUT | RESOURCE_DOES_NOT_EXIST | RESOURCE_ALREADY_EXISTS | INTERNAL_SERVER_FAILURE`
Required: No

 ** errorMessage **   <a name="lexv2-Type-FailedCustomVocabularyItem-errorMessage"></a>
The error message for the failed custom vocabulary item from the custom vocabulary list.
Type: String
Required: No

 ** itemId **   <a name="lexv2-Type-FailedCustomVocabularyItem-itemId"></a>
The unique item identifer for the failed custom vocabulary item from the custom vocabulary list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

## See Also
<a name="API_FailedCustomVocabularyItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/FailedCustomVocabularyItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/FailedCustomVocabularyItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/FailedCustomVocabularyItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
