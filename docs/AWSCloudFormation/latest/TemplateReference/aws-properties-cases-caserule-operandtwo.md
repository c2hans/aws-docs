---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-caserule-operandtwo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::CaseRule OperandTwo
<a name="aws-properties-cases-caserule-operandtwo"></a>

Represents the right hand operand in the condition. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Syntax
<a name="aws-properties-cases-caserule-operandtwo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-caserule-operandtwo-syntax.json"></a>

```
{
  "[BooleanValue](#cfn-cases-caserule-operandtwo-booleanvalue)" : {{Boolean}},
  "[DoubleValue](#cfn-cases-caserule-operandtwo-doublevalue)" : {{Number}},
  "[EmptyValue](#cfn-cases-caserule-operandtwo-emptyvalue)" : {{Json}},
  "[StringValue](#cfn-cases-caserule-operandtwo-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-cases-caserule-operandtwo-syntax.yaml"></a>

```
  [BooleanValue](#cfn-cases-caserule-operandtwo-booleanvalue): {{
    Boolean}}
  [DoubleValue](#cfn-cases-caserule-operandtwo-doublevalue): {{Number}}
  [EmptyValue](#cfn-cases-caserule-operandtwo-emptyvalue): {{Json}}
  [StringValue](#cfn-cases-caserule-operandtwo-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-cases-caserule-operandtwo-properties"></a>

`BooleanValue`  <a name="cfn-cases-caserule-operandtwo-booleanvalue"></a>
Boolean value type.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DoubleValue`  <a name="cfn-cases-caserule-operandtwo-doublevalue"></a>
Double value type.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmptyValue`  <a name="cfn-cases-caserule-operandtwo-emptyvalue"></a>
Represents an empty operand value. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-cases-caserule-operandtwo-stringvalue"></a>
String value type.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
