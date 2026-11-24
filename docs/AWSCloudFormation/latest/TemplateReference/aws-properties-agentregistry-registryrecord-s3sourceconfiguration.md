---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-s3sourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord S3SourceConfiguration

The settings of a skill source that the registry reads from Amazon S3.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-s3sourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-s3sourceconfiguration-syntax.json"></a>

```json
{
  "[BucketOwnerAccountId](#cfn-agentregistry-registryrecord-s3sourceconfiguration-bucketowneraccountid)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-s3sourceconfiguration-syntax.yaml"></a>

```yaml
  [BucketOwnerAccountId](#cfn-agentregistry-registryrecord-s3sourceconfiguration-bucketowneraccountid): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-s3sourceconfiguration-properties"></a>

`BucketOwnerAccountId`  <a name="cfn-agentregistry-registryrecord-s3sourceconfiguration-bucketowneraccountid"></a>
The ID of the AWS account that owns the source bucket. The registry checks that the bucket belongs to this account each time it reads the source.
If you omit it for a source that uses an IAM role, the registry expects the bucket to be in the role's account. A source without a credential provider, which the registry reads as a publicly readable object, requires it.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
