---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2VpcEndpointServiceDetails.html
---

# AwsEc2VpcEndpointServiceDetails
<a name="API_AwsEc2VpcEndpointServiceDetails"></a>

Contains details about the service configuration for a VPC endpoint service.

## Contents
<a name="API_AwsEc2VpcEndpointServiceDetails_Contents"></a>

 ** AcceptanceRequired **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-AcceptanceRequired"></a>
Whether requests from other AWS accounts to create an endpoint to the service must first be accepted.
Type: Boolean
Required: No

 ** AvailabilityZones **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-AvailabilityZones"></a>
The Availability Zones where the service is available.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** BaseEndpointDnsNames **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-BaseEndpointDnsNames"></a>
The DNS names for the service.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** GatewayLoadBalancerArns **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-GatewayLoadBalancerArns"></a>
The ARNs of the Gateway Load Balancers for the service.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** ManagesVpcEndpoints **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-ManagesVpcEndpoints"></a>
Whether the service manages its VPC endpoints.
Type: Boolean
Required: No

 ** NetworkLoadBalancerArns **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-NetworkLoadBalancerArns"></a>
The ARNs of the Network Load Balancers for the service.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** PrivateDnsName **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-PrivateDnsName"></a>
The private DNS name for the service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServiceId **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-ServiceId"></a>
The identifier of the service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServiceName **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-ServiceName"></a>
The name of the service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServiceState **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-ServiceState"></a>
The current state of the service. Valid values are as follows:
+  `Available`
+  `Deleted`
+  `Deleting`
+  `Failed`
+  `Pending`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServiceType **   <a name="securityhub-Type-AwsEc2VpcEndpointServiceDetails-ServiceType"></a>
The types for the service.
Type: Array of [AwsEc2VpcEndpointServiceServiceTypeDetails](API_AwsEc2VpcEndpointServiceServiceTypeDetails.md) objects
Required: No

## See Also
<a name="API_AwsEc2VpcEndpointServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2VpcEndpointServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2VpcEndpointServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2VpcEndpointServiceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
