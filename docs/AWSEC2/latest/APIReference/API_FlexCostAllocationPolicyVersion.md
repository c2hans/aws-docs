---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FlexCostAllocationPolicyVersion.html
---

# FlexCostAllocationPolicyVersion
<a name="API_FlexCostAllocationPolicyVersion"></a>

Describes a version of a flex cost allocation policy.

## Contents
<a name="API_FlexCostAllocationPolicyVersion_Contents"></a>

 ** createdAt **
The date and time when this version of the policy was created.
Type: Timestamp
Required: No

 ** description **
The description of this version of the policy.
Type: String
Required: No

 ** expectedEffectiveAt **
The date and time when this version of the policy is expected to apply to network traffic.
Type: Timestamp
Required: No

 ** fcaPolicyId **
The ID of the policy.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `fcap-[a-f0-9]{17}`
Required: No

 ** instanceFcaPolicyDocument **
The policy document that defines cost allocation for EC2 instances.
Type: [InstanceFlexCostAllocationPolicyDocument](API_InstanceFlexCostAllocationPolicyDocument.md) object
Required: No

 ** natFcaPolicyDocument **
The policy document that defines cost allocation for NAT gateways.
Type: [NatFlexCostAllocationPolicyDocument](API_NatFlexCostAllocationPolicyDocument.md) object
Required: No

 ** networkResourceType **
The type of network resource that the policy applies to.
Type: String
Valid Values: `natgw | pcx | ec2`
Required: No

 ** pcxFcaPolicyDocument **
The policy document that defines cost allocation for Amazon VPC peering connections.
Type: [PcxFlexCostAllocationPolicyDocument](API_PcxFlexCostAllocationPolicyDocument.md) object
Required: No

 ** showBackEnabled **
Indicates whether showback reporting is enabled for this version of the policy.
Type: Boolean
Required: No

 ** version **
The version number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_FlexCostAllocationPolicyVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FlexCostAllocationPolicyVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FlexCostAllocationPolicyVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FlexCostAllocationPolicyVersion)
