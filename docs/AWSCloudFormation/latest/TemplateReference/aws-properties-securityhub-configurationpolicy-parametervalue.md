---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-configurationpolicy-parametervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConfigurationPolicy ParameterValue
<a name="aws-properties-securityhub-configurationpolicy-parametervalue"></a>

 An object that includes the data type of a security control parameter and its current value.

## Syntax
<a name="aws-properties-securityhub-configurationpolicy-parametervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-configurationpolicy-parametervalue-syntax.json"></a>

```
{
  "[Boolean](#cfn-securityhub-configurationpolicy-parametervalue-boolean)" : {{Boolean}},
  "[Double](#cfn-securityhub-configurationpolicy-parametervalue-double)" : {{Number}},
  "[Enum](#cfn-securityhub-configurationpolicy-parametervalue-enum)" : {{String}},
  "[EnumList](#cfn-securityhub-configurationpolicy-parametervalue-enumlist)" : {{[ String, ... ]}},
  "[Integer](#cfn-securityhub-configurationpolicy-parametervalue-integer)" : {{Integer}},
  "[IntegerList](#cfn-securityhub-configurationpolicy-parametervalue-integerlist)" : {{[ Integer, ... ]}},
  "[String](#cfn-securityhub-configurationpolicy-parametervalue-string)" : {{String}},
  "[StringList](#cfn-securityhub-configurationpolicy-parametervalue-stringlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-securityhub-configurationpolicy-parametervalue-syntax.yaml"></a>

```
  [Boolean](#cfn-securityhub-configurationpolicy-parametervalue-boolean): {{
    Boolean}}
  [Double](#cfn-securityhub-configurationpolicy-parametervalue-double): {{Number}}
  [Enum](#cfn-securityhub-configurationpolicy-parametervalue-enum): {{String}}
  [EnumList](#cfn-securityhub-configurationpolicy-parametervalue-enumlist): {{
    - String}}
  [Integer](#cfn-securityhub-configurationpolicy-parametervalue-integer): {{
    Integer}}
  [IntegerList](#cfn-securityhub-configurationpolicy-parametervalue-integerlist): {{
    - Integer}}
  [String](#cfn-securityhub-configurationpolicy-parametervalue-string): {{
    String}}
  [StringList](#cfn-securityhub-configurationpolicy-parametervalue-stringlist): {{
    - String}}
```

## Properties
<a name="aws-properties-securityhub-configurationpolicy-parametervalue-properties"></a>

`Boolean`  <a name="cfn-securityhub-configurationpolicy-parametervalue-boolean"></a>
 A control parameter that is a boolean.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Double`  <a name="cfn-securityhub-configurationpolicy-parametervalue-double"></a>
 A control parameter that is a double.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enum`  <a name="cfn-securityhub-configurationpolicy-parametervalue-enum"></a>
 A control parameter that is an enum.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnumList`  <a name="cfn-securityhub-configurationpolicy-parametervalue-enumlist"></a>
 A control parameter that is a list of enums.
*Required*: No
*Type*: Array of String
*Maximum*: `2048 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Integer`  <a name="cfn-securityhub-configurationpolicy-parametervalue-integer"></a>
 A control parameter that is an integer.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegerList`  <a name="cfn-securityhub-configurationpolicy-parametervalue-integerlist"></a>
 A control parameter that is a list of integers.
*Required*: No
*Type*: Array of Integer
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`String`  <a name="cfn-securityhub-configurationpolicy-parametervalue-string"></a>
 A control parameter that is a string.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringList`  <a name="cfn-securityhub-configurationpolicy-parametervalue-stringlist"></a>
 A control parameter that is a list of strings.
*Required*: No
*Type*: Array of String
*Maximum*: `2048 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
