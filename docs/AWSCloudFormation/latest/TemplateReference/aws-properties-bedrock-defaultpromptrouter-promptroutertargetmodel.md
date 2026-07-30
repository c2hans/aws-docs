---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-defaultpromptrouter-promptroutertargetmodel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DefaultPromptRouter PromptRouterTargetModel
<a name="aws-properties-bedrock-defaultpromptrouter-promptroutertargetmodel"></a>

The target model for a prompt router.

## Syntax
<a name="aws-properties-bedrock-defaultpromptrouter-promptroutertargetmodel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-defaultpromptrouter-promptroutertargetmodel-syntax.json"></a>

```
{
  "[ModelArn](#cfn-bedrock-defaultpromptrouter-promptroutertargetmodel-modelarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-defaultpromptrouter-promptroutertargetmodel-syntax.yaml"></a>

```
  [ModelArn](#cfn-bedrock-defaultpromptrouter-promptroutertargetmodel-modelarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-defaultpromptrouter-promptroutertargetmodel-properties"></a>

`ModelArn`  <a name="cfn-bedrock-defaultpromptrouter-promptroutertargetmodel-modelarn"></a>
The target model's ARN.
*Required*: Yes
*Type*: String
*Pattern*: `(^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})|(^arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+)$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
