---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fms-policy-policyoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::Policy PolicyOption
<a name="aws-properties-fms-policy-policyoption"></a>

Contains the settings to configure a network ACL policy, a AWS Network Firewall firewall policy deployment model, or a third-party firewall policy.

## Syntax
<a name="aws-properties-fms-policy-policyoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fms-policy-policyoption-syntax.json"></a>

```
{
  "[NetworkAclCommonPolicy](#cfn-fms-policy-policyoption-networkaclcommonpolicy)" : {{NetworkAclCommonPolicy}},
  "[NetworkFirewallPolicy](#cfn-fms-policy-policyoption-networkfirewallpolicy)" : {{NetworkFirewallPolicy}},
  "[ThirdPartyFirewallPolicy](#cfn-fms-policy-policyoption-thirdpartyfirewallpolicy)" : {{ThirdPartyFirewallPolicy}}
}
```

### YAML
<a name="aws-properties-fms-policy-policyoption-syntax.yaml"></a>

```
  [NetworkAclCommonPolicy](#cfn-fms-policy-policyoption-networkaclcommonpolicy): {{
    NetworkAclCommonPolicy}}
  [NetworkFirewallPolicy](#cfn-fms-policy-policyoption-networkfirewallpolicy): {{
    NetworkFirewallPolicy}}
  [ThirdPartyFirewallPolicy](#cfn-fms-policy-policyoption-thirdpartyfirewallpolicy): {{
    ThirdPartyFirewallPolicy}}
```

## Properties
<a name="aws-properties-fms-policy-policyoption-properties"></a>

`NetworkAclCommonPolicy`  <a name="cfn-fms-policy-policyoption-networkaclcommonpolicy"></a>
Defines a Firewall Manager network ACL policy.
*Required*: No
*Type*: [NetworkAclCommonPolicy](aws-properties-fms-policy-networkaclcommonpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkFirewallPolicy`  <a name="cfn-fms-policy-policyoption-networkfirewallpolicy"></a>
Defines the deployment model to use for the firewall policy.
*Required*: No
*Type*: [NetworkFirewallPolicy](aws-properties-fms-policy-networkfirewallpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThirdPartyFirewallPolicy`  <a name="cfn-fms-policy-policyoption-thirdpartyfirewallpolicy"></a>
Defines the policy options for a third-party firewall policy.
*Required*: No
*Type*: [ThirdPartyFirewallPolicy](aws-properties-fms-policy-thirdpartyfirewallpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
