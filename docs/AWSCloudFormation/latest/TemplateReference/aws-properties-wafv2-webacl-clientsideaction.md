---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-clientsideaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ClientSideAction
<a name="aws-properties-wafv2-webacl-clientsideaction"></a>

This is part of the `AWSManagedRulesAntiDDoSRuleSet``ClientSideActionConfig` configuration in `ManagedRuleGroupConfig`.

## Syntax
<a name="aws-properties-wafv2-webacl-clientsideaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-clientsideaction-syntax.json"></a>

```
{
  "[ExemptUriRegularExpressions](#cfn-wafv2-webacl-clientsideaction-exempturiregularexpressions)" : {{[ Regex, ... ]}},
  "[Sensitivity](#cfn-wafv2-webacl-clientsideaction-sensitivity)" : {{String}},
  "[UsageOfAction](#cfn-wafv2-webacl-clientsideaction-usageofaction)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-clientsideaction-syntax.yaml"></a>

```
  [ExemptUriRegularExpressions](#cfn-wafv2-webacl-clientsideaction-exempturiregularexpressions): {{
    - Regex}}
  [Sensitivity](#cfn-wafv2-webacl-clientsideaction-sensitivity): {{String}}
  [UsageOfAction](#cfn-wafv2-webacl-clientsideaction-usageofaction): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-clientsideaction-properties"></a>

`ExemptUriRegularExpressions`  <a name="cfn-wafv2-webacl-clientsideaction-exempturiregularexpressions"></a>
The regular expression to match against the web request URI, used to identify requests that can't handle a silent browser challenge. When the `ClientSideAction` setting `UsageOfAction` is enabled, the managed rule group uses this setting to determine which requests to label with `awswaf:managed:aws:anti-ddos:challengeable-request`. If `UsageOfAction` is disabled, this setting has no effect and the managed rule group doesn't add the label to any requests.
The anti-DDoS managed rule group doesn't evaluate the rules `ChallengeDDoSRequests` or `ChallengeAllDuringEvent` for web requests whose URIs match this regex. This is true regardless of whether you override the rule action for either of the rules in your web ACL configuration.
AWS recommends using a regular expression.
This setting is required if `UsageOfAction` is set to `ENABLED`. If required, you can provide between 1 and 5 regex objects in the array of settings.
AWS recommends starting with the following setting. Review and update it for your application's needs:
 `\/api\/|\.(acc|avi|css|gif|jpe?g|js|mp[34]|ogg|otf|pdf|png|tiff?|ttf|webm|webp|woff2?)$`
*Required*: No
*Type*: Array of [Regex](aws-properties-wafv2-webacl-regex.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sensitivity`  <a name="cfn-wafv2-webacl-clientsideaction-sensitivity"></a>
The sensitivity that the rule group rule `ChallengeDDoSRequests` uses when matching against the DDoS suspicion labeling on a request. The managed rule group adds the labeling during DDoS events, before the `ChallengeDDoSRequests` rule runs.
The higher the sensitivity, the more levels of labeling that the rule matches:
+ Low sensitivity is less sensitive, causing the rule to match only on the most likely participants in an attack, which are the requests with the high suspicion label `awswaf:managed:aws:anti-ddos:high-suspicion-ddos-request`.
+ Medium sensitivity causes the rule to match on the medium and high suspicion labels.
+ High sensitivity causes the rule to match on all of the suspicion labels: low, medium, and high.
Default: `HIGH`
*Required*: No
*Type*: String
*Allowed values*: `LOW | MEDIUM | HIGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsageOfAction`  <a name="cfn-wafv2-webacl-clientsideaction-usageofaction"></a>
Determines whether to use the `AWSManagedRulesAntiDDoSRuleSet` rules `ChallengeAllDuringEvent` and `ChallengeDDoSRequests` in the rule group evaluation and the related label `awswaf:managed:aws:anti-ddos:challengeable-request`.
+ If usage is enabled:
  + The managed rule group adds the label `awswaf:managed:aws:anti-ddos:challengeable-request` to any web request whose URL does *NOT* match the regular expressions provided in the `ClientSideAction` setting `ExemptUriRegularExpressions`.
  + The two rules are evaluated against web requests for protected resources that are experiencing a DDoS attack. The two rules only apply their action to matching requests that have the label `awswaf:managed:aws:anti-ddos:challengeable-request`.
+ If usage is disabled:
  + The managed rule group doesn't add the label `awswaf:managed:aws:anti-ddos:challengeable-request` to any web requests.
  + The two rules are not evaluated.
  + None of the other `ClientSideAction` settings have any effect.
This setting only enables or disables the use of the two anti-DDOS rules `ChallengeAllDuringEvent` and `ChallengeDDoSRequests` in the anti-DDoS managed rule group.
This setting doesn't alter the action setting in the two rules. To override the actions used by the rules `ChallengeAllDuringEvent` and `ChallengeDDoSRequests`, enable this setting, and then override the rule actions in the usual way, in your managed rule group configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
