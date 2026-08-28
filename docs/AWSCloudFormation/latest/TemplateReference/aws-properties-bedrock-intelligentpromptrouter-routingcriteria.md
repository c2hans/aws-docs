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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
