---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ViewSearchCriteria.html
---

# ViewSearchCriteria
<a name="API_ViewSearchCriteria"></a>

Defines the search criteria for filtering views.

## Contents
<a name="API_ViewSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-ViewSearchCriteria-AndConditions"></a>
A list of conditions that must all be satisfied.
Type: Array of [ViewSearchCriteria](#API_ViewSearchCriteria) objects
Required: No

 ** OrConditions **   <a name="connect-Type-ViewSearchCriteria-OrConditions"></a>
A list of conditions to be met, where at least one condition must be satisfied.
Type: Array of [ViewSearchCriteria](#API_ViewSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-ViewSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
Type: [StringCondition](API_StringCondition.md) object
Required: No

 ** ViewStatusCondition **   <a name="connect-Type-ViewSearchCriteria-ViewStatusCondition"></a>
A condition that filters views by their status.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** ViewTypeCondition **   <a name="connect-Type-ViewSearchCriteria-ViewTypeCondition"></a>
A condition that filters views by their type.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_MANAGED`
Required: No

## See Also
<a name="API_ViewSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ViewSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ViewSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ViewSearchCriteria)
