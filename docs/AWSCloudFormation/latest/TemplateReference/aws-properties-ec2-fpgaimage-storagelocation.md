---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-fpgaimage-storagelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FpgaImage StorageLocation
<a name="aws-properties-ec2-fpgaimage-storagelocation"></a>

Describes a storage location in Amazon S3.

## Syntax
<a name="aws-properties-ec2-fpgaimage-storagelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-fpgaimage-storagelocation-syntax.json"></a>

```
{
  "[Bucket](#cfn-ec2-fpgaimage-storagelocation-bucket)" : {{String}},
  "[Key](#cfn-ec2-fpgaimage-storagelocation-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-fpgaimage-storagelocation-syntax.yaml"></a>

```
  [Bucket](#cfn-ec2-fpgaimage-storagelocation-bucket): {{String}}
  [Key](#cfn-ec2-fpgaimage-storagelocation-key): {{String}}
```

## Properties
<a name="aws-properties-ec2-fpgaimage-storagelocation-properties"></a>

`Bucket`  <a name="cfn-ec2-fpgaimage-storagelocation-bucket"></a>
The name of the S3 bucket.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Key`  <a name="cfn-ec2-fpgaimage-storagelocation-key"></a>
The key.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
