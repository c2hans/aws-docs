---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-recordtypeschemaoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry RecordTypeSchemaOverride
<a name="aws-properties-agentregistry-registry-recordtypeschemaoverride"></a>

A custom metadata schema override for a specific record type.

## Syntax
<a name="aws-properties-agentregistry-registry-recordtypeschemaoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-recordtypeschemaoverride-syntax.json"></a>

```
{
  "[RecordType](#cfn-agentregistry-registry-recordtypeschemaoverride-recordtype)" : {{String}},
  "[Schema](#cfn-agentregistry-registry-recordtypeschemaoverride-schema)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-recordtypeschemaoverride-syntax.yaml"></a>

```
  [RecordType](#cfn-agentregistry-registry-recordtypeschemaoverride-recordtype): {{String}}
  [Schema](#cfn-agentregistry-registry-recordtypeschemaoverride-schema): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registry-recordtypeschemaoverride-properties"></a>

`RecordType`  <a name="cfn-agentregistry-registry-recordtypeschemaoverride-recordtype"></a>
The record type that this schema override applies to.
*Required*: Yes
*Type*: String
*Allowed values*: `MCP | AGENT | SKILL | GATEWAY | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schema`  <a name="cfn-agentregistry-registry-recordtypeschemaoverride-schema"></a>
The JSON Schema for the specified record type. The schema can contain 1 to 10,240 characters. It must follow the same structural rules as the default schema.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
