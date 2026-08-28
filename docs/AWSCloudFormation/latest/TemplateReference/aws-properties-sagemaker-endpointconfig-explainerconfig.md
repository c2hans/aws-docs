---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-explainerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig ExplainerConfig
<a name="aws-properties-sagemaker-endpointconfig-explainerconfig"></a>

A parameter to activate explainers.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-explainerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-explainerconfig-syntax.json"></a>

```
{
  "[ClarifyExplainerConfig](#cfn-sagemaker-endpointconfig-explainerconfig-clarifyexplainerconfig)" : {{ClarifyExplainerConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-explainerconfig-syntax.yaml"></a>

```
  [ClarifyExplainerConfig](#cfn-sagemaker-endpointconfig-explainerconfig-clarifyexplainerconfig): {{
    ClarifyExplainerConfig}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-explainerconfig-properties"></a>

`ClarifyExplainerConfig`  <a name="cfn-sagemaker-endpointconfig-explainerconfig-clarifyexplainerconfig"></a>
A member of `ExplainerConfig` that contains configuration parameters for the SageMaker Clarify explainer.
*Required*: No
*Type*: [ClarifyExplainerConfig](aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
