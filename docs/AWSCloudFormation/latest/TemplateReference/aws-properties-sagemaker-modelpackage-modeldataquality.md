---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-modeldataquality.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage ModelDataQuality
<a name="aws-properties-sagemaker-modelpackage-modeldataquality"></a>

Data quality constraints and statistics for a model.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-modeldataquality-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-modeldataquality-syntax.json"></a>

```
{
  "[Constraints](#cfn-sagemaker-modelpackage-modeldataquality-constraints)" : {{MetricsSource}},
  "[Statistics](#cfn-sagemaker-modelpackage-modeldataquality-statistics)" : {{MetricsSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-modeldataquality-syntax.yaml"></a>

```
  [Constraints](#cfn-sagemaker-modelpackage-modeldataquality-constraints): {{
    MetricsSource}}
  [Statistics](#cfn-sagemaker-modelpackage-modeldataquality-statistics): {{
    MetricsSource}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-modeldataquality-properties"></a>

`Constraints`  <a name="cfn-sagemaker-modelpackage-modeldataquality-constraints"></a>
Data quality constraints for a model.
*Required*: No
*Type*: [MetricsSource](aws-properties-sagemaker-modelpackage-metricssource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Statistics`  <a name="cfn-sagemaker-modelpackage-modeldataquality-statistics"></a>
Data quality statistics for a model.
*Required*: No
*Type*: [MetricsSource](aws-properties-sagemaker-modelpackage-metricssource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
