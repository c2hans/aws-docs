---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-metricssource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage MetricsSource
<a name="aws-properties-sagemaker-modelpackage-metricssource"></a>

Details about the metrics source.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-metricssource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-metricssource-syntax.json"></a>

```
{
  "[ContentDigest](#cfn-sagemaker-modelpackage-metricssource-contentdigest)" : {{String}},
  "[ContentType](#cfn-sagemaker-modelpackage-metricssource-contenttype)" : {{String}},
  "[S3Uri](#cfn-sagemaker-modelpackage-metricssource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-metricssource-syntax.yaml"></a>

```
  [ContentDigest](#cfn-sagemaker-modelpackage-metricssource-contentdigest): {{String}}
  [ContentType](#cfn-sagemaker-modelpackage-metricssource-contenttype): {{String}}
  [S3Uri](#cfn-sagemaker-modelpackage-metricssource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-metricssource-properties"></a>

`ContentDigest`  <a name="cfn-sagemaker-modelpackage-metricssource-contentdigest"></a>
The hash key used for the metrics source.
*Required*: No
*Type*: String
*Pattern*: `^[Ss][Hh][Aa]256:[0-9a-fA-F]{64}$`
*Maximum*: `72`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContentType`  <a name="cfn-sagemaker-modelpackage-metricssource-contenttype"></a>
The metric source content type.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-sagemaker-modelpackage-metricssource-s3uri"></a>
The S3 URI for the metrics source.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
