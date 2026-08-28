---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-shield-protection-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Shield::Protection Action
<a name="aws-properties-shield-protection-action"></a>

Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.

## Syntax
<a name="aws-properties-shield-protection-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-shield-protection-action-syntax.json"></a>

```
{
  "[Block](#cfn-shield-protection-action-block)" : {{Json}},
  "[Count](#cfn-shield-protection-action-count)" : {{Json}}
}
```

### YAML
<a name="aws-properties-shield-protection-action-syntax.yaml"></a>

```
  [Block](#cfn-shield-protection-action-block): {{Json}}
  [Count](#cfn-shield-protection-action-count): {{Json}}
```

## Properties
<a name="aws-properties-shield-protection-action-properties"></a>

`Block`  <a name="cfn-shield-protection-action-block"></a>
Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF`Block` action.
You must specify exactly one action, either `Block` or `Count`.
Example JSON: `{ "Block": {} }`
Example YAML: `Block: {}`
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Count`  <a name="cfn-shield-protection-action-count"></a>
Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF`Count` action.
You must specify exactly one action, either `Block` or `Count`.
Example JSON: `{ "Count": {} }`
Example YAML: `Count: {}`
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
