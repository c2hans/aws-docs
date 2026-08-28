---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EffectiveOverrideHours.html
---

# EffectiveOverrideHours
<a name="API_EffectiveOverrideHours"></a>

Information about the hours of operation overrides which contribute to effective hours of operations.

## Contents
<a name="API_EffectiveOverrideHours_Contents"></a>

 ** Date **   <a name="connect-Type-EffectiveOverrideHours-Date"></a>
The date that the hours of operation override applies to.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: No

 ** OverrideHours **   <a name="connect-Type-EffectiveOverrideHours-OverrideHours"></a>
Information about the hours of operation overrides that apply to a specific date.
Type: Array of [OverrideHour](API_OverrideHour.md) objects
Required: No

## See Also
<a name="API_EffectiveOverrideHours_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EffectiveOverrideHours)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EffectiveOverrideHours)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EffectiveOverrideHours)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
