---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-principalpermissions-catalogresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::PrincipalPermissions CatalogResource
<a name="aws-properties-lakeformation-principalpermissions-catalogresource"></a>

A structure for the catalog object.

 This is an object with no properties that effectively behaves as a true or false. A valid input for this property type in both yaml or json is null or `{}`.

## Syntax
<a name="aws-properties-lakeformation-principalpermissions-catalogresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-principalpermissions-catalogresource-syntax.json"></a>

```
{
  "[Id](#cfn-lakeformation-principalpermissions-catalogresource-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-principalpermissions-catalogresource-syntax.yaml"></a>

```
  [Id](#cfn-lakeformation-principalpermissions-catalogresource-id): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-principalpermissions-catalogresource-properties"></a>

`Id`  <a name="cfn-lakeformation-principalpermissions-catalogresource-id"></a>
An identifier for the catalog resource.
*Required*: No
*Type*: String
*Minimum*: `12`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
