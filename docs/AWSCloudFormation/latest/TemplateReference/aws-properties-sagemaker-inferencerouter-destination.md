---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencerouter-destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceRouter Destination

An endpoint or inference component that serves a routing target.

## Syntax
<a name="aws-properties-sagemaker-inferencerouter-destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencerouter-destination-syntax.json"></a>

```json
{
  "[ResourceArn](#cfn-sagemaker-inferencerouter-destination-resourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencerouter-destination-syntax.yaml"></a>

```yaml
  [ResourceArn](#cfn-sagemaker-inferencerouter-destination-resourcearn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferencerouter-destination-properties"></a>

`ResourceArn`  <a name="cfn-sagemaker-inferencerouter-destination-resourcearn"></a>
The Amazon Resource Name (ARN) of the endpoint or inference component. The destination can be in any account, and in any AWS Region in the same partition as the inference router. To use a destination in another account, its owner must allow your account to invoke it through your router, in an endpoint policy.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z-]*:sagemaker:[a-z0-9-]+:[0-9]{12}:(endpoint|inference-component)/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
