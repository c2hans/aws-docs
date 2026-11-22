---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-policy-policyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Policy PolicyConfiguration

The configuration settings that control the policy's behavior, including remediation and settings specific to the firewall type.

## Syntax
<a name="aws-properties-networksecuritymanager-policy-policyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-policy-policyconfiguration-syntax.json"></a>

```json
{
  "[IgwFirewallConfig](#cfn-networksecuritymanager-policy-policyconfiguration-igwfirewallconfig)" : {{IgwFirewallConfig}},
  "[RemediationEnabled](#cfn-networksecuritymanager-policy-policyconfiguration-remediationenabled)" : {{Boolean}},
  "[ResourcesCleanUp](#cfn-networksecuritymanager-policy-policyconfiguration-resourcescleanup)" : {{Boolean}},
  "[WafConfig](#cfn-networksecuritymanager-policy-policyconfiguration-wafconfig)" : {{WafConfig}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-policy-policyconfiguration-syntax.yaml"></a>

```yaml
  [IgwFirewallConfig](#cfn-networksecuritymanager-policy-policyconfiguration-igwfirewallconfig): {{
    IgwFirewallConfig}}
  [RemediationEnabled](#cfn-networksecuritymanager-policy-policyconfiguration-remediationenabled): {{Boolean}}
  [ResourcesCleanUp](#cfn-networksecuritymanager-policy-policyconfiguration-resourcescleanup): {{Boolean}}
  [WafConfig](#cfn-networksecuritymanager-policy-policyconfiguration-wafconfig): {{
    WafConfig}}
```

## Properties
<a name="aws-properties-networksecuritymanager-policy-policyconfiguration-properties"></a>

`IgwFirewallConfig`  <a name="cfn-networksecuritymanager-policy-policyconfiguration-igwfirewallconfig"></a>
Settings specific to AWS Network Firewall automated internet firewall policies.
This property is required when `FirewallType` is `IGW_FIREWALL`. Don't specify it for any other firewall type.
*Required*: Conditional
*Type*: [IgwFirewallConfig](aws-properties-networksecuritymanager-policy-igwfirewallconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemediationEnabled`  <a name="cfn-networksecuritymanager-policy-policyconfiguration-remediationenabled"></a>
Specifies whether AWS Network Security Manager automatically remediates noncompliant resources. Default: `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesCleanUp`  <a name="cfn-networksecuritymanager-policy-policyconfiguration-resourcescleanup"></a>
Specifies whether AWS Network Security Manager automatically removes the resources it created when they are no longer needed. This member is required, and the only supported value is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WafConfig`  <a name="cfn-networksecuritymanager-policy-policyconfiguration-wafconfig"></a>
AWS WAF-specific policy settings.
This property is required when `FirewallType` is `WAF`. Don't specify it for any other firewall type; Network Security Manager rejects a `SHIELD_ADVANCED` or `IGW_FIREWALL` policy that includes it.
*Required*: Conditional
*Type*: [WafConfig](aws-properties-networksecuritymanager-policy-wafconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
