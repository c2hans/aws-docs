---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FlexCostAllocationPolicyDescription.html
---

# FlexCostAllocationPolicyDescription
<a name="API_FlexCostAllocationPolicyDescription"></a>

Describes a flex cost allocation policy.

## Contents
<a name="API_FlexCostAllocationPolicyDescription_Contents"></a>

 ** description **
The description of the policy.
Type: String
Required: No

 ** fcaPolicyArn **
The Amazon Resource Name (ARN) of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
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

 ** latestVersion **
The number of the latest version of the policy.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

 ** managedBy **
The entity that manages the policy. Valid values are:
+  `account` - The account that owns the policy created it.
+  `declarative-policy` - An AWS Organizations declarative policy created the policy. You can't modify or delete the policy.
Type: String
Valid Values: `account | declarative-policy`
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

 ** ownerAccount **
The ID of the account that owns the policy.
Type: String
Required: No

 ** pcxFcaPolicyDocument **
The policy document that defines cost allocation for Amazon VPC peering connections.
Type: [PcxFlexCostAllocationPolicyDocument](API_PcxFlexCostAllocationPolicyDocument.md) object
Required: No

 ** policyCreatedAt **
The date and time when the policy was created.
Type: Timestamp
Required: No

 ** showBackEnabled **
Indicates whether showback reporting is enabled for the policy.
Type: Boolean
Required: No

 ** Tags.N **
The tags assigned to the policy.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** updatedAt **
The date and time when the policy was last updated.
Type: Timestamp
Required: No

 ** versionExpectedEffectiveAt **
The date and time when the latest version of the policy is expected to apply to network traffic. The policy configuration in this response is from the latest version.
Type: Timestamp
Required: No

## See Also
<a name="API_FlexCostAllocationPolicyDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FlexCostAllocationPolicyDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FlexCostAllocationPolicyDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FlexCostAllocationPolicyDescription)
