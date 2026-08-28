---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-challengeaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ChallengeAction
<a name="aws-properties-wafv2-webacl-challengeaction"></a>

Specifies that AWS WAF should run a `Challenge` check against the request to verify that the request is coming from a legitimate client session:
+ If the request includes a valid, unexpired challenge token, AWS WAF applies any custom request handling and labels that you've configured and then allows the web request inspection to proceed to the next rule, similar to a `CountAction`.
+ If the request doesn't include a valid, unexpired challenge token, AWS WAF discontinues the web ACL evaluation of the request and blocks it from going to its intended destination.

  AWS WAF then generates a challenge response that it sends back to the client, which includes the following:
  + The header `x-amzn-waf-action` with a value of `challenge`.
  + The HTTP status code `202 Request Accepted`.
  + If the request contains an `Accept` header with a value of `text/html`, the response includes a JavaScript page interstitial with a challenge script.

  Challenges run silent browser interrogations in the background, and don't generally affect the end user experience.

  A challenge enforces token acquisition using an interstitial JavaScript challenge that inspects the client session for legitimate behavior. The challenge blocks bots or at least increases the cost of operating sophisticated bots.

  After the client session successfully responds to the challenge, it receives a new token from AWS WAF, which the challenge script uses to resubmit the original request.

You can configure the expiration time in the `ChallengeConfig``ImmunityTimeProperty` setting at the rule and web ACL level. The rule setting overrides the web ACL setting.

This action option is available for rules. It isn't available for web ACL default actions.

## Syntax
<a name="aws-properties-wafv2-webacl-challengeaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-challengeaction-syntax.json"></a>

```
{
  "[CustomRequestHandling](#cfn-wafv2-webacl-challengeaction-customrequesthandling)" : {{CustomRequestHandling}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-challengeaction-syntax.yaml"></a>

```
  [CustomRequestHandling](#cfn-wafv2-webacl-challengeaction-customrequesthandling): {{
    CustomRequestHandling}}
```

## Properties
<a name="aws-properties-wafv2-webacl-challengeaction-properties"></a>

`CustomRequestHandling`  <a name="cfn-wafv2-webacl-challengeaction-customrequesthandling"></a>
Defines custom handling for the web request, used when the challenge inspection determines that the request's token is valid and unexpired.
For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the [AWS WAF developer guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html).
*Required*: No
*Type*: [CustomRequestHandling](aws-properties-wafv2-webacl-customrequesthandling.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
