---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAttributeFilter.html
---

# RuleAttributeFilter
<a name="API_RuleAttributeFilter"></a>

An object that can be used to specify tag conditions inside the `SearchFilter`. This accepts an `OR` of `AND` (List of List) input where:
+ The top level list specifies conditions that need to be applied with `OR` operator.
+ The inner list specifies conditions that need to be applied with `AND` operator.

## Contents
<a name="API_RuleAttributeFilter_Contents"></a>

 ** AndCondition **   <a name="connect-Type-RuleAttributeFilter-AndCondition"></a>
A list of conditions which would be applied together with an `AND` condition.
Type: [RuleAttributeAndCondition](API_RuleAttributeAndCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-RuleAttributeFilter-OrConditions"></a>
A list of conditions which would be applied together with an `OR` condition.
Type: Array of [RuleAttributeAndCondition](API_RuleAttributeAndCondition.md) objects
Required: No

 ** TagCondition **   <a name="connect-Type-RuleAttributeFilter-TagCondition"></a>
A leaf node condition which can be used to specify a tag condition, for example, `HAVE BPO = 123`.
Type: [TagCondition](API_TagCondition.md) object
Required: No

## See Also
<a name="API_RuleAttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RuleAttributeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RuleAttributeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RuleAttributeFilter)
