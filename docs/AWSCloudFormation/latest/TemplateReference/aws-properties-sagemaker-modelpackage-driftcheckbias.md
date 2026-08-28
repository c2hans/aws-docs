---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-driftcheckbias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage DriftCheckBias
<a name="aws-properties-sagemaker-modelpackage-driftcheckbias"></a>

Represents the drift check bias baselines that can be used when the model monitor is set using the model package.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-driftcheckbias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-driftcheckbias-syntax.json"></a>

```
{
  "[ConfigFile](#cfn-sagemaker-modelpackage-driftcheckbias-configfile)" : {{FileSource}},
  "[PostTrainingConstraints](#cfn-sagemaker-modelpackage-driftcheckbias-posttrainingconstraints)" : {{MetricsSource}},
  "[PreTrainingConstraints](#cfn-sagemaker-modelpackage-driftcheckbias-pretrainingconstraints)" : {{MetricsSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-driftcheckbias-syntax.yaml"></a>

```
  [ConfigFile](#cfn-sagemaker-modelpackage-driftcheckbias-configfile): {{
    FileSource}}
  [PostTrainingConstraints](#cfn-sagemaker-modelpackage-driftcheckbias-posttrainingconstraints): {{
    MetricsSource}}
  [PreTrainingConstraints](#cfn-sagemaker-modelpackage-driftcheckbias-pretrainingconstraints): {{
    MetricsSource}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-driftcheckbias-properties"></a>

`ConfigFile`  <a name="cfn-sagemaker-modelpackage-driftcheckbias-configfile"></a>
The bias config file for a model.
*Required*: No
*Type*: [FileSource](aws-properties-sagemaker-modelpackage-filesource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PostTrainingConstraints`  <a name="cfn-sagemaker-modelpackage-driftcheckbias-posttrainingconstraints"></a>
The post-training constraints.
*Required*: No
*Type*: [MetricsSource](aws-properties-sagemaker-modelpackage-metricssource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreTrainingConstraints`  <a name="cfn-sagemaker-modelpackage-driftcheckbias-pretrainingconstraints"></a>
The pre-training constraints.
*Required*: No
*Type*: [MetricsSource](aws-properties-sagemaker-modelpackage-metricssource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
