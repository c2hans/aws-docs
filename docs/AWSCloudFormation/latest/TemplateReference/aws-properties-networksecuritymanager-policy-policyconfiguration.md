---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-policy-policyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Policy PolicyConfiguration
<a name="aws-properties-networksecuritymanager-policy-policyconfiguration"></a>

The configuration settings that control the policy's behavior, including remediation and settings specific to the firewall type.

## Syntax
<a name="aws-properties-networksecuritymanager-policy-policyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-policy-policyconfiguration-syntax.json"></a>

```
{
  "[RemediationEnabled](#cfn-networksecuritymanager-policy-policyconfiguration-remediationenabled)" : {{Boolean}},
  "[ResourcesCleanUp](#cfn-networksecuritymanager-policy-policyconfiguration-resourcescleanup)" : {{Boolean}},
  "[WafConfig](#cfn-networksecuritymanager-policy-policyconfiguration-wafconfig)" : {{WafConfig}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-policy-policyconfiguration-syntax.yaml"></a>

```
  [RemediationEnabled](#cfn-networksecuritymanager-policy-policyconfiguration-remediationenabled): {{Boolean}}
  [ResourcesCleanUp](#cfn-networksecuritymanager-policy-policyconfiguration-resourcescleanup): {{Boolean}}
  [WafConfig](#cfn-networksecuritymanager-policy-policyconfiguration-wafconfig): {{
    WafConfig}}
```

## Properties
<a name="aws-properties-networksecuritymanager-policy-policyconfiguration-properties"></a>

`RemediationEnabled`  <a name="cfn-networksecuritymanager-policy-policyconfiguration-remediationenabled"></a>
Specifies whether AWS Network Security Manager automatically remediates noncompliant resources. Default: `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesCleanUp`  <a name="cfn-networksecuritymanager-policy-policyconfiguration-resourcescleanup"></a>
Specifies whether AWS Network Security Manager automatically removes the resources it created when they are no longer needed. Default: `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WafConfig`  <a name="cfn-networksecuritymanager-policy-policyconfiguration-wafconfig"></a>
AWS WAF-specific policy settings.
This property is required when `FirewallType` is `WAF`. Don't specify it when `FirewallType` is `SHIELD_ADVANCED`; Network Security Manager rejects a Shield Advanced policy that includes it.
*Required*: Conditional
*Type*: [WafConfig](aws-properties-networksecuritymanager-policy-wafconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
