---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ApplicationInferenceProfile InferenceProfileModel
<a name="aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodel"></a>

Contains information about a model.

## Syntax
<a name="aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodel-syntax.json"></a>

```
{
  "[ModelArn](#cfn-bedrock-applicationinferenceprofile-inferenceprofilemodel-modelarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodel-syntax.yaml"></a>

```
  [ModelArn](#cfn-bedrock-applicationinferenceprofile-inferenceprofilemodel-modelarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodel-properties"></a>

`ModelArn`  <a name="cfn-bedrock-applicationinferenceprofile-inferenceprofilemodel-modelarn"></a>
The Amazon Resource Name (ARN) of the model.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
