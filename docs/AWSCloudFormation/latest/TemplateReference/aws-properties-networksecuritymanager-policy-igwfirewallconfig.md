---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-policy-igwfirewallconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Policy IgwFirewallConfig

Settings for an AWS Network Firewall automated internet firewall policy: the internet connectivity treatment that the firewall applies to the subnets in scope, and any per-subnet overrides. Specify this property only for policies whose `FirewallType` is `IGW_FIREWALL`.

## Syntax
<a name="aws-properties-networksecuritymanager-policy-igwfirewallconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-policy-igwfirewallconfig-syntax.json"></a>

```json
{
  "[DefaultSubnetConnectivity](#cfn-networksecuritymanager-policy-igwfirewallconfig-defaultsubnetconnectivity)" : {{String}},
  "[SubnetConnectivityOverrides](#cfn-networksecuritymanager-policy-igwfirewallconfig-subnetconnectivityoverrides)" : {{[ SubnetConnectivityOverride, ... ]}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-policy-igwfirewallconfig-syntax.yaml"></a>

```yaml
  [DefaultSubnetConnectivity](#cfn-networksecuritymanager-policy-igwfirewallconfig-defaultsubnetconnectivity): {{String}}
  [SubnetConnectivityOverrides](#cfn-networksecuritymanager-policy-igwfirewallconfig-subnetconnectivityoverrides): {{
    - SubnetConnectivityOverride}}
```

## Properties
<a name="aws-properties-networksecuritymanager-policy-igwfirewallconfig-properties"></a>

`DefaultSubnetConnectivity`  <a name="cfn-networksecuritymanager-policy-igwfirewallconfig-defaultsubnetconnectivity"></a>
The internet connectivity treatment that applies to every subnet in scope, unless a subnet connectivity override applies to the subnet. Specify one of the following values:
 `flexible`
Sets the connectivity for each network interface in the subnet based on whether it is associated with a public IP address. A network interface with a public IP address gets bidirectional internet connectivity, and a network interface without one gets outbound-only connectivity. All traffic is inspected against your firewall rules.
 `bidirectional`
Provides bidirectional internet connectivity to every network interface that has a public IP association. A network interface without a public IP address can't communicate with the internet unless a NAT device is explicitly inserted in the path. All inbound and outbound traffic is inspected against your firewall rules.
 `outbound-only`
Provides egress-only connectivity for every network interface in the subnet. All outbound traffic and inbound responses are inspected against your firewall rules, and unsolicited inbound connections are dropped. For IPv4 traffic, the firewall performs NAT.
This property is required when `FirewallType` is `IGW_FIREWALL`. To exclude subnets from inspection, use a subnet connectivity override; `exclude` isn't a valid default.
*Required*: Conditional
*Type*: String
*Allowed values*: `flexible | bidirectional | outbound-only`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetConnectivityOverrides`  <a name="cfn-networksecuritymanager-policy-igwfirewallconfig-subnetconnectivityoverrides"></a>
An ordered list of overrides that apply a different connectivity treatment to the subnets that a scope selects. When a subnet matches more than one override, the first matching override in the list applies. You can specify at most one override for each connectivity type, so the list can contain up to four entries.
*Required*: No
*Type*: Array of [SubnetConnectivityOverride](aws-properties-networksecuritymanager-policy-subnetconnectivityoverride.md)
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
