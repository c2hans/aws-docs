---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-recordtypeschemaoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry RecordTypeSchemaOverride
<a name="aws-properties-agentregistry-registry-recordtypeschemaoverride"></a>

The custom metadata fields for one record type, in addition to the common attributes defined in `defaultSchema`.

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
The record type these fields apply to.
*Required*: Yes
*Type*: String
*Allowed values*: `MCP | AGENT | SKILL | GATEWAY | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schema`  <a name="cfn-agentregistry-registry-recordtypeschemaoverride-schema"></a>
A JSON Schema with the fields for this record type.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
