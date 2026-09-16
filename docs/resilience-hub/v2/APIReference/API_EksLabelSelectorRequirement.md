---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_EksLabelSelectorRequirement.html
---

# EksLabelSelectorRequirement
<a name="API_EksLabelSelectorRequirement"></a>

A single label requirement in a label selector, expressed as a key, an operator, and an optional list of values.

## Contents
<a name="API_EksLabelSelectorRequirement_Contents"></a>

 ** key **   <a name="ngresiliencehub-Type-EksLabelSelectorRequirement-key"></a>
The label key that the requirement applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 317.
Pattern: `([a-z0-9]([-a-z0-9.]*[a-z0-9])?/)?[A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?`
Required: Yes

 ** operator **   <a name="ngresiliencehub-Type-EksLabelSelectorRequirement-operator"></a>
The operator that relates the label key to the values.
Type: String
Valid Values: `IN | NOT_IN | EXISTS | DOES_NOT_EXIST`
Required: Yes

 ** values **   <a name="ngresiliencehub-Type-EksLabelSelectorRequirement-values"></a>
The label values to compare against. Specify values when the operator is IN or NOT\_IN. Leave this empty when the operator is EXISTS or DOES\_NOT\_EXIST.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `([A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?)?`
Required: No

## See Also
<a name="API_EksLabelSelectorRequirement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/EksLabelSelectorRequirement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/EksLabelSelectorRequirement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/EksLabelSelectorRequirement)
