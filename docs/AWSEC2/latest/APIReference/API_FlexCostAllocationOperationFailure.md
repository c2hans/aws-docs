---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FlexCostAllocationOperationFailure.html
---

# FlexCostAllocationOperationFailure

Describes a policy, association, or network resource that a Networking Flexible Cost Allocation operation failed to process.

## Contents
<a name="API_FlexCostAllocationOperationFailure_Contents"></a>

 ** failureCode **
The code that identifies the type of failure. Possible values are:
+  `ResourceNotFound` - (`DeleteNetworkingFlexCostAllocationPolicies`) The policy doesn't exist or isn't owned by your account.
+  `InvalidResourceState` - (`DeleteNetworkingFlexCostAllocationPolicies`) The policy has active associations.
+  `InvalidResource` - (`AssociateNetworkingFlexCostAllocationPolicy`) The resource ID is malformed, the resource type doesn't match the policy, or the scope is an account other than yours. (`DisassociateNetworkingFlexCostAllocationPolicy`) The association doesn't exist or was already removed.
+  `ResourceAlreadyAssociated` - (`AssociateNetworkingFlexCostAllocationPolicy`) The resource already has an active association.
+  `InternalError` - An internal error occurred. Retry the request.
Type: String
Required: No

 ** failureReason **
The reason for the failure.
Type: String
Required: No

 ** resourceId **
The ID of the resource that could not be processed.
Type: String
Required: No

## See Also
<a name="API_FlexCostAllocationOperationFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FlexCostAllocationOperationFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FlexCostAllocationOperationFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FlexCostAllocationOperationFailure)
