---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-entityresolution-schemamapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::SchemaMapping
<a name="aws-resource-entityresolution-schemamapping"></a>

Creates a schema mapping, which defines the schema of the input customer records table. The `SchemaMapping` also provides AWS Entity Resolution with some metadata about the table, such as the attribute types of the columns and which columns to match on.

## Syntax
<a name="aws-resource-entityresolution-schemamapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-entityresolution-schemamapping-syntax.json"></a>

```
{
  "Type" : "AWS::EntityResolution::SchemaMapping",
  "Properties" : {
      "[Description](#cfn-entityresolution-schemamapping-description)" : {{String}},
      "[MappedInputFields](#cfn-entityresolution-schemamapping-mappedinputfields)" : {{[ SchemaInputAttribute, ... ]}},
      "[SchemaName](#cfn-entityresolution-schemamapping-schemaname)" : {{String}},
      "[Tags](#cfn-entityresolution-schemamapping-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-entityresolution-schemamapping-syntax.yaml"></a>

```
Type: AWS::EntityResolution::SchemaMapping
Properties:
  [Description](#cfn-entityresolution-schemamapping-description): {{String}}
  [MappedInputFields](#cfn-entityresolution-schemamapping-mappedinputfields): {{
    - SchemaInputAttribute}}
  [SchemaName](#cfn-entityresolution-schemamapping-schemaname): {{String}}
  [Tags](#cfn-entityresolution-schemamapping-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-entityresolution-schemamapping-properties"></a>

`Description`  <a name="cfn-entityresolution-schemamapping-description"></a>
A description of the schema.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MappedInputFields`  <a name="cfn-entityresolution-schemamapping-mappedinputfields"></a>
A list of `MappedInputFields`. Each `MappedInputField` corresponds to a column the source data table, and contains column name plus additional information that AWS Entity Resolution uses for matching.
*Required*: Yes
*Type*: Array of [SchemaInputAttribute](aws-properties-entityresolution-schemamapping-schemainputattribute.md)
*Minimum*: `2`
*Maximum*: `35`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaName`  <a name="cfn-entityresolution-schemamapping-schemaname"></a>
The name of the schema. There can't be multiple `SchemaMappings` with the same name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_0-9-]*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-entityresolution-schemamapping-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-entityresolution-schemamapping-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
