---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkingFlexCostAllocationPolicies.html
---

# DescribeNetworkingFlexCostAllocationPolicies

Describes one or more of your flex cost allocation policies. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Parameters
<a name="API_DescribeNetworkingFlexCostAllocationPolicies_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FcaPolicyIds.N**
The IDs of the flex cost allocation policies to describe.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Length Constraints: Fixed length of 22.
Pattern: `fcap-[a-f0-9]{17}`
Required: No

 **Filters.N**
The filters.
+  `fca-policy-id` - The ID of the policy.
+  `managed-by` - The entity that manages the policy (`account` \| `declarative-policy`).
+  `network-resource-type` - The type of network resource that the policy applies to (`natgw` \| `ec2` \| `pcx`).
+  `showback-enabled` - Indicates whether showback reporting is enabled for the policy (`true` \| `false`).
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
<a name="API_DescribeNetworkingFlexCostAllocationPolicies_ResponseElements"></a>

The following elements are returned by the service.

 **flexCostAllocationPolicies**
Information about the flex cost allocation policies.
Type: Array of [FlexCostAllocationPolicyDescription](API_FlexCostAllocationPolicyDescription.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeNetworkingFlexCostAllocationPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeNetworkingFlexCostAllocationPolicies_Examples"></a>

### Example 1
<a name="API_DescribeNetworkingFlexCostAllocationPolicies_Example_1"></a>

This example describes the specified flex cost allocation policy.

#### Sample Request
<a name="API_DescribeNetworkingFlexCostAllocationPolicies_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeNetworkingFlexCostAllocationPolicies
&FcaPolicyIds.1=fcap-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeNetworkingFlexCostAllocationPolicies_Example_1_Response"></a>

```
<DescribeNetworkingFlexCostAllocationPoliciesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</requestId>
    <flexCostAllocationPolicies>
        <item>
            <fcaPolicyId>fcap-1234567890abcdef0</fcaPolicyId>
            <fcaPolicyArn>arn:aws:ec2:us-east-1:111122223333:fca-policy/fcap-1234567890abcdef0</fcaPolicyArn>
            <networkResourceType>natgw</networkResourceType>
            <natFcaPolicyDocument>
                <ReportingGranularity>
                    <item>vpc</item>
                </ReportingGranularity>
                <Dimensions>
                    <item>data-transfer</item>
                    <item>data-processing</item>
                </Dimensions>
            </natFcaPolicyDocument>
            <showBackEnabled>true</showBackEnabled>
            <ownerAccount>111122223333</ownerAccount>
            <latestVersion>1</latestVersion>
            <policyCreatedAt>2026-11-01T12:00:00.000Z</policyCreatedAt>
            <updatedAt>2026-11-01T12:00:00.000Z</updatedAt>
            <managedBy>account</managedBy>
        </item>
    </flexCostAllocationPolicies>
</DescribeNetworkingFlexCostAllocationPoliciesResponse>
```

## See Also
<a name="API_DescribeNetworkingFlexCostAllocationPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeNetworkingFlexCostAllocationPolicies)
