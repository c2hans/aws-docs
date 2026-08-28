---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelExplainabilityJobDefinition ModelExplainabilityAppSpecification
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification"></a>

Docker container image configuration object for the model explainability job.

## Syntax
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-syntax.json"></a>

```
{
  "[ConfigUri](#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-configuri)" : {{String}},
  "[Environment](#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-environment)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ImageUri](#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-imageuri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-syntax.yaml"></a>

```
  [ConfigUri](#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-configuri): {{String}}
  [Environment](#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-environment): {{
    {{Key}}: {{Value}}}}
  [ImageUri](#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-imageuri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-properties"></a>

`ConfigUri`  <a name="cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-configuri"></a>
JSON formatted Amazon S3 file that defines explainability parameters. For more information on this JSON configuration file, see [Configure model explainability parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-config-json-monitor-model-explainability-parameters.html).
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-environment"></a>
Sets the environment variables in the Docker container.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z_][a-zA-Z0-9_]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageUri`  <a name="cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-imageuri"></a>
The container image to be run by the model explainability job.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
