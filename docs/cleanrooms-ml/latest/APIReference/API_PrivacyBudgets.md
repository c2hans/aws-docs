---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_PrivacyBudgets.html
---

# PrivacyBudgets
<a name="API_PrivacyBudgets"></a>

The privacy budget information that controls access to Clean Rooms ML input channels.

## Contents
<a name="API_PrivacyBudgets_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accessBudgets **   <a name="API-Type-PrivacyBudgets-accessBudgets"></a>
A list of access budgets that apply to resources associated with this Clean Rooms ML input channel.
Type: Array of [AccessBudget](API_AccessBudget.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_PrivacyBudgets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/PrivacyBudgets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/PrivacyBudgets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/PrivacyBudgets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
