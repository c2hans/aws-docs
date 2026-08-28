---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-filesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage FileSource
<a name="aws-properties-sagemaker-modelpackage-filesource"></a>

Contains details regarding the file source.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-filesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-filesource-syntax.json"></a>

```
{
  "[ContentDigest](#cfn-sagemaker-modelpackage-filesource-contentdigest)" : {{String}},
  "[ContentType](#cfn-sagemaker-modelpackage-filesource-contenttype)" : {{String}},
  "[S3Uri](#cfn-sagemaker-modelpackage-filesource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-filesource-syntax.yaml"></a>

```
  [ContentDigest](#cfn-sagemaker-modelpackage-filesource-contentdigest): {{String}}
  [ContentType](#cfn-sagemaker-modelpackage-filesource-contenttype): {{String}}
  [S3Uri](#cfn-sagemaker-modelpackage-filesource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-filesource-properties"></a>

`ContentDigest`  <a name="cfn-sagemaker-modelpackage-filesource-contentdigest"></a>
The digest of the file source.
*Required*: No
*Type*: String
*Pattern*: `^[Ss][Hh][Aa]256:[0-9a-fA-F]{64}$`
*Maximum*: `72`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContentType`  <a name="cfn-sagemaker-modelpackage-filesource-contenttype"></a>
The type of content stored in the file source.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-sagemaker-modelpackage-filesource-s3uri"></a>
The Amazon S3 URI for the file source.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
