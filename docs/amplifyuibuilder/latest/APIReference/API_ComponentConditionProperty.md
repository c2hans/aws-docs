---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentConditionProperty.html
---

# ComponentConditionProperty
<a name="API_ComponentConditionProperty"></a>

Represents a conditional expression to set a component property. Use `ComponentConditionProperty` to set a property to different values conditionally, based on the value of another property.

## Contents
<a name="API_ComponentConditionProperty_Contents"></a>

 ** else **   <a name="amplifyuibuilder-Type-ComponentConditionProperty-else"></a>
The value to assign to the property if the condition is not met.
Type: [ComponentProperty](API_ComponentProperty.md) object
Required: No

 ** field **   <a name="amplifyuibuilder-Type-ComponentConditionProperty-field"></a>
The name of a field. Specify this when the property is a data model.
Type: String
Required: No

 ** operand **   <a name="amplifyuibuilder-Type-ComponentConditionProperty-operand"></a>
The value of the property to evaluate.
Type: String
Required: No

 ** operandType **   <a name="amplifyuibuilder-Type-ComponentConditionProperty-operandType"></a>
The type of the property to evaluate.
Type: String
Required: No

 ** operator **   <a name="amplifyuibuilder-Type-ComponentConditionProperty-operator"></a>
The operator to use to perform the evaluation, such as `eq` to represent equals.
Type: String
Required: No

 ** property **   <a name="amplifyuibuilder-Type-ComponentConditionProperty-property"></a>
The name of the conditional property.
Type: String
Required: No

 ** then **   <a name="amplifyuibuilder-Type-ComponentConditionProperty-then"></a>
The value to assign to the property if the condition is met.
Type: [ComponentProperty](API_ComponentProperty.md) object
Required: No

## See Also
<a name="API_ComponentConditionProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ComponentConditionProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ComponentConditionProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ComponentConditionProperty)
