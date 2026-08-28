---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-clientsideactionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ClientSideActionConfig
<a name="aws-properties-wafv2-webacl-clientsideactionconfig"></a>

This is part of the configuration for the managed rules `AWSManagedRulesAntiDDoSRuleSet` in `ManagedRuleGroupConfig`.

## Syntax
<a name="aws-properties-wafv2-webacl-clientsideactionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-clientsideactionconfig-syntax.json"></a>

```
{
  "[Challenge](#cfn-wafv2-webacl-clientsideactionconfig-challenge)" : {{ClientSideAction}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-clientsideactionconfig-syntax.yaml"></a>

```
  [Challenge](#cfn-wafv2-webacl-clientsideactionconfig-challenge): {{
    ClientSideAction}}
```

## Properties
<a name="aws-properties-wafv2-webacl-clientsideactionconfig-properties"></a>

`Challenge`  <a name="cfn-wafv2-webacl-clientsideactionconfig-challenge"></a>
Configuration for the use of the `AWSManagedRulesAntiDDoSRuleSet` rules `ChallengeAllDuringEvent` and `ChallengeDDoSRequests`.
This setting isn't related to the configuration of the `Challenge` action itself. It only configures the use of the two anti-DDoS rules named here.
You can enable or disable the use of these rules, and you can configure how to use them when they are enabled.
*Required*: Yes
*Type*: [ClientSideAction](aws-properties-wafv2-webacl-clientsideaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
