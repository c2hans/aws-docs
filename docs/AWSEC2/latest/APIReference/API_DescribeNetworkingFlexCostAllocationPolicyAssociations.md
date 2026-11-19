---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkingFlexCostAllocationPolicyAssociations.html
---

# DescribeNetworkingFlexCostAllocationPolicyAssociations

Describes the associations between your flex cost allocation policies and network resources. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Parameters
<a name="API_DescribeNetworkingFlexCostAllocationPolicyAssociations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FcaPolicyAssociationIds.N**
The IDs of the policy associations to describe.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Length Constraints: Fixed length of 27.
Pattern: `fcapassoc-[a-f0-9]{17}`
Required: No

 **Filters.N**
The filters.
+  `fca-policy-id` - The ID of the policy.
+  `managed-by` - The entity that manages the association (`account` \| `declarative-policy`).
+  `resource-id` - The ID of the associated network resource.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return in a single call. The range is 5 to 1000. To retrieve the remaining results, make another call with the returned `nextToken` value.
Default: 100
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeNetworkingFlexCostAllocationPolicyAssociations_ResponseElements"></a>

The following elements are returned by the service.

 **fcaPolicyAssociations**
Information about the policy associations.
Type: Array of [FlexCostAllocationPolicyAssociationDescription](API_FlexCostAllocationPolicyAssociationDescription.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeNetworkingFlexCostAllocationPolicyAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeNetworkingFlexCostAllocationPolicyAssociations_Examples"></a>

### Example 1
<a name="API_DescribeNetworkingFlexCostAllocationPolicyAssociations_Example_1"></a>

This example describes the specified policy association.

#### Sample Request
<a name="API_DescribeNetworkingFlexCostAllocationPolicyAssociations_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeNetworkingFlexCostAllocationPolicyAssociations
&FcaPolicyAssociationIds.1=fcapassoc-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeNetworkingFlexCostAllocationPolicyAssociations_Example_1_Response"></a>

```
<DescribeNetworkingFlexCostAllocationPolicyAssociationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>a1b2c3d4-5678-90ab-cdef-EXAMPLE88888</requestId>
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
</DescribeNetworkingFlexCostAllocationPolicyAssociationsResponse>
```

## See Also
<a name="API_DescribeNetworkingFlexCostAllocationPolicyAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicyAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicyAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicyAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicyAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicyAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicyAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicyAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicyAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicyAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicyAssociations)
