---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-custommetadataschemaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry CustomMetadataSchemaConfiguration
<a name="aws-properties-agentregistry-registry-custommetadataschemaconfiguration"></a>

Configuration that defines a typed custom metadata schema for a registry. A default schema and schema overrides for specific record types are both optional.

Schema evolution is additive only. You can add fields and enum values. You can't remove fields, change field types, or remove enum values.

If you remove this configuration from the template during a stack update, the existing schema isn't cleared. The service keeps the current schema.

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
The default JSON Schema for custom metadata. It applies to record types that don't have a schema override. The schema can contain 1 to 10,240 characters.
Supported property types are string, string with an enum constraint, string with a `uri` format, and boolean.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordTypeSchemaOverrides`  <a name="cfn-agentregistry-registry-custommetadataschemaconfiguration-recordtypeschemaoverrides"></a>
A list of schema overrides for specific record types. You can specify up to 5 overrides. When a record's type matches an override, the service uses that override's schema instead of the default schema for validation.
*Required*: No
*Type*: Array of [RecordTypeSchemaOverride](aws-properties-agentregistry-registry-recordtypeschemaoverride.md)
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
