---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnConcentrators.html
---

# DescribeVpnConcentrators
<a name="API_DescribeVpnConcentrators"></a>

Describes one or more of your VPN concentrators.

## Request Parameters
<a name="API_DescribeVpnConcentrators_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters to limit the results.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 200. Maximum value of 1000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

 **VpnConcentratorId.N**
One or more VPN concentrator IDs.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeVpnConcentrators_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **vpnConcentratorSet**
Information about the VPN concentrators.
Type: Array of [VpnConcentrator](API_VpnConcentrator.md) objects

## Errors
<a name="API_DescribeVpnConcentrators_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVpnConcentrators_Examples"></a>

### Example
<a name="API_DescribeVpnConcentrators_Example_1"></a>

This example describes all VPN Concentrators.

#### Sample Request
<a name="API_DescribeVpnConcentrators_Example_1_Request"></a>

```
https://ec2.us-east-1.amazonaws.com/?Version=2016-11-15&Action=DescribeVpnConcentrators
```

#### Sample Response
<a name="API_DescribeVpnConcentrators_Example_1_Response"></a>

```
<DescribeVpnConcentratorsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>e1d4832f-cef7-4809-b9d4-3e54e50aff7a</requestId>
    <vpnConcentratorSet>
        <item>
            <state>available</state>
            <tagSet />
            <transitGatewayAttachmentId>tgw-attach-04a445da95a6814cc</transitGatewayAttachmentId>
            <transitGatewayId>tgw-0eae06e326d7c27d8</transitGatewayId>
            <type>ipsec.1</type>
            <vpnConcentratorId>vcn-0767cb7521c5c4945</vpnConcentratorId>
        </item>
    </vpnConcentratorSet>
</DescribeVpnConcentratorsResponse>
```

## See Also
<a name="API_DescribeVpnConcentrators_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVpnConcentrators)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVpnConcentrators)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVpnConcentrators)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVpnConcentrators)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVpnConcentrators)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVpnConcentrators)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVpnConcentrators)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVpnConcentrators)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVpnConcentrators)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVpnConcentrators)
