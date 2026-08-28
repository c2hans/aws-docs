---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-securitycontrol-parametervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::SecurityControl ParameterValue
<a name="aws-properties-securityhub-securitycontrol-parametervalue"></a>

 An object that includes the data type of a security control parameter and its current value.

## Syntax
<a name="aws-properties-securityhub-securitycontrol-parametervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-securitycontrol-parametervalue-syntax.json"></a>

```
{
  "[Boolean](#cfn-securityhub-securitycontrol-parametervalue-boolean)" : {{Boolean}},
  "[Double](#cfn-securityhub-securitycontrol-parametervalue-double)" : {{Number}},
  "[Enum](#cfn-securityhub-securitycontrol-parametervalue-enum)" : {{String}},
  "[EnumList](#cfn-securityhub-securitycontrol-parametervalue-enumlist)" : {{[ String, ... ]}},
  "[Integer](#cfn-securityhub-securitycontrol-parametervalue-integer)" : {{Integer}},
  "[IntegerList](#cfn-securityhub-securitycontrol-parametervalue-integerlist)" : {{[ Integer, ... ]}},
  "[String](#cfn-securityhub-securitycontrol-parametervalue-string)" : {{String}},
  "[StringList](#cfn-securityhub-securitycontrol-parametervalue-stringlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-securityhub-securitycontrol-parametervalue-syntax.yaml"></a>

```
  [Boolean](#cfn-securityhub-securitycontrol-parametervalue-boolean): {{
    Boolean}}
  [Double](#cfn-securityhub-securitycontrol-parametervalue-double): {{Number}}
  [Enum](#cfn-securityhub-securitycontrol-parametervalue-enum): {{String}}
  [EnumList](#cfn-securityhub-securitycontrol-parametervalue-enumlist): {{
    - String}}
  [Integer](#cfn-securityhub-securitycontrol-parametervalue-integer): {{
    Integer}}
  [IntegerList](#cfn-securityhub-securitycontrol-parametervalue-integerlist): {{
    - Integer}}
  [String](#cfn-securityhub-securitycontrol-parametervalue-string): {{
    String}}
  [StringList](#cfn-securityhub-securitycontrol-parametervalue-stringlist): {{
    - String}}
```

## Properties
<a name="aws-properties-securityhub-securitycontrol-parametervalue-properties"></a>

`Boolean`  <a name="cfn-securityhub-securitycontrol-parametervalue-boolean"></a>
 A control parameter that is a boolean.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Double`  <a name="cfn-securityhub-securitycontrol-parametervalue-double"></a>
 A control parameter that is a double.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enum`  <a name="cfn-securityhub-securitycontrol-parametervalue-enum"></a>
 A control parameter that is an enum.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnumList`  <a name="cfn-securityhub-securitycontrol-parametervalue-enumlist"></a>
 A control parameter that is a list of enums.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Integer`  <a name="cfn-securityhub-securitycontrol-parametervalue-integer"></a>
 A control parameter that is an integer.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegerList`  <a name="cfn-securityhub-securitycontrol-parametervalue-integerlist"></a>
 A control parameter that is a list of integers.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`String`  <a name="cfn-securityhub-securitycontrol-parametervalue-string"></a>
 A control parameter that is a string.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringList`  <a name="cfn-securityhub-securitycontrol-parametervalue-stringlist"></a>
 A control parameter that is a list of strings.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
