---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-readset-readsets3access.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::ReadSet ReadSetS3Access
<a name="aws-properties-omics-readset-readsets3access"></a>

<a name="aws-properties-omics-readset-readsets3access-description"></a>The `ReadSetS3Access` property type specifies Property description not available. for an [AWS::Omics::ReadSet](aws-resource-omics-readset.md).

## Syntax
<a name="aws-properties-omics-readset-readsets3access-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-readset-readsets3access-syntax.json"></a>

```
{
  "[S3Uri](#cfn-omics-readset-readsets3access-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-omics-readset-readsets3access-syntax.yaml"></a>

```
  [S3Uri](#cfn-omics-readset-readsets3access-s3uri): {{String}}
```

## Properties
<a name="aws-properties-omics-readset-readsets3access-properties"></a>

`S3Uri`  <a name="cfn-omics-readset-readsets3access-s3uri"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/(.{1,1024})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
