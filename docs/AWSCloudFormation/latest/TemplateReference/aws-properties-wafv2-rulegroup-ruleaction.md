---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-ruleaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup RuleAction
<a name="aws-properties-wafv2-rulegroup-ruleaction"></a>

The action that AWS WAF should take on a web request when it matches a rule's statement. Settings at the web ACL level can override the rule action setting.

## Syntax
<a name="aws-properties-wafv2-rulegroup-ruleaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-ruleaction-syntax.json"></a>

```
{
  "[Allow](#cfn-wafv2-rulegroup-ruleaction-allow)" : {{AllowAction}},
  "[Block](#cfn-wafv2-rulegroup-ruleaction-block)" : {{BlockAction}},
  "[Captcha](#cfn-wafv2-rulegroup-ruleaction-captcha)" : {{CaptchaAction}},
  "[Challenge](#cfn-wafv2-rulegroup-ruleaction-challenge)" : {{ChallengeAction}},
  "[Count](#cfn-wafv2-rulegroup-ruleaction-count)" : {{CountAction}},
  "[Monetize](#cfn-wafv2-rulegroup-ruleaction-monetize)" : {{MonetizeAction}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-ruleaction-syntax.yaml"></a>

```
  [Allow](#cfn-wafv2-rulegroup-ruleaction-allow): {{
    AllowAction}}
  [Block](#cfn-wafv2-rulegroup-ruleaction-block): {{
    BlockAction}}
  [Captcha](#cfn-wafv2-rulegroup-ruleaction-captcha): {{
    CaptchaAction}}
  [Challenge](#cfn-wafv2-rulegroup-ruleaction-challenge): {{
    ChallengeAction}}
  [Count](#cfn-wafv2-rulegroup-ruleaction-count): {{
    CountAction}}
  [Monetize](#cfn-wafv2-rulegroup-ruleaction-monetize): {{
    MonetizeAction}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-ruleaction-properties"></a>

`Allow`  <a name="cfn-wafv2-rulegroup-ruleaction-allow"></a>
Instructs AWS WAF to allow the web request.
*Required*: No
*Type*: [AllowAction](aws-properties-wafv2-rulegroup-allowaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Block`  <a name="cfn-wafv2-rulegroup-ruleaction-block"></a>
Instructs AWS WAF to block the web request.
*Required*: No
*Type*: [BlockAction](aws-properties-wafv2-rulegroup-blockaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Captcha`  <a name="cfn-wafv2-rulegroup-ruleaction-captcha"></a>
Specifies that AWS WAF should run a `CAPTCHA` check against the request:
+ If the request includes a valid, unexpired `CAPTCHA` token, AWS WAF allows the web request inspection to proceed to the next rule, similar to a `CountAction`.
+ If the request doesn't include a valid, unexpired `CAPTCHA` token, AWS WAF discontinues the web ACL evaluation of the request and blocks it from going to its intended destination.

  AWS WAF generates a response that it sends back to the client, which includes the following:
  + The header `x-amzn-waf-action` with a value of `captcha`.
  + The HTTP status code `405 Method Not Allowed`.
  + If the request contains an `Accept` header with a value of `text/html`, the response includes a `CAPTCHA` challenge.
You can configure the expiration time in the `CaptchaConfig``ImmunityTimeProperty` setting at the rule and web ACL level. The rule setting overrides the web ACL setting.
This action option is available for rules. It isn't available for web ACL default actions.
*Required*: No
*Type*: [CaptchaAction](aws-properties-wafv2-rulegroup-captchaaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Challenge`  <a name="cfn-wafv2-rulegroup-ruleaction-challenge"></a>
Instructs AWS WAF to run a `Challenge` check against the web request.
*Required*: No
*Type*: [ChallengeAction](aws-properties-wafv2-rulegroup-challengeaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Count`  <a name="cfn-wafv2-rulegroup-ruleaction-count"></a>
Instructs AWS WAF to count the web request and then continue evaluating the request using the remaining rules in the web ACL.
*Required*: No
*Type*: [CountAction](aws-properties-wafv2-rulegroup-countaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Monetize`  <a name="cfn-wafv2-rulegroup-ruleaction-monetize"></a>
Instructs AWS WAF to return an HTTP 402 Payment Required response with a price manifest. The requesting client can complete payment and resubmit the request to gain access. This is a terminating action-requests that do not complete payment are blocked. This action is available only for web ACLs associated with Amazon CloudFront distributions and requires a `MonetizationConfig` on the web ACL.
*Required*: No
*Type*: [MonetizeAction](aws-properties-wafv2-rulegroup-monetizeaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-wafv2-rulegroup-ruleaction--examples"></a>

**Topics**
+ [Set an allow action](#aws-properties-wafv2-rulegroup-ruleaction--examples--Set_an_allow_action)
+ [Set an allow action with a custom request setting](#aws-properties-wafv2-rulegroup-ruleaction--examples--Set_an_allow_action_with_a_custom_request_setting)

### Set an allow action
<a name="aws-properties-wafv2-rulegroup-ruleaction--examples--Set_an_allow_action"></a>

The following shows an example allow action specification.

#### YAML
<a name="aws-properties-wafv2-rulegroup-ruleaction--examples--Set_an_allow_action--yaml"></a>

```
Action:
  Allow: {}
```

#### JSON
<a name="aws-properties-wafv2-rulegroup-ruleaction--examples--Set_an_allow_action--json"></a>

```
"Action": {
  "Allow": {}
}
```

### Set an allow action with a custom request setting
<a name="aws-properties-wafv2-rulegroup-ruleaction--examples--Set_an_allow_action_with_a_custom_request_setting"></a>

The following shows an example allow action specification with custom request handling.

#### YAML
<a name="aws-properties-wafv2-rulegroup-ruleaction--examples--Set_an_allow_action_with_a_custom_request_setting--yaml"></a>

```
Action:
  Allow:
    CustomRequestHandling:
      InsertHeaders:
        - Name: AllowActionHeader1Name
          Value: AllowActionHeader1Value
        - Name: AllowActionHeader2Name
          Value: AllowActionHeader2Value
```

#### JSON
<a name="aws-properties-wafv2-rulegroup-ruleaction--examples--Set_an_allow_action_with_a_custom_request_setting--json"></a>

```
"Action": {
  "Allow": {
    "CustomRequestHandling": {
      "InsertHeaders": [
        {
          "Name": "AllowActionHeader1Name",
          "Value": "AllowActionHeader1Value"
        },
        {
          "Name": "AllowActionHeader2Name",
          "Value": "AllowActionHeader2Value"
        }
      ]
    }
  }
}
```
