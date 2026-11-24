---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-registryrecordsynchronizedsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord RegistryRecordSynchronizedSource

The source that a skill record's content was last synchronized from. Exactly one member is set, for the source's provider.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-registryrecordsynchronizedsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-registryrecordsynchronizedsource-syntax.json"></a>

```json
{
  "[S3](#cfn-agentregistry-registryrecord-registryrecordsynchronizedsource-s3)" : {{S3SynchronizedSource}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-registryrecordsynchronizedsource-syntax.yaml"></a>

```yaml
  [S3](#cfn-agentregistry-registryrecord-registryrecordsynchronizedsource-s3): {{
    S3SynchronizedSource}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-registryrecordsynchronizedsource-properties"></a>

`S3`  <a name="cfn-agentregistry-registryrecord-registryrecordsynchronizedsource-s3"></a>
The Amazon S3 source that the registry read.
*Required*: Yes
*Type*: [S3SynchronizedSource](aws-properties-agentregistry-registryrecord-s3synchronizedsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
