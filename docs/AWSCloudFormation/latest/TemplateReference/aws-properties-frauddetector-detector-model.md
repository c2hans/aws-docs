---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-frauddetector-detector-model.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FraudDetector::Detector Model
<a name="aws-properties-frauddetector-detector-model"></a>

The model.

## Syntax
<a name="aws-properties-frauddetector-detector-model-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-frauddetector-detector-model-syntax.json"></a>

```
{
  "[Arn](#cfn-frauddetector-detector-model-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-frauddetector-detector-model-syntax.yaml"></a>

```
  [Arn](#cfn-frauddetector-detector-model-arn): {{String}}
```

## Properties
<a name="aws-properties-frauddetector-detector-model-properties"></a>

`Arn`  <a name="cfn-frauddetector-detector-model-arn"></a>
The ARN of the model.
*Required*: No
*Type*: String
*Pattern*: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
