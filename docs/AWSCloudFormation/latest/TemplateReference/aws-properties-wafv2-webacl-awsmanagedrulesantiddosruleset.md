---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-awsmanagedrulesantiddosruleset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL AWSManagedRulesAntiDDoSRuleSet
<a name="aws-properties-wafv2-webacl-awsmanagedrulesantiddosruleset"></a>

Configures the use of the anti-DDoS managed rule group, `AWSManagedRulesAntiDDoSRuleSet`. This configuration is used in `ManagedRuleGroupConfig`.

The configuration that you provide here determines whether and how the rules in the rule group are used.

For additional information about this and the other intelligent threat mitigation rule groups, see [Intelligent threat mitigation in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections) and [AWS Managed Rules rule groups list](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list) in the *AWS WAF Developer Guide*.

## Syntax
<a name="aws-properties-wafv2-webacl-awsmanagedrulesantiddosruleset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-awsmanagedrulesantiddosruleset-syntax.json"></a>

```
{
  "[ClientSideActionConfig](#cfn-wafv2-webacl-awsmanagedrulesantiddosruleset-clientsideactionconfig)" : {{ClientSideActionConfig}},
  "[SensitivityToBlock](#cfn-wafv2-webacl-awsmanagedrulesantiddosruleset-sensitivitytoblock)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-awsmanagedrulesantiddosruleset-syntax.yaml"></a>

```
  [ClientSideActionConfig](#cfn-wafv2-webacl-awsmanagedrulesantiddosruleset-clientsideactionconfig): {{
    ClientSideActionConfig}}
  [SensitivityToBlock](#cfn-wafv2-webacl-awsmanagedrulesantiddosruleset-sensitivitytoblock): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-awsmanagedrulesantiddosruleset-properties"></a>

`ClientSideActionConfig`  <a name="cfn-wafv2-webacl-awsmanagedrulesantiddosruleset-clientsideactionconfig"></a>
Configures the request handling that's applied by the managed rule group rules `ChallengeAllDuringEvent` and `ChallengeDDoSRequests` during a distributed denial of service (DDoS) attack.
*Required*: Yes
*Type*: [ClientSideActionConfig](aws-properties-wafv2-webacl-clientsideactionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SensitivityToBlock`  <a name="cfn-wafv2-webacl-awsmanagedrulesantiddosruleset-sensitivitytoblock"></a>
The sensitivity that the rule group rule `DDoSRequests` uses when matching against the DDoS suspicion labeling on a request. The managed rule group adds the labeling during DDoS events, before the `DDoSRequests` rule runs.
The higher the sensitivity, the more levels of labeling that the rule matches:
+ Low sensitivity is less sensitive, causing the rule to match only on the most likely participants in an attack, which are the requests with the high suspicion label `awswaf:managed:aws:anti-ddos:high-suspicion-ddos-request`.
+ Medium sensitivity causes the rule to match on the medium and high suspicion labels.
+ High sensitivity causes the rule to match on all of the suspicion labels: low, medium, and high.
Default: `LOW`
*Required*: No
*Type*: String
*Allowed values*: `LOW | MEDIUM | HIGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
