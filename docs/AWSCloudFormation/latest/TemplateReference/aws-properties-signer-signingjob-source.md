---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-signer-signingjob-source.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Signer::SigningJob Source
<a name="aws-properties-signer-signingjob-source"></a>

An `S3Source` object that contains information about the S3 bucket where you saved your unsigned code.

## Syntax
<a name="aws-properties-signer-signingjob-source-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-signer-signingjob-source-syntax.json"></a>

```
{
  "[S3](#cfn-signer-signingjob-source-s3)" : {{S3Source}}
}
```

### YAML
<a name="aws-properties-signer-signingjob-source-syntax.yaml"></a>

```
  [S3](#cfn-signer-signingjob-source-s3): {{
    S3Source}}
```

## Properties
<a name="aws-properties-signer-signingjob-source-properties"></a>

`S3`  <a name="cfn-signer-signingjob-source-s3"></a>
The `S3Source` object.
*Required*: No
*Type*: [S3Source](aws-properties-signer-signingjob-s3source.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
