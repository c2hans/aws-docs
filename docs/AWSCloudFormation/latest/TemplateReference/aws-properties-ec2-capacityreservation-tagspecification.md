---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-capacityreservation-tagspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::CapacityReservation TagSpecification
<a name="aws-properties-ec2-capacityreservation-tagspecification"></a>

An array of key-value pairs to apply to this resource.

For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-ec2-capacityreservation-tagspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-capacityreservation-tagspecification-syntax.json"></a>

```
{
  "[ResourceType](#cfn-ec2-capacityreservation-tagspecification-resourcetype)" : {{String}},
  "[Tags](#cfn-ec2-capacityreservation-tagspecification-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-capacityreservation-tagspecification-syntax.yaml"></a>

```
  [ResourceType](#cfn-ec2-capacityreservation-tagspecification-resourcetype): {{String}}
  [Tags](#cfn-ec2-capacityreservation-tagspecification-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-ec2-capacityreservation-tagspecification-properties"></a>

`ResourceType`  <a name="cfn-ec2-capacityreservation-tagspecification-resourcetype"></a>
The type of resource to tag. Specify `capacity-reservation`.
*Required*: No
*Type*: String
*Allowed values*: `capacity-reservation | client-vpn-endpoint | customer-gateway | carrier-gateway | coip-pool | declarative-policies-report | dedicated-host | dhcp-options | egress-only-internet-gateway | elastic-ip | elastic-gpu | export-image-task | export-instance-task | fleet | fpga-image | host-reservation | image | image-usage-report | import-image-task | import-snapshot-task | instance | instance-event-window | internet-gateway | ipam | ipam-pool | ipam-scope | ipv4pool-ec2 | ipv6pool-ec2 | key-pair | launch-template | local-gateway | local-gateway-route-table | local-gateway-virtual-interface | local-gateway-virtual-interface-group | local-gateway-route-table-vpc-association | local-gateway-route-table-virtual-interface-group-association | natgateway | network-acl | network-interface | network-insights-analysis | network-insights-path | network-insights-access-scope | network-insights-access-scope-analysis | outpost-lag | placement-group | prefix-list | replace-root-volume-task | reserved-instances | route-table | security-group | security-group-rule | service-link-virtual-interface | snapshot | spot-fleet-request | spot-instances-request | subnet | subnet-cidr-reservation | traffic-mirror-filter | traffic-mirror-session | traffic-mirror-target | transit-gateway | transit-gateway-attachment | transit-gateway-connect-peer | transit-gateway-multicast-domain | transit-gateway-policy-table | transit-gateway-metering-policy | transit-gateway-route-table | transit-gateway-route-table-announcement | volume | vpc | vpc-endpoint | vpc-endpoint-connection | vpc-endpoint-service | vpc-endpoint-service-permission | vpc-peering-connection | vpn-connection | vpn-gateway | vpc-flow-log | capacity-reservation-fleet | traffic-mirror-filter-rule | vpc-endpoint-connection-device-type | verified-access-instance | verified-access-group | verified-access-endpoint | verified-access-policy | verified-access-trust-provider | vpn-connection-device-type | vpc-block-public-access-exclusion | vpc-encryption-control | route-server | route-server-endpoint | route-server-peer | ipam-resource-discovery | ipam-resource-discovery-association | instance-connect-endpoint | verified-access-endpoint-target | ipam-external-resource-verification-token | capacity-block | mac-modification-task | ipam-prefix-list-resolver | ipam-policy | ipam-prefix-list-resolver-target | ipam-internet-registry-association | secondary-interface | secondary-network | secondary-subnet | capacity-manager-data-export | vpn-concentrator | ipam-pool-allocation | capacity-reservation-cancellation-quote | application-status-check`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-capacityreservation-tagspecification-tags"></a>
The tags to apply to the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-capacityreservation-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
