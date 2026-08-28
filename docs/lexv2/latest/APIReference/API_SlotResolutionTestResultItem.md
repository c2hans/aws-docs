---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotResolutionTestResultItem.html
---

# SlotResolutionTestResultItem
<a name="API_SlotResolutionTestResultItem"></a>

Information about the success and failure rate of slot resolution in the results of a test execution.

## Contents
<a name="API_SlotResolutionTestResultItem_Contents"></a>

 ** resultCounts **   <a name="lexv2-Type-SlotResolutionTestResultItem-resultCounts"></a>
A result for slot resolution in the results of a test execution.
Type: [SlotResolutionTestResultItemCounts](API_SlotResolutionTestResultItemCounts.md) object
Required: Yes

 ** slotName **   <a name="lexv2-Type-SlotResolutionTestResultItem-slotName"></a>
The name of the slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_.-]?)+$`
Required: Yes

## See Also
<a name="API_SlotResolutionTestResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SlotResolutionTestResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SlotResolutionTestResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SlotResolutionTestResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
