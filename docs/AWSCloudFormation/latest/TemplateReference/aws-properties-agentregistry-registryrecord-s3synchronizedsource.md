---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-s3synchronizedsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord S3SynchronizedSource

The Amazon S3 object version that the registry read when it last synchronized the record. At most one of `VersionId` and `ETag` is set.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-s3synchronizedsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-s3synchronizedsource-syntax.json"></a>

```json
{
  "[ETag](#cfn-agentregistry-registryrecord-s3synchronizedsource-etag)" : {{String}},
  "[SynchronizedAt](#cfn-agentregistry-registryrecord-s3synchronizedsource-synchronizedat)" : {{String}},
  "[VersionId](#cfn-agentregistry-registryrecord-s3synchronizedsource-versionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-s3synchronizedsource-syntax.yaml"></a>

```yaml
  [ETag](#cfn-agentregistry-registryrecord-s3synchronizedsource-etag): {{String}}
  [SynchronizedAt](#cfn-agentregistry-registryrecord-s3synchronizedsource-synchronizedat): {{String}}
  [VersionId](#cfn-agentregistry-registryrecord-s3synchronizedsource-versionid): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-s3synchronizedsource-properties"></a>

`ETag`  <a name="cfn-agentregistry-registryrecord-s3synchronizedsource-etag"></a>
The entity tag (ETag) of the object that the registry read, without quotes, when the object has no version ID. The registry doesn't record it for a SKILL.md source when the registry uses a customer managed AWS Key Management Service (AWS KMS) key.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SynchronizedAt`  <a name="cfn-agentregistry-registryrecord-s3synchronizedsource-synchronizedat"></a>
The timestamp when the registry read the source.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionId`  <a name="cfn-agentregistry-registryrecord-s3synchronizedsource-versionid"></a>
The version ID of the object that the registry read. Absent when the bucket isn't versioned.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
