---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-model-multimodelconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Model MultiModelConfig
<a name="aws-properties-sagemaker-model-multimodelconfig"></a>

Specifies additional configuration for hosting multi-model endpoints.

## Syntax
<a name="aws-properties-sagemaker-model-multimodelconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-model-multimodelconfig-syntax.json"></a>

```
{
  "[ModelCacheSetting](#cfn-sagemaker-model-multimodelconfig-modelcachesetting)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-model-multimodelconfig-syntax.yaml"></a>

```
  [ModelCacheSetting](#cfn-sagemaker-model-multimodelconfig-modelcachesetting): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-model-multimodelconfig-properties"></a>

`ModelCacheSetting`  <a name="cfn-sagemaker-model-multimodelconfig-modelcachesetting"></a>
Whether to cache models for a multi-model endpoint. By default, multi-model endpoints cache models so that a model does not have to be loaded into memory each time it is invoked. Some use cases do not benefit from model caching. For example, if an endpoint hosts a large number of models that are each invoked infrequently, the endpoint might perform better if you disable model caching. To disable model caching, set the value of this parameter to Disabled.
*Required*: No
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
