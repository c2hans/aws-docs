---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkingFlexCostAllocationPolicies.html
---

# DeleteNetworkingFlexCostAllocationPolicies

Deletes one or more flex cost allocation policies.

## Request Parameters
<a name="API_DeleteNetworkingFlexCostAllocationPolicies_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FcaPolicyIds.N**
The IDs of the flex cost allocation policies to delete. You can specify up to 50 policy IDs. This parameter is required.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 22.
Pattern: `fcap-[a-f0-9]{17}`
Required: Yes

## Response Elements
<a name="API_DeleteNetworkingFlexCostAllocationPolicies_ResponseElements"></a>

The following elements are returned by the service.

 **failed**
Information about the policies that could not be deleted.
Type: Array of [FlexCostAllocationOperationFailure](API_FlexCostAllocationOperationFailure.md) objects

 **requestId**
The ID of the request.
Type: String

 **successful**
The IDs of the policies that were successfully deleted.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 22.
Pattern: `fcap-[a-f0-9]{17}`

## Errors
<a name="API_DeleteNetworkingFlexCostAllocationPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteNetworkingFlexCostAllocationPolicies_Examples"></a>

### Example 1
<a name="API_DeleteNetworkingFlexCostAllocationPolicies_Example_1"></a>

This example deletes the specified flex cost allocation policy.

#### Sample Request
<a name="API_DeleteNetworkingFlexCostAllocationPolicies_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteNetworkingFlexCostAllocationPolicies
&FcaPolicyIds.1=fcap-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteNetworkingFlexCostAllocationPolicies_Example_1_Response"></a>

```
<DeleteNetworkingFlexCostAllocationPoliciesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</requestId>
    <successful>
        <item>fcap-1234567890abcdef0</item>
    </successful>
    <failed/>
</DeleteNetworkingFlexCostAllocationPoliciesResponse>
```

## See Also
<a name="API_DeleteNetworkingFlexCostAllocationPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteNetworkingFlexCostAllocationPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteNetworkingFlexCostAllocationPolicies)
