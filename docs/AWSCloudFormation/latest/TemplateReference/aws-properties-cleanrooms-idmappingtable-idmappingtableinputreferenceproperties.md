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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
