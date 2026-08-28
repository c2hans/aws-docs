---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-application-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Application S3Location
<a name="aws-properties-appstream-application-s3location"></a>

The S3 location of the application icon.

## Syntax
<a name="aws-properties-appstream-application-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-application-s3location-syntax.json"></a>

```
{
  "[S3Bucket](#cfn-appstream-application-s3location-s3bucket)" : {{String}},
  "[S3Key](#cfn-appstream-application-s3location-s3key)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-application-s3location-syntax.yaml"></a>

```
  [S3Bucket](#cfn-appstream-application-s3location-s3bucket): {{String}}
  [S3Key](#cfn-appstream-application-s3location-s3key): {{String}}
```

## Properties
<a name="aws-properties-appstream-application-s3location-properties"></a>

`S3Bucket`  <a name="cfn-appstream-application-s3location-s3bucket"></a>
The S3 bucket of the S3 object.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Key`  <a name="cfn-appstream-application-s3location-s3key"></a>
The S3 key of the S3 object.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
