---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Condition.html
---

# Condition
<a name="API_Condition"></a>

A leaf node condition which can be used to specify a ProficiencyName, ProficiencyValue and ProficiencyLimit.

## Contents
<a name="API_Condition_Contents"></a>

 ** NumberCondition **   <a name="connect-Type-Condition-NumberCondition"></a>
A leaf node condition which can be used to specify a numeric condition.
Type: [NumberCondition](API_NumberCondition.md) object
Required: No

 ** StringCondition **   <a name="connect-Type-Condition-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
The currently supported values for `FieldName` are `name` and `value`.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Condition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Condition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Condition)
