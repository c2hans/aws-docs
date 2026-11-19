---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateNetworkingFlexCostAllocationPolicy.html
---

# DisassociateNetworkingFlexCostAllocationPolicy

Disassociates a flex cost allocation policy from one or more network resources.

## Request Parameters
<a name="API_DisassociateNetworkingFlexCostAllocationPolicy_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FcaPolicyAssociationIds.N**
The IDs of the policy associations to remove. You can specify up to 100 association IDs. This parameter is required.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Fixed length of 27.
Pattern: `fcapassoc-[a-f0-9]{17}`
Required: Yes

## Response Elements
<a name="API_DisassociateNetworkingFlexCostAllocationPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **fcaPolicyDisassociationFailures**
Information about the policy associations that could not be removed.
Type: Array of [FlexCostAllocationOperationFailure](API_FlexCostAllocationOperationFailure.md) objects

 **fcaPolicyDisassociations**
The IDs of the policy associations that were removed.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Length Constraints: Fixed length of 27.
Pattern: `fcapassoc-[a-f0-9]{17}`

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DisassociateNetworkingFlexCostAllocationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisassociateNetworkingFlexCostAllocationPolicy_Examples"></a>

### Example 1
<a name="API_DisassociateNetworkingFlexCostAllocationPolicy_Example_1"></a>

This example removes the specified policy association.

#### Sample Request
<a name="API_DisassociateNetworkingFlexCostAllocationPolicy_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisassociateNetworkingFlexCostAllocationPolicy
&FcaPolicyAssociationIds.1=fcapassoc-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisassociateNetworkingFlexCostAllocationPolicy_Example_1_Response"></a>

```
<DisassociateNetworkingFlexCostAllocationPolicyResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>a1b2c3d4-5678-90ab-cdef-EXAMPLE77777</requestId>
    <fcaPolicyDisassociations>
        <item>fcapassoc-1234567890abcdef0</item>
    </fcaPolicyDisassociations>
    <fcaPolicyDisassociationFailures/>
</DisassociateNetworkingFlexCostAllocationPolicyResponse>
```

## See Also
<a name="API_DisassociateNetworkingFlexCostAllocationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisassociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisassociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisassociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisassociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisassociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisassociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisassociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisassociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisassociateNetworkingFlexCostAllocationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisassociateNetworkingFlexCostAllocationPolicy)
