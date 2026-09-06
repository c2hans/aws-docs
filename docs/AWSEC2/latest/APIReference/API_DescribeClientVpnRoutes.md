---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnRoutes.html
---

# DescribeClientVpnRoutes
<a name="API_DescribeClientVpnRoutes"></a>

Describes the routes for the specified Client VPN endpoint.

## Request Parameters
<a name="API_DescribeClientVpnRoutes_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. Filter names and values are case-sensitive.
+  `destination-cidr` - The CIDR of the route destination.
+  `origin` - How the route was associated with the Client VPN endpoint (`associate` \| `add-route`).
+  `target-subnet` - The ID of the subnet through which traffic is routed.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the nextToken value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeClientVpnRoutes_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **routes**
Information about the Client VPN endpoint routes.
Type: Array of [ClientVpnRoute](API_ClientVpnRoute.md) objects

## Errors
<a name="API_DescribeClientVpnRoutes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeClientVpnRoutes_Examples"></a>

### Example
<a name="API_DescribeClientVpnRoutes_Example_1"></a>

This example describes the routes for a specific Client VPN endpoint.

#### Sample Request
<a name="API_DescribeClientVpnRoutes_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeClientVpnRoutes
&ClientVpnEndpointId.1=cvpn-endpoint-EXAMPLEc8db8d3536
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeClientVpnRoutes_Example_1_Response"></a>

```
<DescribeClientVpnRoutesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>08fb643f-4d8f-443b-b853-EXAMPLE9cc8c</requestId>
    <routes>
        <item>
            <destinationCidr>10.0.0.0/16</destinationCidr>
            <clientVpnEndpointId>cvpn-endpoint-EXAMPLEc8db8d3536</clientVpnEndpointId>
            <origin>associate</origin>
            <status>
                <code>active</code>
            </status>
            <targetSubnet>subnet-EXAMPLE18f440ab91</targetSubnet>
            <type>Nat</type>
        </item>
        <item>
            <destinationCidr>10.0.1.128/28</destinationCidr>
            <clientVpnEndpointId>cvpn-endpoint-EXAMPLEc8db8d3536</clientVpnEndpointId>
            <origin>add-route</origin>
            <status>
                <code>active</code>
            </status>
            <targetSubnet>EXAMPLE18f440ab91</targetSubnet>
            <type>Nat</type>
        </item>
    </routes>
</DescribeClientVpnRoutesResponse>
```

## See Also
<a name="API_DescribeClientVpnRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeClientVpnRoutes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeClientVpnRoutes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeClientVpnRoutes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeClientVpnRoutes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeClientVpnRoutes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeClientVpnRoutes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeClientVpnRoutes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeClientVpnRoutes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeClientVpnRoutes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeClientVpnRoutes)
