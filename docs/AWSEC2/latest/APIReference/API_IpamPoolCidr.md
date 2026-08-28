---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPoolCidr.html
---

# IpamPoolCidr
<a name="API_IpamPoolCidr"></a>

A CIDR provisioned to an IPAM pool.

## Contents
<a name="API_IpamPoolCidr_Contents"></a>

 ** cidr **
The CIDR provisioned to the IPAM pool. A CIDR is a representation of an IP address and its associated network mask (or netmask) and refers to a range of IP addresses. An IPv4 CIDR example is `10.24.34.0/23`. An IPv6 CIDR example is `2001:DB8::/32`.
Type: String
Required: No

 ** failureReason **
Details related to why an IPAM pool CIDR failed to be provisioned.
Type: [IpamPoolCidrFailureReason](API_IpamPoolCidrFailureReason.md) object
Required: No

 ** ipamPoolCidrId **
The IPAM pool CIDR ID.
Type: String
Required: No

 ** netmaskLength **
The netmask length of the CIDR you'd like to provision to a pool. Can be used for provisioning Amazon-provided IPv6 CIDRs to top-level pools and for provisioning CIDRs to pools with source pools. Cannot be used to provision BYOIP CIDRs to top-level pools. "NetmaskLength" or "Cidr" is required.
Type: Integer
Required: No

 ** state **
The state of the CIDR.
Type: String
Valid Values: `pending-provision | provisioned | failed-provision | pending-deprovision | deprovisioned | failed-deprovision | pending-import | failed-import`
Required: No

## See Also
<a name="API_IpamPoolCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPoolCidr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPoolCidr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPoolCidr)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
