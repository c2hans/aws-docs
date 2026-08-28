---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestSetDiscrepancyErrors.html
---

# TestSetDiscrepancyErrors
<a name="API_TestSetDiscrepancyErrors"></a>

Contains details about the errors in the test set discrepancy report

## Contents
<a name="API_TestSetDiscrepancyErrors_Contents"></a>

 ** intentDiscrepancies **   <a name="lexv2-Type-TestSetDiscrepancyErrors-intentDiscrepancies"></a>
Contains information about discrepancies found for intents between the test set and the bot.
Type: Array of [TestSetIntentDiscrepancyItem](API_TestSetIntentDiscrepancyItem.md) objects
Required: Yes

 ** slotDiscrepancies **   <a name="lexv2-Type-TestSetDiscrepancyErrors-slotDiscrepancies"></a>
Contains information about discrepancies found for slots between the test set and the bot.
Type: Array of [TestSetSlotDiscrepancyItem](API_TestSetSlotDiscrepancyItem.md) objects
Required: Yes

## See Also
<a name="API_TestSetDiscrepancyErrors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestSetDiscrepancyErrors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestSetDiscrepancyErrors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestSetDiscrepancyErrors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
