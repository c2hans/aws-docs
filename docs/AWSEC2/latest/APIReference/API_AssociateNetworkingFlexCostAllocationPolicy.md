---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateNetworkingFlexCostAllocationPolicy.html
---

# AssociateNetworkingFlexCostAllocationPolicy

Associates a flex cost allocation policy with one or more network resources. You can associate the policy directly with specific resources by resource ID, or you can associate it with a scope of resources in an account, Amazon VPC, or subnet.

The following limits apply:
+ A request can associate up to 20 resources.
+ A policy can have up to 100 active associations.
+ A network resource can have only one active association, across all policies. If a resource is already associated, the response includes it in the failures with the code `ResourceAlreadyAssociated`.

## Request Parameters
<a name="API_AssociateNetworkingFlexCostAllocationPolicy_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FcaPolicyId**
The ID of the flex cost allocation policy to associate. This parameter is required.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `fcap-[a-f0-9]{17}`
Required: Yes

 **NetworkResourceIds.N**
The IDs of the network resources to associate with the policy. You can specify from 1 to 20 resource IDs.
You must specify `NetworkResourceIds`, `NetworkResourceScope`, or both. A request can include at most 20 distinct resources in total.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 **NetworkResourceScope**
The scope of network resources to associate with the policy. Use a scope to associate the policy with the resources in an account, Amazon VPC, or subnet.
You must specify `NetworkResourceScope`, `NetworkResourceIds`, or both.
Type: [FlexCostAllocationNetworkResourceScope](API_FlexCostAllocationNetworkResourceScope.md) object
Required: No

## Response Elements
<a name="API_AssociateNetworkingFlexCostAllocationPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **fcaPolicyAssociationFailures**
Information about the network resources that could not be associated with the policy.
Type: Array of [FlexCostAllocationOperationFailure](API_FlexCostAllocationOperationFailure.md) objects

 **fcaPolicyAssociations**
Information about the policy associations that were created.
Type: Array of [FlexCostAllocationPolicyAssociationDescription](API_FlexCostAllocationPolicyAssociationDescription.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AssociateNetworkingFlexCostAllocationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AssociateNetworkingFlexCostAllocationPolicy_Examples"></a>

### Example 1
<a name="API_AssociateNetworkingFlexCostAllocationPolicy_Example_1"></a>

This example associates the specified flex cost allocation policy with a NAT gateway.

#### Sample Request
<a name="API_AssociateNetworkingFlexCostAllocationPolicy_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssociateNetworkingFlexCostAllocationPolicy
&FcaPolicyId=fcap-1234567890abcdef0
&NetworkResourceIds.1=nat-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssociateNetworkingFlexCostAllocationPolicy_Example_1_Response"></a>

```
<AssociateNetworkingFlexCostAllocationPolicyResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>a1b2c3d4-5678-90ab-cdef-EXAMPLE66666</requestId>
    <fcaPolicyAssociations>
        <item>
            <fcaPolicyAssociationId>fcapassoc-1234567890abcdef0</fcaPolicyAssociationId>
            <fcaPolicyId>fcap-1234567890abcdef0</fcaPolicyId>
            <networkResourceId>nat-1234567890abcdef0</networkResourceId>
            <ownerAccount>111122223333</ownerAccount>
            <associatedAt>2026-11-03T08:00:00.000Z</associatedAt>
            <expectedEffectiveAt>2026-11-03T09:00:00.000Z</expectedEffectiveAt>
            <associationMode>direct</associationMode>
            <managedBy>account</managedBy>
        </item>
    </fcaPolicyAssociations>
    <fcaPolicyAssociationFailures/>
</AssociateNetworkingFlexCostAllocationPolicyResponse>
```

## See Also
<a name="API_AssociateNetworkingFlexCostAllocationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateNetworkingFlexCostAllocationPolicy)
