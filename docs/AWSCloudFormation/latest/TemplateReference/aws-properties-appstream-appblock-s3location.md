---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-appblock-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::AppBlock S3Location
<a name="aws-properties-appstream-appblock-s3location"></a>

The S3 location of the app block.

## Syntax
<a name="aws-properties-appstream-appblock-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-appblock-s3location-syntax.json"></a>

```
{
  "[S3Bucket](#cfn-appstream-appblock-s3location-s3bucket)" : {{String}},
  "[S3Key](#cfn-appstream-appblock-s3location-s3key)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-appblock-s3location-syntax.yaml"></a>

```
  [S3Bucket](#cfn-appstream-appblock-s3location-s3bucket): {{String}}
  [S3Key](#cfn-appstream-appblock-s3location-s3key): {{String}}
```

## Properties
<a name="aws-properties-appstream-appblock-s3location-properties"></a>

`S3Bucket`  <a name="cfn-appstream-appblock-s3location-s3bucket"></a>
The S3 bucket of the app block.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Key`  <a name="cfn-appstream-appblock-s3location-s3key"></a>
The S3 key of the S3 object of the virtual hard disk.
This is required when it's used by `SetupScriptDetails` and `PostSetupScriptDetails`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
