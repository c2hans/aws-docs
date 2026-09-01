---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-scaleinpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig ScaleInPolicy
<a name="aws-properties-sagemaker-endpointconfig-scaleinpolicy"></a>

<a name="aws-properties-sagemaker-endpointconfig-scaleinpolicy-description"></a>The `ScaleInPolicy` property type specifies Property description not available. for an [AWS::SageMaker::EndpointConfig](aws-resource-sagemaker-endpointconfig.md).

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-scaleinpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-scaleinpolicy-syntax.json"></a>

```
{
  "[CooldownInMinutes](#cfn-sagemaker-endpointconfig-scaleinpolicy-cooldowninminutes)" : {{Integer}},
  "[MaximumStepSize](#cfn-sagemaker-endpointconfig-scaleinpolicy-maximumstepsize)" : {{Integer}},
  "[Strategy](#cfn-sagemaker-endpointconfig-scaleinpolicy-strategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-scaleinpolicy-syntax.yaml"></a>

```
  [CooldownInMinutes](#cfn-sagemaker-endpointconfig-scaleinpolicy-cooldowninminutes): {{Integer}}
  [MaximumStepSize](#cfn-sagemaker-endpointconfig-scaleinpolicy-maximumstepsize): {{Integer}}
  [Strategy](#cfn-sagemaker-endpointconfig-scaleinpolicy-strategy): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-scaleinpolicy-properties"></a>

`CooldownInMinutes`  <a name="cfn-sagemaker-endpointconfig-scaleinpolicy-cooldowninminutes"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaximumStepSize`  <a name="cfn-sagemaker-endpointconfig-scaleinpolicy-maximumstepsize"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Strategy`  <a name="cfn-sagemaker-endpointconfig-scaleinpolicy-strategy"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
