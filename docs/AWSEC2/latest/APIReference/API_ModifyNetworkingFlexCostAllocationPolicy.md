---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyNetworkingFlexCostAllocationPolicy.html
---

# ModifyNetworkingFlexCostAllocationPolicy

Modifies a flex cost allocation policy. Changing a policy document or `ShowBackEnabled` creates a new version of the policy. Changing only the description doesn't create a new version.

A policy can have up to 100 versions. Versions are never removed, so after a policy reaches 100 versions, you can't change its policy document or `ShowBackEnabled`. Policies that are managed by a declarative policy aren't subject to this limit.

## Request Parameters
<a name="API_ModifyNetworkingFlexCostAllocationPolicy_RequestParameters"></a>

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

 **FcaPolicyId**
The ID of the flex cost allocation policy to modify. This parameter is required.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `fcap-[a-f0-9]{17}`
Required: Yes

 **InstanceFcaPolicyDocument**
The updated policy document that defines cost allocation for EC2 instances.
Type: [InstanceFlexCostAllocationPolicyDocument](API_InstanceFlexCostAllocationPolicyDocument.md) object
Required: No

 **NatFcaPolicyDocument**
The updated policy document that defines cost allocation for NAT gateways.
Type: [NatFlexCostAllocationPolicyDocument](API_NatFlexCostAllocationPolicyDocument.md) object
Required: No

 **PcxFcaPolicyDocument**
The updated policy document that defines cost allocation for Amazon VPC peering connections.
Type: [PcxFlexCostAllocationPolicyDocument](API_PcxFlexCostAllocationPolicyDocument.md) object
Required: No

 **ShowBackEnabled**
Specifies whether showback reporting is enabled for the policy. If you omit this parameter, the current setting is unchanged.
Type: Boolean
Required: No

## Response Elements
<a name="API_ModifyNetworkingFlexCostAllocationPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **fcaPolicyId**
The ID of the flex cost allocation policy.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `fcap-[a-f0-9]{17}`

 **requestId**
The ID of the request.
Type: String

 **updatedAt**
The date and time when the policy was updated.
Type: Timestamp

 **version**
The version number of the policy that this modification created.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.

 **versionExpectedEffectiveAt**
The date and time when the new version of the policy is expected to apply to network traffic.
Type: Timestamp

## Errors
<a name="API_ModifyNetworkingFlexCostAllocationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyNetworkingFlexCostAllocationPolicy_Examples"></a>

### Example 1
<a name="API_ModifyNetworkingFlexCostAllocationPolicy_Example_1"></a>

This example disables showback reporting for the specified flex cost allocation policy, which creates a new version of the policy.

#### Sample Request
<a name="API_ModifyNetworkingFlexCostAllocationPolicy_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyNetworkingFlexCostAllocationPolicy
&FcaPolicyId=fcap-1234567890abcdef0
&ShowBackEnabled=false
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyNetworkingFlexCostAllocationPolicy_Example_1_Response"></a>

```
<ModifyNetworkingFlexCostAllocationPolicyResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>a1b2c3d4-5678-90ab-cdef-EXAMPLE44444</requestId>
    <fcaPolicyId>fcap-1234567890abcdef0</fcaPolicyId>
    <updatedAt>2026-11-02T09:00:00.000Z</updatedAt>
    <version>2</version>
    <versionExpectedEffectiveAt>2026-11-02T10:00:00.000Z</versionExpectedEffectiveAt>
</ModifyNetworkingFlexCostAllocationPolicyResponse>
```

## See Also
<a name="API_ModifyNetworkingFlexCostAllocationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyNetworkingFlexCostAllocationPolicy)
