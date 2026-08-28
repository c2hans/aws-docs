---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiguardrail-guardrailtopicconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIGuardrail GuardrailTopicConfig
<a name="aws-properties-wisdom-aiguardrail-guardrailtopicconfig"></a>

Topic configuration in topic policy.

## Syntax
<a name="aws-properties-wisdom-aiguardrail-guardrailtopicconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiguardrail-guardrailtopicconfig-syntax.json"></a>

```
{
  "[Definition](#cfn-wisdom-aiguardrail-guardrailtopicconfig-definition)" : {{String}},
  "[Examples](#cfn-wisdom-aiguardrail-guardrailtopicconfig-examples)" : {{[ String, ... ]}},
  "[Name](#cfn-wisdom-aiguardrail-guardrailtopicconfig-name)" : {{String}},
  "[Type](#cfn-wisdom-aiguardrail-guardrailtopicconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiguardrail-guardrailtopicconfig-syntax.yaml"></a>

```
  [Definition](#cfn-wisdom-aiguardrail-guardrailtopicconfig-definition): {{String}}
  [Examples](#cfn-wisdom-aiguardrail-guardrailtopicconfig-examples): {{
    - String}}
  [Name](#cfn-wisdom-aiguardrail-guardrailtopicconfig-name): {{String}}
  [Type](#cfn-wisdom-aiguardrail-guardrailtopicconfig-type): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiguardrail-guardrailtopicconfig-properties"></a>

`Definition`  <a name="cfn-wisdom-aiguardrail-guardrailtopicconfig-definition"></a>
Definition of topic in topic policy.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Examples`  <a name="cfn-wisdom-aiguardrail-guardrailtopicconfig-examples"></a>
Text example in topic policy.
*Required*: No
*Type*: Array of String
*Maximum*: `100`
*Minimum*: `1 | 0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wisdom-aiguardrail-guardrailtopicconfig-name"></a>
Name of topic in topic policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z-_ !?.]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-wisdom-aiguardrail-guardrailtopicconfig-type"></a>
Type of topic in a policy.
*Required*: Yes
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
