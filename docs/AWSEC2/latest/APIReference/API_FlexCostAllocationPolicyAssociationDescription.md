---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FlexCostAllocationPolicyAssociationDescription.html
---

# FlexCostAllocationPolicyAssociationDescription
<a name="API_FlexCostAllocationPolicyAssociationDescription"></a>

Describes an association between a flex cost allocation policy and a network resource.

## Contents
<a name="API_FlexCostAllocationPolicyAssociationDescription_Contents"></a>

 ** associatedAt **
The date and time when the association was created.
Type: Timestamp
Required: No

 ** associationMode **
The mode of the association. Valid values:
+  `direct` - The policy is associated with specific resources by resource ID.
+  `scope` - The policy is associated with a scope of resources in an account, Amazon VPC, or subnet.
Type: String
Valid Values: `direct | scope`
Required: No

 ** expectedEffectiveAt **
The date and time when the association is expected to apply to network traffic.
Type: Timestamp
Required: No

 ** fcaPolicyAssociationId **
The ID of the policy association.
Type: String
Length Constraints: Fixed length of 27.
Pattern: `fcapassoc-[a-f0-9]{17}`
Required: No

 ** fcaPolicyId **
The ID of the policy.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `fcap-[a-f0-9]{17}`
Required: No

 ** managedBy **
The entity that manages the association. Valid values are:
+  `account` - The account that owns the association created it.
+  `declarative-policy` - An AWS Organizations declarative policy created the association. You can't remove the association.
Type: String
Valid Values: `account | declarative-policy`
Required: No

 ** networkResourceId **
The ID of the associated network resource.
Type: String
Required: No

 ** ownerAccount **
The ID of the account that owns the association.
Type: String
Required: No

## See Also
<a name="API_FlexCostAllocationPolicyAssociationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FlexCostAllocationPolicyAssociationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FlexCostAllocationPolicyAssociationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FlexCostAllocationPolicyAssociationDescription)
