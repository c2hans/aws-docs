---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ServiceManagedInput.html
---

# ServiceManagedInput
<a name="API_ServiceManagedInput"></a>

The configuration for a service-managed private connection.

## Contents
<a name="API_ServiceManagedInput_Contents"></a>

 ** hostAddress **   <a name="securityagent-Type-ServiceManagedInput-hostAddress"></a>
The IP address or DNS name of the target resource.
Type: String
Required: Yes

 ** subnetIds **   <a name="securityagent-Type-ServiceManagedInput-subnetIds"></a>
The subnets that the service-managed resource gateway spans.
Type: Array of strings
Required: Yes

 ** vpcId **   <a name="securityagent-Type-ServiceManagedInput-vpcId"></a>
The VPC to create the service-managed resource gateway in.
Type: String
Required: Yes

 ** certificate **   <a name="securityagent-Type-ServiceManagedInput-certificate"></a>
The certificate for the private connection.
Type: String
Required: No

 ** dnsResolution **   <a name="securityagent-Type-ServiceManagedInput-dnsResolution"></a>
The DNS resolution mode for the resource gateway. Defaults to PUBLIC when not set.
Type: String
Valid Values: `PUBLIC | IN_VPC`
Required: No

 ** ipAddressType **   <a name="securityagent-Type-ServiceManagedInput-ipAddressType"></a>
The IP address type of the service-managed resource gateway.
Type: String
Valid Values: `IPV4 | IPV6 | DUAL_STACK`
Required: No

 ** ipv4AddressesPerEni **   <a name="securityagent-Type-ServiceManagedInput-ipv4AddressesPerEni"></a>
The number of IPv4 addresses in each elastic network interface for the service-managed resource gateway.
Type: Integer
Required: No

 ** portRanges **   <a name="securityagent-Type-ServiceManagedInput-portRanges"></a>
The TCP port ranges that a consumer can use to access the resource.
Type: Array of strings
Required: No

 ** securityGroupIds **   <a name="securityagent-Type-ServiceManagedInput-securityGroupIds"></a>
The security groups to attach to the service-managed resource gateway.
Type: Array of strings
Required: No

## See Also
<a name="API_ServiceManagedInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ServiceManagedInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ServiceManagedInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ServiceManagedInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
