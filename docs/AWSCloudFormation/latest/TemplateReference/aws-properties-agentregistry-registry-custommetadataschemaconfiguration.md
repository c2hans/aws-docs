---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-custommetadataschemaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry CustomMetadataSchemaConfiguration
<a name="aws-properties-agentregistry-registry-custommetadataschemaconfiguration"></a>

The custom metadata fields that records in the registry can carry. `defaultSchema` defines the common attributes for every record type, and `recordTypeSchemaOverrides` adds fields for individual record types.

## Syntax
<a name="aws-properties-agentregistry-registry-custommetadataschemaconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-custommetadataschemaconfiguration-syntax.json"></a>

```
{
  "[DefaultSchema](#cfn-agentregistry-registry-custommetadataschemaconfiguration-defaultschema)" : {{String}},
  "[RecordTypeSchemaOverrides](#cfn-agentregistry-registry-custommetadataschemaconfiguration-recordtypeschemaoverrides)" : {{[ RecordTypeSchemaOverride, ... ]}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-custommetadataschemaconfiguration-syntax.yaml"></a>

```
  [DefaultSchema](#cfn-agentregistry-registry-custommetadataschemaconfiguration-defaultschema): {{String}}
  [RecordTypeSchemaOverrides](#cfn-agentregistry-registry-custommetadataschemaconfiguration-recordtypeschemaoverrides): {{
    - RecordTypeSchemaOverride}}
```

## Properties
<a name="aws-properties-agentregistry-registry-custommetadataschemaconfiguration-properties"></a>

`DefaultSchema`  <a name="cfn-agentregistry-registry-custommetadataschemaconfiguration-defaultschema"></a>
A JSON Schema with the common attributes: fields that records of every record type can carry.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordTypeSchemaOverrides`  <a name="cfn-agentregistry-registry-custommetadataschemaconfiguration-recordtypeschemaoverrides"></a>
The fields for individual record types. Records of a record type can carry the common attributes defined in `defaultSchema` plus that record type's fields.
*Required*: No
*Type*: Array of [RecordTypeSchemaOverride](aws-properties-agentregistry-registry-recordtypeschemaoverride.md)
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
