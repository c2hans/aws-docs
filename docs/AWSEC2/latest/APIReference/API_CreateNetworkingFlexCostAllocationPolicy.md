---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkingFlexCostAllocationPolicy.html
---

# CreateNetworkingFlexCostAllocationPolicy

Creates a flex cost allocation policy for Networking Flexible Cost Allocation (FCA), a feature of Amazon Virtual Private Cloud (Amazon VPC). The policy allocates the charges of a shared networking resource at the reporting granularity that you specify. You can create a policy for one of the following resource types: NAT gateways, Amazon VPC peering connections, or EC2 instances. Policies can allocate data transfer charges for all three types, and data processing charges for NAT gateways.

You can have up to 100 policies per account in each AWS Region, plus one additional policy per network resource type created by a declarative policy, for a maximum of 103 policies in an AWS Region.

## Request Parameters
<a name="API_CreateNetworkingFlexCostAllocationPolicy_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **Description**
A description for the policy. The description can be up to 1024 characters long.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceFcaPolicyDocument**
The policy document that defines cost allocation for EC2 instances. Provide this document when `NetworkResourceType` is `ec2`.
Type: [InstanceFlexCostAllocationPolicyDocument](API_InstanceFlexCostAllocationPolicyDocument.md) object
Required: No

 **NatFcaPolicyDocument**
The policy document that defines cost allocation for NAT gateways. Provide this document when `NetworkResourceType` is `natgw`.
Type: [NatFlexCostAllocationPolicyDocument](API_NatFlexCostAllocationPolicyDocument.md) object
Required: No

 **NetworkResourceType**
The type of network resource that the policy applies to. This parameter is required. Valid values are `natgw` (NAT gateway), `pcx` (Amazon VPC peering connection), and `ec2` (EC2 instance).
Specify the policy document that matches the resource type: `NatFcaPolicyDocument` for `natgw`, `InstanceFcaPolicyDocument` for `ec2`, or `PcxFcaPolicyDocument` for `pcx`. Don't specify a policy document for a different resource type.
Type: String
Valid Values: `natgw | pcx | ec2`
Required: Yes

 **PcxFcaPolicyDocument**
The policy document that defines cost allocation for Amazon VPC peering connections. Provide this document when `NetworkResourceType` is `pcx`.
Type: [PcxFlexCostAllocationPolicyDocument](API_PcxFlexCostAllocationPolicyDocument.md) object
Required: No

 **ShowBackEnabled**
Specifies whether showback reporting is enabled for the policy.
Default: `true`
Type: Boolean
Required: No

 **TagSpecifications.N**
The tags to assign to the policy.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateNetworkingFlexCostAllocationPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **createdAt**
The date and time when the policy was created.
Type: Timestamp

 **expectedEffectiveAt**
The date and time when the policy is expected to apply to network traffic.
Type: Timestamp

 **fcaPolicyArn**
The Amazon Resource Name (ARN) of the flex cost allocation policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 **fcaPolicyId**
The ID of the flex cost allocation policy.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `fcap-[a-f0-9]{17}`

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateNetworkingFlexCostAllocationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateNetworkingFlexCostAllocationPolicy_Examples"></a>

### Example 1
<a name="API_CreateNetworkingFlexCostAllocationPolicy_Example_1"></a>

This example creates a flex cost allocation policy for NAT gateways that reports data transfer and data processing costs at the VPC granularity.

#### Sample Request
<a name="API_CreateNetworkingFlexCostAllocationPolicy_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateNetworkingFlexCostAllocationPolicy
&NetworkResourceType=natgw
&NatFcaPolicyDocument.ReportingGranularity.1=vpc
&NatFcaPolicyDocument.Dimensions.1=data-transfer
&NatFcaPolicyDocument.Dimensions.2=data-processing
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateNetworkingFlexCostAllocationPolicy_Example_1_Response"></a>

```
<CreateNetworkingFlexCostAllocationPolicyResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</requestId>
    <fcaPolicyId>fcap-1234567890abcdef0</fcaPolicyId>
    <fcaPolicyArn>arn:aws:ec2:us-east-1:111122223333:fca-policy/fcap-1234567890abcdef0</fcaPolicyArn>
    <createdAt>2026-11-01T12:00:00.000Z</createdAt>
    <expectedEffectiveAt>2026-11-01T13:00:00.000Z</expectedEffectiveAt>
</CreateNetworkingFlexCostAllocationPolicyResponse>
```

## See Also
<a name="API_CreateNetworkingFlexCostAllocationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateNetworkingFlexCostAllocationPolicy)
