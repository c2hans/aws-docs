---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-ruleaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL RuleAction
<a name="aws-properties-wafv2-webacl-ruleaction"></a>

The action that AWS WAF should take on a web request when it matches a rule's statement. Settings at the web ACL level can override the rule action setting.

## Syntax
<a name="aws-properties-wafv2-webacl-ruleaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-ruleaction-syntax.json"></a>

```
{
  "[Allow](#cfn-wafv2-webacl-ruleaction-allow)" : {{AllowAction}},
  "[Block](#cfn-wafv2-webacl-ruleaction-block)" : {{BlockAction}},
  "[Captcha](#cfn-wafv2-webacl-ruleaction-captcha)" : {{CaptchaAction}},
  "[Challenge](#cfn-wafv2-webacl-ruleaction-challenge)" : {{ChallengeAction}},
  "[Count](#cfn-wafv2-webacl-ruleaction-count)" : {{CountAction}},
  "[Monetize](#cfn-wafv2-webacl-ruleaction-monetize)" : {{MonetizeAction}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-ruleaction-syntax.yaml"></a>

```
  [Allow](#cfn-wafv2-webacl-ruleaction-allow): {{
    AllowAction}}
  [Block](#cfn-wafv2-webacl-ruleaction-block): {{
    BlockAction}}
  [Captcha](#cfn-wafv2-webacl-ruleaction-captcha): {{
    CaptchaAction}}
  [Challenge](#cfn-wafv2-webacl-ruleaction-challenge): {{
    ChallengeAction}}
  [Count](#cfn-wafv2-webacl-ruleaction-count): {{
    CountAction}}
  [Monetize](#cfn-wafv2-webacl-ruleaction-monetize): {{
    MonetizeAction}}
```

## Properties
<a name="aws-properties-wafv2-webacl-ruleaction-properties"></a>

`Allow`  <a name="cfn-wafv2-webacl-ruleaction-allow"></a>
Instructs AWS WAF to allow the web request.
*Required*: No
*Type*: [AllowAction](aws-properties-wafv2-webacl-allowaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Block`  <a name="cfn-wafv2-webacl-ruleaction-block"></a>
Instructs AWS WAF to block the web request.
*Required*: No
*Type*: [BlockAction](aws-properties-wafv2-webacl-blockaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Captcha`  <a name="cfn-wafv2-webacl-ruleaction-captcha"></a>
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
*Type*: [CaptchaAction](aws-properties-wafv2-webacl-captchaaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Challenge`  <a name="cfn-wafv2-webacl-ruleaction-challenge"></a>
Instructs AWS WAF to run a `Challenge` check against the web request.
*Required*: No
*Type*: [ChallengeAction](aws-properties-wafv2-webacl-challengeaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Count`  <a name="cfn-wafv2-webacl-ruleaction-count"></a>
Instructs AWS WAF to count the web request and then continue evaluating the request using the remaining rules in the web ACL.
*Required*: No
*Type*: [CountAction](aws-properties-wafv2-webacl-countaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Monetize`  <a name="cfn-wafv2-webacl-ruleaction-monetize"></a>
Instructs AWS WAF to return an HTTP 402 Payment Required response with a price manifest. The requesting client can complete payment and resubmit the request to gain access. This is a terminating action-requests that do not complete payment are blocked. This action is available only for web ACLs associated with Amazon CloudFront distributions and requires a `MonetizationConfig` on the web ACL.
*Required*: No
*Type*: [MonetizeAction](aws-properties-wafv2-webacl-monetizeaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
