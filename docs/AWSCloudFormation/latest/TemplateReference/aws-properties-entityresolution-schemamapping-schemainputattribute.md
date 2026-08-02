---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-schemamapping-schemainputattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::SchemaMapping SchemaInputAttribute
<a name="aws-properties-entityresolution-schemamapping-schemainputattribute"></a>

A configuration object for defining input data fields in AWS Entity Resolution. The `SchemaInputAttribute` specifies how individual fields in your input data should be processed and matched.

## Syntax
<a name="aws-properties-entityresolution-schemamapping-schemainputattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-schemamapping-schemainputattribute-syntax.json"></a>

```
{
  "[FieldName](#cfn-entityresolution-schemamapping-schemainputattribute-fieldname)" : {{String}},
  "[GroupName](#cfn-entityresolution-schemamapping-schemainputattribute-groupname)" : {{String}},
  "[Hashed](#cfn-entityresolution-schemamapping-schemainputattribute-hashed)" : {{Boolean}},
  "[MatchKey](#cfn-entityresolution-schemamapping-schemainputattribute-matchkey)" : {{String}},
  "[SubType](#cfn-entityresolution-schemamapping-schemainputattribute-subtype)" : {{String}},
  "[Type](#cfn-entityresolution-schemamapping-schemainputattribute-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-schemamapping-schemainputattribute-syntax.yaml"></a>

```
  [FieldName](#cfn-entityresolution-schemamapping-schemainputattribute-fieldname): {{String}}
  [GroupName](#cfn-entityresolution-schemamapping-schemainputattribute-groupname): {{String}}
  [Hashed](#cfn-entityresolution-schemamapping-schemainputattribute-hashed): {{Boolean}}
  [MatchKey](#cfn-entityresolution-schemamapping-schemainputattribute-matchkey): {{String}}
  [SubType](#cfn-entityresolution-schemamapping-schemainputattribute-subtype): {{String}}
  [Type](#cfn-entityresolution-schemamapping-schemainputattribute-type): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-schemamapping-schemainputattribute-properties"></a>

`FieldName`  <a name="cfn-entityresolution-schemamapping-schemainputattribute-fieldname"></a>
A string containing the field name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_0-9- \t]*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupName`  <a name="cfn-entityresolution-schemamapping-schemainputattribute-groupname"></a>
A string that instructs AWS Entity Resolution to combine several columns into a unified column with the identical attribute type.
For example, when working with columns such as `NAME_FIRST`, `NAME_MIDDLE`, and `NAME_LAST`, assigning them a common `groupName` will prompt AWS Entity Resolution to concatenate them into a single value.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z_0-9- \t]*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Hashed`  <a name="cfn-entityresolution-schemamapping-schemainputattribute-hashed"></a>
 Indicates if the column values are hashed in the schema input.
If the value is set to `TRUE`, the column values are hashed.
If the value is set to `FALSE`, the column values are cleartext.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchKey`  <a name="cfn-entityresolution-schemamapping-schemainputattribute-matchkey"></a>
A key that allows grouping of multiple input attributes into a unified matching group.
For example, consider a scenario where the source table contains various addresses, such as `business_address` and `shipping_address`. By assigning a `matchKey` called `address` to both attributes, AWS Entity Resolution will match records across these fields to create a consolidated matching group.
If no `matchKey` is specified for a column, it won't be utilized for matching purposes but will still be included in the output table.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z_0-9- \t]*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubType`  <a name="cfn-entityresolution-schemamapping-schemainputattribute-subtype"></a>
The subtype of the attribute, selected from a list of values.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-entityresolution-schemamapping-schemainputattribute-type"></a>
The type of the attribute, selected from a list of values.
LiveRamp supports: `NAME` \| `NAME_FIRST` \| `NAME_MIDDLE` \| `NAME_LAST` \| `ADDRESS` \| `ADDRESS_STREET1` \| `ADDRESS_STREET2` \| `ADDRESS_STREET3` \| `ADDRESS_CITY` \| `ADDRESS_STATE` \| `ADDRESS_COUNTRY` \| `ADDRESS_POSTALCODE` \| `PHONE` \| `PHONE_NUMBER` \| `EMAIL_ADDRESS` \| `UNIQUE_ID` \| `PROVIDER_ID`
TransUnion supports: `NAME` \| `NAME_FIRST` \| `NAME_LAST` \| `ADDRESS` \| `ADDRESS_CITY` \| `ADDRESS_STATE` \| `ADDRESS_COUNTRY` \| `ADDRESS_POSTALCODE` \| `PHONE_NUMBER` \| `EMAIL_ADDRESS` \| `UNIQUE_ID` \| `IPV4` \| `IPV6` \| `MAID`
Unified ID 2.0 supports: `PHONE_NUMBER` \| `EMAIL_ADDRESS` \| `UNIQUE_ID`
Normalization is only supported for `NAME`, `ADDRESS`, `PHONE`, and `EMAIL_ADDRESS`.
If you want to normalize `NAME_FIRST`, `NAME_MIDDLE`, and `NAME_LAST`, you must group them by assigning them to the `NAME``groupName`.
If you want to normalize `ADDRESS_STREET1`, `ADDRESS_STREET2`, `ADDRESS_STREET3`, `ADDRESS_CITY`, `ADDRESS_STATE`, `ADDRESS_COUNTRY`, and `ADDRESS_POSTALCODE`, you must group them by assigning them to the `ADDRESS``groupName`.
If you want to normalize `PHONE_NUMBER` and `PHONE_COUNTRYCODE`, you must group them by assigning them to the `PHONE``groupName`.
*Required*: Yes
*Type*: String
*Allowed values*: `NAME | NAME_FIRST | NAME_MIDDLE | NAME_LAST | ADDRESS | ADDRESS_STREET1 | ADDRESS_STREET2 | ADDRESS_STREET3 | ADDRESS_CITY | ADDRESS_STATE | ADDRESS_COUNTRY | ADDRESS_POSTALCODE | PHONE | PHONE_NUMBER | PHONE_COUNTRYCODE | EMAIL_ADDRESS | UNIQUE_ID | DATE | STRING | PROVIDER_ID`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
