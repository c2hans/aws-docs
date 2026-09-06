---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IdMappingTable IdMappingTableInputReferenceProperties
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties"></a>

The input reference properties for the ID mapping table.

## Syntax
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties-syntax.json"></a>

```
{
  "[IdMappingTableInputSource](#cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties-idmappingtableinputsource)" : {{[ IdMappingTableInputSource, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties-syntax.yaml"></a>

```
  [IdMappingTableInputSource](#cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties-idmappingtableinputsource): {{
    - IdMappingTableInputSource}}
```

## Properties
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties-properties"></a>

`IdMappingTableInputSource`  <a name="cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties-idmappingtableinputsource"></a>
The input source of the ID mapping table.
*Required*: Yes
*Type*: [Array](aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource.md) of [IdMappingTableInputSource](aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
