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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
