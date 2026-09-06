---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ServiceConfiguration.html
---

# ServiceConfiguration
<a name="API_ServiceConfiguration"></a>

Describes a service configuration for a VPC endpoint service.

## Contents
<a name="API_ServiceConfiguration_Contents"></a>

 ** acceptanceRequired **
Indicates whether requests from other AWS accounts to create an endpoint to the service must first be accepted.
Type: Boolean
Required: No

 ** AvailabilityZoneIdSet.N **
The IDs of the Availability Zones in which the service is available.
Either `AvailabilityZone` or `AvailabilityZoneId` can be specified, but not both
Type: Array of strings
Required: No

 ** AvailabilityZoneSet.N **
The Availability Zones in which the service is available.
Either `AvailabilityZone` or `AvailabilityZoneId` can be specified, but not both
Type: Array of strings
Required: No

 ** BaseEndpointDnsNameSet.N **
The DNS names for the service.
Type: Array of strings
Required: No

 ** GatewayLoadBalancerArnSet.N **
The Amazon Resource Names (ARNs) of the Gateway Load Balancers for the service.
Type: Array of strings
Required: No

 ** managesVpcEndpoints **
Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted.
Type: Boolean
Required: No

 ** NetworkLoadBalancerArnSet.N **
The Amazon Resource Names (ARNs) of the Network Load Balancers for the service.
Type: Array of strings
Required: No

 ** payerResponsibility **
The payer responsibility.
Type: String
Valid Values: `ServiceOwner`
Required: No

 ** privateDnsName **
The private DNS name for the service.
Type: String
Required: No

 ** privateDnsNameConfiguration **
Information about the endpoint service private DNS name configuration.
Type: [PrivateDnsNameConfiguration](API_PrivateDnsNameConfiguration.md) object
Required: No

 ** remoteAccessEnabled **
Indicates whether consumers can access the service from a Region other than the Region where the service is hosted.
Type: Boolean
Required: No

 ** serviceId **
The ID of the service.
Type: String
Required: No

 ** serviceName **
The name of the service.
Type: String
Required: No

 ** serviceState **
The service state.
Type: String
Valid Values: `Pending | Available | Deleting | Deleted | Failed`
Required: No

 ** ServiceType.N **
The type of service.
Type: Array of [ServiceTypeDetail](API_ServiceTypeDetail.md) objects
Required: No

 ** SupportedIpAddressTypeSet.N **
The supported IP address types.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `ipv4 | ipv6`
Required: No

 ** SupportedRegionSet.N **
The supported Regions.
Type: Array of [SupportedRegionDetail](API_SupportedRegionDetail.md) objects
Required: No

 ** TagSet.N **
The tags assigned to the service.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ServiceConfiguration)
