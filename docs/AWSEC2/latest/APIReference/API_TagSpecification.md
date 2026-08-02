---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TagSpecification.html
---

# TagSpecification
<a name="API_TagSpecification"></a>

The tags to apply to a resource when the resource is being created. When you specify a tag, you must specify the resource type to tag, otherwise the request will fail.

**Note**
The `Valid Values` lists all the resource types that can be tagged. However, the action you're using might not support tagging all of these resource types. If you try to tag a resource type that is unsupported for the action you're using, you'll get an error.

## Contents
<a name="API_TagSpecification_Contents"></a>

 ** ResourceType ** (request), ** resourceType ** (response)
The type of resource to tag on creation.
Type: String
Valid Values: `capacity-reservation | client-vpn-endpoint | customer-gateway | carrier-gateway | coip-pool | declarative-policies-report | dedicated-host | dhcp-options | egress-only-internet-gateway | elastic-ip | elastic-gpu | export-image-task | export-instance-task | fleet | fpga-image | host-reservation | image | image-usage-report | import-image-task | import-snapshot-task | instance | instance-event-window | internet-gateway | ipam | ipam-pool | ipam-scope | ipv4pool-ec2 | ipv6pool-ec2 | key-pair | launch-template | local-gateway | local-gateway-route-table | local-gateway-virtual-interface | local-gateway-virtual-interface-group | local-gateway-route-table-vpc-association | local-gateway-route-table-virtual-interface-group-association | natgateway | network-acl | network-interface | network-insights-analysis | network-insights-path | network-insights-access-scope | network-insights-access-scope-analysis | outpost-lag | placement-group | prefix-list | replace-root-volume-task | reserved-instances | route-table | security-group | security-group-rule | service-link-virtual-interface | snapshot | spot-fleet-request | spot-instances-request | subnet | subnet-cidr-reservation | traffic-mirror-filter | traffic-mirror-session | traffic-mirror-target | transit-gateway | transit-gateway-attachment | transit-gateway-connect-peer | transit-gateway-multicast-domain | transit-gateway-policy-table | transit-gateway-metering-policy | transit-gateway-route-table | transit-gateway-route-table-announcement | volume | vpc | vpc-endpoint | vpc-endpoint-connection | vpc-endpoint-service | vpc-endpoint-service-permission | vpc-peering-connection | vpn-connection | vpn-gateway | vpc-flow-log | capacity-reservation-fleet | traffic-mirror-filter-rule | vpc-endpoint-connection-device-type | verified-access-instance | verified-access-group | verified-access-endpoint | verified-access-policy | verified-access-trust-provider | vpn-connection-device-type | vpc-block-public-access-exclusion | vpc-encryption-control | route-server | route-server-endpoint | route-server-peer | ipam-resource-discovery | ipam-resource-discovery-association | instance-connect-endpoint | verified-access-endpoint-target | ipam-external-resource-verification-token | capacity-block | mac-modification-task | ipam-prefix-list-resolver | ipam-policy | ipam-prefix-list-resolver-target | secondary-interface | secondary-network | secondary-subnet | capacity-manager-data-export | vpn-concentrator | ipam-pool-allocation | capacity-reservation-cancellation-quote`
Required: No

 ** Tag.N **
The tags to apply to the resource.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_TagSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TagSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TagSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TagSpecification)
