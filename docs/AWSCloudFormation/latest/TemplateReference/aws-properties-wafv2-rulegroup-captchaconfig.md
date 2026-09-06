---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-captchaconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup CaptchaConfig
<a name="aws-properties-wafv2-rulegroup-captchaconfig"></a>

Specifies how AWS WAF should handle `CAPTCHA` evaluations. This is available at the web ACL level and in each rule.

## Syntax
<a name="aws-properties-wafv2-rulegroup-captchaconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-captchaconfig-syntax.json"></a>

```
{
  "[ImmunityTimeProperty](#cfn-wafv2-rulegroup-captchaconfig-immunitytimeproperty)" : {{ImmunityTimeProperty}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-captchaconfig-syntax.yaml"></a>

```
  [ImmunityTimeProperty](#cfn-wafv2-rulegroup-captchaconfig-immunitytimeproperty): {{
    ImmunityTimeProperty}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-captchaconfig-properties"></a>

`ImmunityTimeProperty`  <a name="cfn-wafv2-rulegroup-captchaconfig-immunitytimeproperty"></a>
Determines how long a `CAPTCHA` timestamp in the token remains valid after the client successfully solves a `CAPTCHA` puzzle.
*Required*: No
*Type*: [ImmunityTimeProperty](aws-properties-wafv2-rulegroup-immunitytimeproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
