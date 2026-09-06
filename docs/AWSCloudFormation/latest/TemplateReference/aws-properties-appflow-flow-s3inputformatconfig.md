---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-s3inputformatconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow S3InputFormatConfig
<a name="aws-properties-appflow-flow-s3inputformatconfig"></a>

 When you use Amazon S3 as the source, the configuration format that you provide the flow input data.

## Syntax
<a name="aws-properties-appflow-flow-s3inputformatconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-s3inputformatconfig-syntax.json"></a>

```
{
  "[S3InputFileType](#cfn-appflow-flow-s3inputformatconfig-s3inputfiletype)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-s3inputformatconfig-syntax.yaml"></a>

```
  [S3InputFileType](#cfn-appflow-flow-s3inputformatconfig-s3inputfiletype): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-s3inputformatconfig-properties"></a>

`S3InputFileType`  <a name="cfn-appflow-flow-s3inputformatconfig-s3inputfiletype"></a>
 The file type that Amazon AppFlow gets from your Amazon S3 bucket.
*Required*: No
*Type*: String
*Allowed values*: `CSV | JSON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
