---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiguardrail-aiguardrailtopicpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIGuardrail AIGuardrailTopicPolicyConfig
<a name="aws-properties-wisdom-aiguardrail-aiguardrailtopicpolicyconfig"></a>

Topic policy configuration for a guardrail.

## Syntax
<a name="aws-properties-wisdom-aiguardrail-aiguardrailtopicpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiguardrail-aiguardrailtopicpolicyconfig-syntax.json"></a>

```
{
  "[TopicsConfig](#cfn-wisdom-aiguardrail-aiguardrailtopicpolicyconfig-topicsconfig)" : {{[ GuardrailTopicConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-wisdom-aiguardrail-aiguardrailtopicpolicyconfig-syntax.yaml"></a>

```
  [TopicsConfig](#cfn-wisdom-aiguardrail-aiguardrailtopicpolicyconfig-topicsconfig): {{
    - GuardrailTopicConfig}}
```

## Properties
<a name="aws-properties-wisdom-aiguardrail-aiguardrailtopicpolicyconfig-properties"></a>

`TopicsConfig`  <a name="cfn-wisdom-aiguardrail-aiguardrailtopicpolicyconfig-topicsconfig"></a>
List of topic configs in topic policy.
*Required*: Yes
*Type*: Array of [GuardrailTopicConfig](aws-properties-wisdom-aiguardrail-guardrailtopicconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
