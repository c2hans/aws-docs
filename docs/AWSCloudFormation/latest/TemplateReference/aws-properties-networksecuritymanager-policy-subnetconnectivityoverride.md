---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-policy-subnetconnectivityoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Policy SubnetConnectivityOverride

Applies a connectivity treatment to the subnets that a scope selects, instead of the policy's `DefaultSubnetConnectivity`.

## Syntax
<a name="aws-properties-networksecuritymanager-policy-subnetconnectivityoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-policy-subnetconnectivityoverride-syntax.json"></a>

```json
{
  "[ConnectivityType](#cfn-networksecuritymanager-policy-subnetconnectivityoverride-connectivitytype)" : {{String}},
  "[Scopes](#cfn-networksecuritymanager-policy-subnetconnectivityoverride-scopes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-policy-subnetconnectivityoverride-syntax.yaml"></a>

```yaml
  [ConnectivityType](#cfn-networksecuritymanager-policy-subnetconnectivityoverride-connectivitytype): {{String}}
  [Scopes](#cfn-networksecuritymanager-policy-subnetconnectivityoverride-scopes): {{
    - String}}
```

## Properties
<a name="aws-properties-networksecuritymanager-policy-subnetconnectivityoverride-properties"></a>

`ConnectivityType`  <a name="cfn-networksecuritymanager-policy-subnetconnectivityoverride-connectivitytype"></a>
The connectivity treatment to apply to the subnets that the override's scope selects. The rest of the subnets in scope keep the policy's default connectivity. Specify one of the following values:
 `flexible`
Sets the connectivity for each network interface in the subnet based on whether it is associated with a public IP address. A network interface with a public IP address gets bidirectional internet connectivity, and a network interface without one gets outbound-only connectivity. All traffic is inspected against your firewall rules.
 `bidirectional`
Provides bidirectional internet connectivity to every network interface that has a public IP association. A network interface without a public IP address can't communicate with the internet unless a NAT device is explicitly inserted in the path. All inbound and outbound traffic is inspected against your firewall rules.
 `outbound-only`
Provides egress-only connectivity for every network interface in the subnet. All outbound traffic and inbound responses are inspected against your firewall rules, and unsolicited inbound connections are dropped. For IPv4 traffic, the firewall performs NAT.
 `exclude`
The firewall doesn't inspect traffic for the selected subnets. Their traffic bypasses the firewall and passes directly through the internet gateway. You can specify this value only in an override.
*Required*: Yes
*Type*: String
*Allowed values*: `flexible | bidirectional | outbound-only | exclude`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scopes`  <a name="cfn-networksecuritymanager-policy-subnetconnectivityoverride-scopes"></a>
A list that contains the Amazon Resource Name (ARN) of the scope that selects the subnets to override. The list must contain exactly one scope ARN, and the scope must belong to your account and have a `SpecializedScopeType` of `IGW_FIREWALL_SUBNET_CONNECTIVITY_OVERRIDE`. The deployment determines which accounts are in scope, and the referenced scope selects subnets within those accounts.
To get this value from a scope defined in the same template, use `Fn::GetAtt` with the [AWS::NetworkSecurityManager::Scope](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-scope.html) resource.
*Required*: Yes
*Type*: Array of String
*Minimum*: `20`
*Maximum*: `1010 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
