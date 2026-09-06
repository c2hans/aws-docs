---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ServiceManagedInput.html
---

# ServiceManagedInput
<a name="API_ServiceManagedInput"></a>

Configuration for a service-managed Private Connection.

## Contents
<a name="API_ServiceManagedInput_Contents"></a>

 ** hostAddress **   <a name="devopsagent-Type-ServiceManagedInput-hostAddress"></a>
IP address or DNS name of the target resource.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9.:\-]+`
Required: Yes

 ** subnetIds **   <a name="devopsagent-Type-ServiceManagedInput-subnetIds"></a>
Subnets that the service-managed Resource Gateway will span.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `subnet-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: Yes

 ** vpcId **   <a name="devopsagent-Type-ServiceManagedInput-vpcId"></a>
VPC to create the service-managed Resource Gateway in.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: Yes

 ** certificate **   <a name="devopsagent-Type-ServiceManagedInput-certificate"></a>
Certificate for the Private Connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Required: No

 ** dnsResolution **   <a name="devopsagent-Type-ServiceManagedInput-dnsResolution"></a>
DNS resolution mode for the resource gateway. Defaults to PUBLIC when not set.
Type: String
Valid Values: `PUBLIC | IN_VPC`
Required: No

 ** ipAddressType **   <a name="devopsagent-Type-ServiceManagedInput-ipAddressType"></a>
IP address type of the service-managed Resource Gateway.
Type: String
Valid Values: `IPV4 | IPV6 | DUAL_STACK`
Required: No

 ** ipv4AddressesPerEni **   <a name="devopsagent-Type-ServiceManagedInput-ipv4AddressesPerEni"></a>
Number of IPv4 addresses in each ENI for the service-managed Resource Gateway.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 62.
Required: No

 ** portRanges **   <a name="devopsagent-Type-ServiceManagedInput-portRanges"></a>
TCP port ranges that a consumer can use to access the resource.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 11 items.
Length Constraints: Minimum length of 1.
Pattern: `((\d{1,5}\-\d{1,5})|(\d+))`
Required: No

 ** securityGroupIds **   <a name="devopsagent-Type-ServiceManagedInput-securityGroupIds"></a>
Security groups to attach to the service-managed Resource Gateway. If not specified, a default security group is created.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 11. Maximum length of 20.
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

## See Also
<a name="API_ServiceManagedInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ServiceManagedInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ServiceManagedInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ServiceManagedInput)
