---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-challengeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ChallengeConfig
<a name="aws-properties-wafv2-webacl-challengeconfig"></a>

Specifies how AWS WAF should handle `Challenge` evaluations. This is available at the web ACL level and in each rule.

## Syntax
<a name="aws-properties-wafv2-webacl-challengeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-challengeconfig-syntax.json"></a>

```
{
  "[ImmunityTimeProperty](#cfn-wafv2-webacl-challengeconfig-immunitytimeproperty)" : {{ImmunityTimeProperty}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-challengeconfig-syntax.yaml"></a>

```
  [ImmunityTimeProperty](#cfn-wafv2-webacl-challengeconfig-immunitytimeproperty): {{
    ImmunityTimeProperty}}
```

## Properties
<a name="aws-properties-wafv2-webacl-challengeconfig-properties"></a>

`ImmunityTimeProperty`  <a name="cfn-wafv2-webacl-challengeconfig-immunitytimeproperty"></a>
Determines how long a challenge timestamp in the token remains valid after the client successfully responds to a challenge.
*Required*: No
*Type*: [ImmunityTimeProperty](aws-properties-wafv2-webacl-immunitytimeproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
