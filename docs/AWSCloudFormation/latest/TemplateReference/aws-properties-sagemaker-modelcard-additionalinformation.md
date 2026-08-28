---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-additionalinformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard AdditionalInformation
<a name="aws-properties-sagemaker-modelcard-additionalinformation"></a>

Additional information about the model.

## Syntax
<a name="aws-properties-sagemaker-modelcard-additionalinformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-additionalinformation-syntax.json"></a>

```
{
  "[CaveatsAndRecommendations](#cfn-sagemaker-modelcard-additionalinformation-caveatsandrecommendations)" : {{String}},
  "[CustomDetails](#cfn-sagemaker-modelcard-additionalinformation-customdetails)" : {{{{{Key}}: {{Value}}, ...}}},
  "[EthicalConsiderations](#cfn-sagemaker-modelcard-additionalinformation-ethicalconsiderations)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-additionalinformation-syntax.yaml"></a>

```
  [CaveatsAndRecommendations](#cfn-sagemaker-modelcard-additionalinformation-caveatsandrecommendations): {{String}}
  [CustomDetails](#cfn-sagemaker-modelcard-additionalinformation-customdetails): {{
    {{Key}}: {{Value}}}}
  [EthicalConsiderations](#cfn-sagemaker-modelcard-additionalinformation-ethicalconsiderations): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-additionalinformation-properties"></a>

`CaveatsAndRecommendations`  <a name="cfn-sagemaker-modelcard-additionalinformation-caveatsandrecommendations"></a>
Caveats and recommendations for those who might use this model in their applications.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomDetails`  <a name="cfn-sagemaker-modelcard-additionalinformation-customdetails"></a>
Any additional information to document about the model.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z_][a-zA-Z0-9_]*`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EthicalConsiderations`  <a name="cfn-sagemaker-modelcard-additionalinformation-ethicalconsiderations"></a>
Any ethical considerations documented by the model card author.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
