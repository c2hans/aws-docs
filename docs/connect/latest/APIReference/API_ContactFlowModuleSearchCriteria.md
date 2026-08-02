---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlowModuleSearchCriteria.html
---

# ContactFlowModuleSearchCriteria
<a name="API_ContactFlowModuleSearchCriteria"></a>

The search criteria to be used to return flow modules.

## Contents
<a name="API_ContactFlowModuleSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-ContactFlowModuleSearchCriteria-AndConditions"></a>
A list of conditions which would be applied together with an `AND` condition.
Type: Array of [ContactFlowModuleSearchCriteria](#API_ContactFlowModuleSearchCriteria) objects
Required: No

 ** OrConditions **   <a name="connect-Type-ContactFlowModuleSearchCriteria-OrConditions"></a>
A list of conditions which would be applied together with an `OR` condition.
Type: Array of [ContactFlowModuleSearchCriteria](#API_ContactFlowModuleSearchCriteria) objects
Required: No

 ** StateCondition **   <a name="connect-Type-ContactFlowModuleSearchCriteria-StateCondition"></a>
The state of the flow.
Type: String
Valid Values: `ACTIVE | ARCHIVED`
Required: No

 ** StatusCondition **   <a name="connect-Type-ContactFlowModuleSearchCriteria-StatusCondition"></a>
The status of the flow.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** StringCondition **   <a name="connect-Type-ContactFlowModuleSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_ContactFlowModuleSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlowModuleSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlowModuleSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlowModuleSearchCriteria)
