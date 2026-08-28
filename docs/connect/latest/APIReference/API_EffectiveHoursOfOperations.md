---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EffectiveHoursOfOperations.html
---

# EffectiveHoursOfOperations
<a name="API_EffectiveHoursOfOperations"></a>

Information about the hours of operations with the effective override applied.

## Contents
<a name="API_EffectiveHoursOfOperations_Contents"></a>

 ** Date **   <a name="connect-Type-EffectiveHoursOfOperations-Date"></a>
The date that the hours of operation or overrides applies to.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: No

 ** OperationalHours **   <a name="connect-Type-EffectiveHoursOfOperations-OperationalHours"></a>
Information about the hours of operations with the effective override applied.
Type: Array of [OperationalHour](API_OperationalHour.md) objects
Required: No

## See Also
<a name="API_EffectiveHoursOfOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EffectiveHoursOfOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EffectiveHoursOfOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EffectiveHoursOfOperations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
