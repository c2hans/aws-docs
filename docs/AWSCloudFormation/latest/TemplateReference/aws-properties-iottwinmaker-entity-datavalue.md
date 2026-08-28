---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-entity-datavalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::Entity DataValue
<a name="aws-properties-iottwinmaker-entity-datavalue"></a>

An object that specifies a value for a property.

## Syntax
<a name="aws-properties-iottwinmaker-entity-datavalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-entity-datavalue-syntax.json"></a>

```
{
  "[BooleanValue](#cfn-iottwinmaker-entity-datavalue-booleanvalue)" : {{Boolean}},
  "[DoubleValue](#cfn-iottwinmaker-entity-datavalue-doublevalue)" : {{Number}},
  "[Expression](#cfn-iottwinmaker-entity-datavalue-expression)" : {{String}},
  "[IntegerValue](#cfn-iottwinmaker-entity-datavalue-integervalue)" : {{Integer}},
  "[ListValue](#cfn-iottwinmaker-entity-datavalue-listvalue)" : {{[ DataValue, ... ]}},
  "[LongValue](#cfn-iottwinmaker-entity-datavalue-longvalue)" : {{Number}},
  "[MapValue](#cfn-iottwinmaker-entity-datavalue-mapvalue)" : {{{{{Key}}: {{Value}}, ...}}},
  "[RelationshipValue](#cfn-iottwinmaker-entity-datavalue-relationshipvalue)" : {{RelationshipValue}},
  "[StringValue](#cfn-iottwinmaker-entity-datavalue-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-entity-datavalue-syntax.yaml"></a>

```
  [BooleanValue](#cfn-iottwinmaker-entity-datavalue-booleanvalue): {{
    Boolean}}
  [DoubleValue](#cfn-iottwinmaker-entity-datavalue-doublevalue): {{Number}}
  [Expression](#cfn-iottwinmaker-entity-datavalue-expression): {{String}}
  [IntegerValue](#cfn-iottwinmaker-entity-datavalue-integervalue): {{
    Integer}}
  [ListValue](#cfn-iottwinmaker-entity-datavalue-listvalue): {{
    - DataValue}}
  [LongValue](#cfn-iottwinmaker-entity-datavalue-longvalue): {{Number}}
  [MapValue](#cfn-iottwinmaker-entity-datavalue-mapvalue): {{
    {{Key}}: {{Value}}}}
  [RelationshipValue](#cfn-iottwinmaker-entity-datavalue-relationshipvalue): {{
    RelationshipValue}}
  [StringValue](#cfn-iottwinmaker-entity-datavalue-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-iottwinmaker-entity-datavalue-properties"></a>

`BooleanValue`  <a name="cfn-iottwinmaker-entity-datavalue-booleanvalue"></a>
A boolean value.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DoubleValue`  <a name="cfn-iottwinmaker-entity-datavalue-doublevalue"></a>
A double value.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-iottwinmaker-entity-datavalue-expression"></a>
An expression that produces the value.
*Required*: No
*Type*: String
*Pattern*: `(^\$\{Parameters\.[a-zA-z]+([a-zA-z_0-9]*)}$)`
*Minimum*: `1`
*Maximum*: `316`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegerValue`  <a name="cfn-iottwinmaker-entity-datavalue-integervalue"></a>
An integer value.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListValue`  <a name="cfn-iottwinmaker-entity-datavalue-listvalue"></a>
A list of multiple values.
*Required*: No
*Type*: Array of [DataValue](#aws-properties-iottwinmaker-entity-datavalue)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LongValue`  <a name="cfn-iottwinmaker-entity-datavalue-longvalue"></a>
A long value.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapValue`  <a name="cfn-iottwinmaker-entity-datavalue-mapvalue"></a>
An object that maps strings to multiple DataValue objects.
*Required*: No
*Type*: Object of [DataValue](#aws-properties-iottwinmaker-entity-datavalue)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelationshipValue`  <a name="cfn-iottwinmaker-entity-datavalue-relationshipvalue"></a>
A value that relates a component to another component.
*Required*: No
*Type*: [RelationshipValue](aws-properties-iottwinmaker-entity-relationshipvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-iottwinmaker-entity-datavalue-stringvalue"></a>
A string value.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
