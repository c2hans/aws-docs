---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelQualityJobDefinition ModelQualityBaselineConfig
<a name="aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig"></a>

Configuration for monitoring constraints and monitoring statistics. These baseline resources are compared against the results of the current job from the series of jobs scheduled to collect data periodically.

## Syntax
<a name="aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-syntax.json"></a>

```
{
  "[BaseliningJobName](#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-baseliningjobname)" : {{String}},
  "[ConstraintsResource](#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-constraintsresource)" : {{ConstraintsResource}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-syntax.yaml"></a>

```
  [BaseliningJobName](#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-baseliningjobname): {{String}}
  [ConstraintsResource](#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-constraintsresource): {{
    ConstraintsResource}}
```

## Properties
<a name="aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-properties"></a>

`BaseliningJobName`  <a name="cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-baseliningjobname"></a>
The name of the job that performs baselining for the monitoring job.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConstraintsResource`  <a name="cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-constraintsresource"></a>
The constraints resource for a monitoring job.
*Required*: No
*Type*: [ConstraintsResource](aws-properties-sagemaker-modelqualityjobdefinition-constraintsresource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
