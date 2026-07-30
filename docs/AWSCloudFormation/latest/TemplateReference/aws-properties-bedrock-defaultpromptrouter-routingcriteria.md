---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-defaultpromptrouter-routingcriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DefaultPromptRouter RoutingCriteria
<a name="aws-properties-bedrock-defaultpromptrouter-routingcriteria"></a>

Routing criteria for a prompt router.

## Syntax
<a name="aws-properties-bedrock-defaultpromptrouter-routingcriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-defaultpromptrouter-routingcriteria-syntax.json"></a>

```
{
  "[ResponseQualityDifference](#cfn-bedrock-defaultpromptrouter-routingcriteria-responsequalitydifference)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrock-defaultpromptrouter-routingcriteria-syntax.yaml"></a>

```
  [ResponseQualityDifference](#cfn-bedrock-defaultpromptrouter-routingcriteria-responsequalitydifference): {{Number}}
```

## Properties
<a name="aws-properties-bedrock-defaultpromptrouter-routingcriteria-properties"></a>

`ResponseQualityDifference`  <a name="cfn-bedrock-defaultpromptrouter-routingcriteria-responsequalitydifference"></a>
The criteria's response quality difference.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
