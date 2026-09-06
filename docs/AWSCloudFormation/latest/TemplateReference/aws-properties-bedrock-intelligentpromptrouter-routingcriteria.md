---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-intelligentpromptrouter-routingcriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::IntelligentPromptRouter RoutingCriteria
<a name="aws-properties-bedrock-intelligentpromptrouter-routingcriteria"></a>

Routing criteria for a prompt router.

## Syntax
<a name="aws-properties-bedrock-intelligentpromptrouter-routingcriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-intelligentpromptrouter-routingcriteria-syntax.json"></a>

```
{
  "[ResponseQualityDifference](#cfn-bedrock-intelligentpromptrouter-routingcriteria-responsequalitydifference)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrock-intelligentpromptrouter-routingcriteria-syntax.yaml"></a>

```
  [ResponseQualityDifference](#cfn-bedrock-intelligentpromptrouter-routingcriteria-responsequalitydifference): {{Number}}
```

## Properties
<a name="aws-properties-bedrock-intelligentpromptrouter-routingcriteria-properties"></a>

`ResponseQualityDifference`  <a name="cfn-bedrock-intelligentpromptrouter-routingcriteria-responsequalitydifference"></a>
The criteria's response quality difference.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
