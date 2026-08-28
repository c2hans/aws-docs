---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CalculationComponent.html
---

# CalculationComponent
<a name="API_CalculationComponent"></a>

Represents a component metric referenced in a custom metric calculation formula.

## Contents
<a name="API_CalculationComponent_Contents"></a>

 ** Alias **   <a name="connect-Type-CalculationComponent-Alias"></a>
The alias used to reference this component in the calculation expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** MetricFilters **   <a name="connect-Type-CalculationComponent-MetricFilters"></a>
The filters applied to the calculation component.
Type: Array of [MetricFilter](API_MetricFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** MetricId **   <a name="connect-Type-CalculationComponent-MetricId"></a>
The ARN of an AWS-managed metric used in this calculation component. Mutually exclusive with `MetricName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: No

 ** MetricName **   <a name="connect-Type-CalculationComponent-MetricName"></a>
The name of an AWS-managed metric used in this calculation component (for example, `CONTACTS_HANDLED`). Mutually exclusive with `MetricId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_CalculationComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CalculationComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CalculationComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CalculationComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
