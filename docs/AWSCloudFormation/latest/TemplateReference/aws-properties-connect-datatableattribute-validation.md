---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-datatableattribute-validation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::DataTableAttribute Validation
<a name="aws-properties-connect-datatableattribute-validation"></a>

Defines validation rules for data table attribute values. Based on JSON Schema Draft 2020-12 with additional Connect-specific validations. Validation rules ensure data integrity and consistency across the data table.

## Syntax
<a name="aws-properties-connect-datatableattribute-validation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-datatableattribute-validation-syntax.json"></a>

```
{
  "[Enum](#cfn-connect-datatableattribute-validation-enum)" : {{Enum}},
  "[ExclusiveMaximum](#cfn-connect-datatableattribute-validation-exclusivemaximum)" : {{Number}},
  "[ExclusiveMinimum](#cfn-connect-datatableattribute-validation-exclusiveminimum)" : {{Number}},
  "[Maximum](#cfn-connect-datatableattribute-validation-maximum)" : {{Number}},
  "[MaxLength](#cfn-connect-datatableattribute-validation-maxlength)" : {{Integer}},
  "[MaxValues](#cfn-connect-datatableattribute-validation-maxvalues)" : {{Integer}},
  "[Minimum](#cfn-connect-datatableattribute-validation-minimum)" : {{Number}},
  "[MinLength](#cfn-connect-datatableattribute-validation-minlength)" : {{Integer}},
  "[MinValues](#cfn-connect-datatableattribute-validation-minvalues)" : {{Integer}},
  "[MultipleOf](#cfn-connect-datatableattribute-validation-multipleof)" : {{Number}}
}
```

### YAML
<a name="aws-properties-connect-datatableattribute-validation-syntax.yaml"></a>

```
  [Enum](#cfn-connect-datatableattribute-validation-enum): {{
    Enum}}
  [ExclusiveMaximum](#cfn-connect-datatableattribute-validation-exclusivemaximum): {{Number}}
  [ExclusiveMinimum](#cfn-connect-datatableattribute-validation-exclusiveminimum): {{Number}}
  [Maximum](#cfn-connect-datatableattribute-validation-maximum): {{Number}}
  [MaxLength](#cfn-connect-datatableattribute-validation-maxlength): {{Integer}}
  [MaxValues](#cfn-connect-datatableattribute-validation-maxvalues): {{Integer}}
  [Minimum](#cfn-connect-datatableattribute-validation-minimum): {{Number}}
  [MinLength](#cfn-connect-datatableattribute-validation-minlength): {{Integer}}
  [MinValues](#cfn-connect-datatableattribute-validation-minvalues): {{Integer}}
  [MultipleOf](#cfn-connect-datatableattribute-validation-multipleof): {{Number}}
```

## Properties
<a name="aws-properties-connect-datatableattribute-validation-properties"></a>

`Enum`  <a name="cfn-connect-datatableattribute-validation-enum"></a>
Defines enumeration constraints for attribute values. Can specify a list of allowed values and whether custom values are permitted beyond the enumerated list.
*Required*: No
*Type*: [Enum](aws-properties-connect-datatableattribute-enum.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExclusiveMaximum`  <a name="cfn-connect-datatableattribute-validation-exclusivemaximum"></a>
The largest exclusive numeric value for NUMBER value type. Can be provided alongside Maximum where both operate independently. Must be greater than ExclusiveMinimum and Minimum. Applies to NUMBER and values within NUMBER\_LIST.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExclusiveMinimum`  <a name="cfn-connect-datatableattribute-validation-exclusiveminimum"></a>
The smallest exclusive numeric value for NUMBER value type. Can be provided alongside Minimum where both operate independently. Must be less than ExclusiveMaximum and Maximum. Applies to NUMBER and values within NUMBER\_LIST.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Maximum`  <a name="cfn-connect-datatableattribute-validation-maximum"></a>
The largest inclusive numeric value for NUMBER value type. Can be provided alongside ExclusiveMaximum where both operate independently. Must be greater than or equal to Minimum and greater than ExclusiveMinimum. Applies to NUMBER and values within NUMBER\_LIST.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxLength`  <a name="cfn-connect-datatableattribute-validation-maxlength"></a>
The maximum number of characters a text value can contain. Applies to TEXT value type and values within a TEXT\_LIST. Must be greater than or equal to MinLength.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxValues`  <a name="cfn-connect-datatableattribute-validation-maxvalues"></a>
The maximum number of values in a list. Must be an integer greater than or equal to 0 and greater than or equal to MinValues. Applies to all list types.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Minimum`  <a name="cfn-connect-datatableattribute-validation-minimum"></a>
The smallest inclusive numeric value for NUMBER value type. Cannot be provided when ExclusiveMinimum is also provided. Must be less than or equal to Maximum and less than ExclusiveMaximum. Applies to NUMBER and values within NUMBER\_LIST.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinLength`  <a name="cfn-connect-datatableattribute-validation-minlength"></a>
The minimum number of characters a text value can contain. Applies to TEXT value type and values within a TEXT\_LIST. Must be less than or equal to MaxLength.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinValues`  <a name="cfn-connect-datatableattribute-validation-minvalues"></a>
The minimum number of values in a list. Must be an integer greater than or equal to 0 and less than or equal to MaxValues. Applies to all list types.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultipleOf`  <a name="cfn-connect-datatableattribute-validation-multipleof"></a>
Specifies that numeric values must be multiples of this number. Must be greater than 0. The result of dividing a value by this multiple must result in an integer. Applies to NUMBER and values within NUMBER\_LIST.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
