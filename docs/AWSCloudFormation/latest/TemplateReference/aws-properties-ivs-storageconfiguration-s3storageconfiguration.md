---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-storageconfiguration-s3storageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::StorageConfiguration S3StorageConfiguration
<a name="aws-properties-ivs-storageconfiguration-s3storageconfiguration"></a>

The S3StorageConfiguration property type describes an S3 location where recorded videos will be stored.

## Syntax
<a name="aws-properties-ivs-storageconfiguration-s3storageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-storageconfiguration-s3storageconfiguration-syntax.json"></a>

```
{
  "[BucketName](#cfn-ivs-storageconfiguration-s3storageconfiguration-bucketname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ivs-storageconfiguration-s3storageconfiguration-syntax.yaml"></a>

```
  [BucketName](#cfn-ivs-storageconfiguration-s3storageconfiguration-bucketname): {{String}}
```

## Properties
<a name="aws-properties-ivs-storageconfiguration-s3storageconfiguration-properties"></a>

`BucketName`  <a name="cfn-ivs-storageconfiguration-s3storageconfiguration-bucketname"></a>
Name of the S3 bucket where recorded video will be stored.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9-.]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
