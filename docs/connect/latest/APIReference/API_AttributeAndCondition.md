---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AttributeAndCondition.html
---

# AttributeAndCondition
<a name="API_AttributeAndCondition"></a>

A list of conditions which would be applied together with an `AND` condition.

## Contents
<a name="API_AttributeAndCondition_Contents"></a>

 ** HierarchyGroupCondition **   <a name="connect-Type-AttributeAndCondition-HierarchyGroupCondition"></a>
A leaf node condition which can be used to specify a hierarchy group condition.
Type: [HierarchyGroupCondition](API_HierarchyGroupCondition.md) object
Required: No

 ** TagConditions **   <a name="connect-Type-AttributeAndCondition-TagConditions"></a>
A leaf node condition which can be used to specify a tag condition.
Type: Array of [TagCondition](API_TagCondition.md) objects
Required: No

## See Also
<a name="API_AttributeAndCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AttributeAndCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AttributeAndCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AttributeAndCondition)
