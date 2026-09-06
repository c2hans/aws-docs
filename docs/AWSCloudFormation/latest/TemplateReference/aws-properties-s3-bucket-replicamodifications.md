---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-replicamodifications.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket ReplicaModifications
<a name="aws-properties-s3-bucket-replicamodifications"></a>

A filter that you can specify for selection for modifications on replicas.

## Syntax
<a name="aws-properties-s3-bucket-replicamodifications-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-replicamodifications-syntax.json"></a>

```
{
  "[Status](#cfn-s3-bucket-replicamodifications-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-replicamodifications-syntax.yaml"></a>

```
  [Status](#cfn-s3-bucket-replicamodifications-status): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-replicamodifications-properties"></a>

`Status`  <a name="cfn-s3-bucket-replicamodifications-status"></a>
Specifies whether Amazon S3 replicates modifications on replicas.
*Allowed values*: `Enabled` \| `Disabled`
*Required*: Yes
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
