---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetNetworkingFlexCostAllocationPolicyVersions.html
---

# GetNetworkingFlexCostAllocationPolicyVersions
<a name="API_GetNetworkingFlexCostAllocationPolicyVersions"></a>

Retrieves the versions of a flex cost allocation policy.

## Request Parameters
<a name="API_GetNetworkingFlexCostAllocationPolicyVersions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FcaPolicyId**
The ID of the flex cost allocation policy. This parameter is required.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `fcap-[a-f0-9]{17}`
Required: Yes

 **VersionsToInclude.N**
The policy versions to include in the results.
Type: Array of integers
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

## Response Elements
<a name="API_GetNetworkingFlexCostAllocationPolicyVersions_ResponseElements"></a>

The following elements are returned by the service.

 **fcaPolicyVersions**
Information about the policy versions.
Type: Array of [FlexCostAllocationPolicyVersion](API_FlexCostAllocationPolicyVersion.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetNetworkingFlexCostAllocationPolicyVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetNetworkingFlexCostAllocationPolicyVersions_Examples"></a>

### Example 1
<a name="API_GetNetworkingFlexCostAllocationPolicyVersions_Example_1"></a>

This example retrieves versions 1 and 2 of the specified flex cost allocation policy.

#### Sample Request
<a name="API_GetNetworkingFlexCostAllocationPolicyVersions_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetNetworkingFlexCostAllocationPolicyVersions
&FcaPolicyId=fcap-1234567890abcdef0
&VersionsToInclude.1=1
&VersionsToInclude.2=2
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetNetworkingFlexCostAllocationPolicyVersions_Example_1_Response"></a>

```
<GetNetworkingFlexCostAllocationPolicyVersionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>a1b2c3d4-5678-90ab-cdef-EXAMPLE55555</requestId>
    <fcaPolicyVersions>
        <item>
            <fcaPolicyId>fcap-1234567890abcdef0</fcaPolicyId>
            <version>1</version>
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
            <createdAt>2026-11-01T12:00:00.000Z</createdAt>
            <expectedEffectiveAt>2026-11-01T13:00:00.000Z</expectedEffectiveAt>
        </item>
        <item>
            <fcaPolicyId>fcap-1234567890abcdef0</fcaPolicyId>
            <version>2</version>
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
            <showBackEnabled>false</showBackEnabled>
            <createdAt>2026-11-02T09:15:00.000Z</createdAt>
            <expectedEffectiveAt>2026-11-02T11:00:00.000Z</expectedEffectiveAt>
        </item>
    </fcaPolicyVersions>
</GetNetworkingFlexCostAllocationPolicyVersionsResponse>
```

## See Also
<a name="API_GetNetworkingFlexCostAllocationPolicyVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetNetworkingFlexCostAllocationPolicyVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetNetworkingFlexCostAllocationPolicyVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetNetworkingFlexCostAllocationPolicyVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetNetworkingFlexCostAllocationPolicyVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetNetworkingFlexCostAllocationPolicyVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetNetworkingFlexCostAllocationPolicyVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetNetworkingFlexCostAllocationPolicyVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetNetworkingFlexCostAllocationPolicyVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetNetworkingFlexCostAllocationPolicyVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetNetworkingFlexCostAllocationPolicyVersions)
