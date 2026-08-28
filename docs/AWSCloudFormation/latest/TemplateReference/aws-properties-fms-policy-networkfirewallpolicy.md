---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fms-policy-networkfirewallpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::Policy NetworkFirewallPolicy
<a name="aws-properties-fms-policy-networkfirewallpolicy"></a>

Configures the firewall policy deployment model of AWS Network Firewall. For information about Network Firewall deployment models, see [AWS Network Firewall example architectures with routing](https://docs.aws.amazon.com/network-firewall/latest/developerguide/architectures.html) in the *Network Firewall Developer Guide*.

## Syntax
<a name="aws-properties-fms-policy-networkfirewallpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fms-policy-networkfirewallpolicy-syntax.json"></a>

```
{
  "[FirewallDeploymentModel](#cfn-fms-policy-networkfirewallpolicy-firewalldeploymentmodel)" : {{String}}
}
```

### YAML
<a name="aws-properties-fms-policy-networkfirewallpolicy-syntax.yaml"></a>

```
  [FirewallDeploymentModel](#cfn-fms-policy-networkfirewallpolicy-firewalldeploymentmodel): {{String}}
```

## Properties
<a name="aws-properties-fms-policy-networkfirewallpolicy-properties"></a>

`FirewallDeploymentModel`  <a name="cfn-fms-policy-networkfirewallpolicy-firewalldeploymentmodel"></a>
Defines the deployment model to use for the firewall policy. To use a distributed model, set [FirewallDeploymentModel](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html) to `DISTRIBUTED`.
*Required*: Yes
*Type*: String
*Allowed values*: `DISTRIBUTED | CENTRALIZED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
