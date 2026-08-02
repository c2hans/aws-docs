---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPolicyDocument.html
---

# IpamPolicyDocument
<a name="API_IpamPolicyDocument"></a>

Information about an IPAM policy.

## Contents
<a name="API_IpamPolicyDocument_Contents"></a>

 ** AllocationRuleSet.N **
The allocation rules in the IPAM policy document.
Allocation rules are optional configurations within an IPAM policy that map AWS resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.
Type: Array of [IpamPolicyAllocationRule](API_IpamPolicyAllocationRule.md) objects
Required: No

 ** ipamPolicyId **
The ID of the IPAM policy.
Type: String
Required: No

 ** locale **
The locale of the IPAM policy document.
Type: String
Required: No

 ** resourceType **
The resource type of the IPAM policy document.
The AWS service or resource type that can use IP addresses through IPAM policies. Supported services and resource types include:
+ Elastic IP addresses
Type: String
Valid Values: `alb | eip | rds | rnat`
Required: No

## See Also
<a name="API_IpamPolicyDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPolicyDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPolicyDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPolicyDocument)
