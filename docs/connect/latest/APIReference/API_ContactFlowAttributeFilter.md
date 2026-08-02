---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlowAttributeFilter.html
---

# ContactFlowAttributeFilter
<a name="API_ContactFlowAttributeFilter"></a>

 Filter for contact flow attributes with multiple condition types.

## Contents
<a name="API_ContactFlowAttributeFilter_Contents"></a>

 ** AndCondition **   <a name="connect-Type-ContactFlowAttributeFilter-AndCondition"></a>
 A list of conditions which would be applied together with a AND condition.
Type: [ContactFlowAttributeAndCondition](API_ContactFlowAttributeAndCondition.md) object
Required: No

 ** ContactFlowTypeCondition **   <a name="connect-Type-ContactFlowAttributeFilter-ContactFlowTypeCondition"></a>
 Contact flow type condition within attribute filter.
Type: [ContactFlowTypeCondition](API_ContactFlowTypeCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-ContactFlowAttributeFilter-OrConditions"></a>
 A list of conditions which would be applied together with an OR condition.
Type: Array of [ContactFlowAttributeAndCondition](API_ContactFlowAttributeAndCondition.md) objects
Required: No

 ** TagCondition **   <a name="connect-Type-ContactFlowAttributeFilter-TagCondition"></a>
A leaf node condition which can be used to specify a tag condition, for example, `HAVE BPO = 123`.
Type: [TagCondition](API_TagCondition.md) object
Required: No

## See Also
<a name="API_ContactFlowAttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlowAttributeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlowAttributeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlowAttributeFilter)
