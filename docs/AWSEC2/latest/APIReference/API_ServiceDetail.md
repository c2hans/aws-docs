---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ServiceDetail.html
---

# ServiceDetail
<a name="API_ServiceDetail"></a>

Describes a VPC endpoint service.

## Contents
<a name="API_ServiceDetail_Contents"></a>

 ** acceptanceRequired **
Indicates whether VPC endpoint connection requests to the service must be accepted by the service owner.
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

 ** managesVpcEndpoints **
Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted.
Type: Boolean
Required: No

 ** owner **
The AWS account ID of the service owner.
Type: String
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

 ** PrivateDnsNameSet.N **
The private DNS names assigned to the VPC endpoint service.
Type: Array of [PrivateDnsDetails](API_PrivateDnsDetails.md) objects
Required: No

 ** privateDnsNameVerificationState **
The verification state of the VPC endpoint service.
Consumers of the endpoint service cannot use the private name when the state is not `verified`.
Type: String
Valid Values: `pendingVerification | verified | failed`
Required: No

 ** serviceId **
The ID of the endpoint service.
Type: String
Required: No

 ** serviceName **
The name of the service.
Type: String
Required: No

 ** serviceRegion **
The Region where the service is hosted.
Type: String
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

 ** TagSet.N **
The tags assigned to the service.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcEndpointPolicySupported **
Indicates whether the service supports endpoint policies.
Type: Boolean
Required: No

## See Also
<a name="API_ServiceDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ServiceDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ServiceDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ServiceDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
