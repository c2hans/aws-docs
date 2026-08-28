---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateTagSpecificationRequest.html
---

# LaunchTemplateTagSpecificationRequest
<a name="API_LaunchTemplateTagSpecificationRequest"></a>

The tags specification for the resources that are created during instance launch.

## Contents
<a name="API_LaunchTemplateTagSpecificationRequest_Contents"></a>

 ** ResourceType **
The type of resource to tag.
Valid Values lists all resource types for Amazon EC2 that can be tagged. When you create a launch template, you can specify tags for the following resource types only: `instance` \| `volume` \| `network-interface` \| `spot-instances-request`. If the instance does not include the resource type that you specify, the instance launch fails. For example, not all instance types include a volume.
To tag a resource after it has been created, see [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html).
Type: String
Valid Values: `capacity-reservation | client-vpn-endpoint | customer-gateway | carrier-gateway | coip-pool | declarative-policies-report | dedicated-host | dhcp-options | egress-only-internet-gateway | elastic-ip | elastic-gpu | export-image-task | export-instance-task | fleet | fpga-image | host-reservation | image | image-usage-report | import-image-task | import-snapshot-task | instance | instance-event-window | internet-gateway | ipam | ipam-pool | ipam-scope | ipv4pool-ec2 | ipv6pool-ec2 | key-pair | launch-template | local-gateway | local-gateway-route-table | local-gateway-virtual-interface | local-gateway-virtual-interface-group | local-gateway-route-table-vpc-association | local-gateway-route-table-virtual-interface-group-association | natgateway | network-acl | network-interface | network-insights-analysis | network-insights-path | network-insights-access-scope | network-insights-access-scope-analysis | outpost-lag | placement-group | prefix-list | replace-root-volume-task | reserved-instances | route-table | security-group | security-group-rule | service-link-virtual-interface | snapshot | spot-fleet-request | spot-instances-request | subnet | subnet-cidr-reservation | traffic-mirror-filter | traffic-mirror-session | traffic-mirror-target | transit-gateway | transit-gateway-attachment | transit-gateway-connect-peer | transit-gateway-multicast-domain | transit-gateway-policy-table | transit-gateway-metering-policy | transit-gateway-route-table | transit-gateway-route-table-announcement | volume | vpc | vpc-endpoint | vpc-endpoint-connection | vpc-endpoint-service | vpc-endpoint-service-permission | vpc-peering-connection | vpn-connection | vpn-gateway | vpc-flow-log | capacity-reservation-fleet | traffic-mirror-filter-rule | vpc-endpoint-connection-device-type | verified-access-instance | verified-access-group | verified-access-endpoint | verified-access-policy | verified-access-trust-provider | vpn-connection-device-type | vpc-block-public-access-exclusion | vpc-encryption-control | route-server | route-server-endpoint | route-server-peer | ipam-resource-discovery | ipam-resource-discovery-association | instance-connect-endpoint | verified-access-endpoint-target | ipam-external-resource-verification-token | capacity-block | mac-modification-task | ipam-prefix-list-resolver | ipam-policy | ipam-prefix-list-resolver-target | ipam-internet-registry-association | secondary-interface | secondary-network | secondary-subnet | capacity-manager-data-export | vpn-concentrator | ipam-pool-allocation | capacity-reservation-cancellation-quote | application-status-check`
Required: No

 ** Tag.N **
The tags to apply to the resource.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_LaunchTemplateTagSpecificationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateTagSpecificationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateTagSpecificationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateTagSpecificationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
