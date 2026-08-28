---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElbv2LoadBalancerDetails.html
---

# AwsElbv2LoadBalancerDetails
<a name="API_AwsElbv2LoadBalancerDetails"></a>

Information about a load balancer.

## Contents
<a name="API_AwsElbv2LoadBalancerDetails_Contents"></a>

 ** AvailabilityZones **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-AvailabilityZones"></a>
The Availability Zones for the load balancer.
Type: Array of [AvailabilityZone](API_AvailabilityZone.md) objects
Required: No

 ** CanonicalHostedZoneId **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-CanonicalHostedZoneId"></a>
The ID of the Amazon Route 53 hosted zone associated with the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreatedTime **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-CreatedTime"></a>
Indicates when the load balancer was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DNSName **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-DNSName"></a>
The public DNS name of the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IpAddressType **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-IpAddressType"></a>
The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` (for IPv4 addresses) and `dualstack` (for IPv4 and IPv6 addresses).
Type: String
Pattern: `.*\S.*`
Required: No

 ** LoadBalancerAttributes **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-LoadBalancerAttributes"></a>
Attributes of the load balancer.
Type: Array of [AwsElbv2LoadBalancerAttribute](API_AwsElbv2LoadBalancerAttribute.md) objects
Required: No

 ** Scheme **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-Scheme"></a>
The nodes of an Internet-facing load balancer have public IP addresses.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecurityGroups **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-SecurityGroups"></a>
The IDs of the security groups for the load balancer.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** State **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-State"></a>
The state of the load balancer.
Type: [LoadBalancerState](API_LoadBalancerState.md) object
Required: No

 ** Type **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-Type"></a>
The type of load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsElbv2LoadBalancerDetails-VpcId"></a>
The ID of the VPC for the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElbv2LoadBalancerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElbv2LoadBalancerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElbv2LoadBalancerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElbv2LoadBalancerDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
