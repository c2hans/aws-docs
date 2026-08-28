---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AdditionalResources.html
---

# AdditionalResources
<a name="API_AdditionalResources"></a>

The choice level additional resources for a custom lens.

This field does not apply to AWS official lenses.

## Contents
<a name="API_AdditionalResources_Contents"></a>

 ** Content **   <a name="wellarchitected-Type-AdditionalResources-Content"></a>
The URLs for additional resources, either helpful resources or improvement plans, for a custom lens. Up to five additional URLs can be specified.
Type: Array of [ChoiceContent](API_ChoiceContent.md) objects
Required: No

 ** Type **   <a name="wellarchitected-Type-AdditionalResources-Type"></a>
Type of additional resource for a custom lens.
Type: String
Valid Values: `HELPFUL_RESOURCE | IMPROVEMENT_PLAN`
Required: No

## See Also
<a name="API_AdditionalResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AdditionalResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AdditionalResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AdditionalResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
