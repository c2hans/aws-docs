---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayMulticastDomains.html
---

# DescribeTransitGatewayMulticastDomains
<a name="API_DescribeTransitGatewayMulticastDomains"></a>

Describes one or more transit gateway multicast domains.

## Request Parameters
<a name="API_DescribeTransitGatewayMulticastDomains_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. The possible values are:
+  `state` - The state of the transit gateway multicast domain. Valid values are `pending` \| `available` \| `deleting` \| `deleted`.
+  `transit-gateway-id` - The ID of the transit gateway.
+  `transit-gateway-multicast-domain-id` - The ID of the transit gateway multicast domain.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

 **TransitGatewayMulticastDomainIds.N**
The ID of the transit gateway multicast domain.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeTransitGatewayMulticastDomains_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **transitGatewayMulticastDomains**
Information about the transit gateway multicast domains.
Type: Array of [TransitGatewayMulticastDomain](API_TransitGatewayMulticastDomain.md) objects

## Errors
<a name="API_DescribeTransitGatewayMulticastDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeTransitGatewayMulticastDomains_Examples"></a>

### Example 1
<a name="API_DescribeTransitGatewayMulticastDomains_Example_1"></a>

This example describes your multicast domains.

#### Sample Request
<a name="API_DescribeTransitGatewayMulticastDomains_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeTransitGatewayMulticastDomains
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTransitGatewayMulticastDomains_Example_1_Response"></a>

```
<DescribeTransitGatewayMulticastDomainsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>e19ec53b-f3f5-4eae-97c3-a9605EXAMPLE</requestId>
    <transitGatewayMulticastDomains>
        <item>
            <creationTime>2019-11-19T22:05:50.000Z</creationTime>
            <state>available</state>
            <tagSet/>
            <transitGatewayId>tgw-06150e5ae0EXAMPLE</transitGatewayId>
            <transitGatewayMulticastDomainId>tgw-mcast-domain-0c4905cef7EXAMPLE</transitGatewayMulticastDomainId>
        </item>
    </transitGatewayMulticastDomains>
</DescribeTransitGatewayMulticastDomainsResponse>
```

## See Also
<a name="API_DescribeTransitGatewayMulticastDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeTransitGatewayMulticastDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeTransitGatewayMulticastDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeTransitGatewayMulticastDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeTransitGatewayMulticastDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeTransitGatewayMulticastDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeTransitGatewayMulticastDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeTransitGatewayMulticastDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeTransitGatewayMulticastDomains)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeTransitGatewayMulticastDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeTransitGatewayMulticastDomains)
