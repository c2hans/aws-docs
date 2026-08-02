---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayConnectPeers.html
---

# DescribeTransitGatewayConnectPeers
<a name="API_DescribeTransitGatewayConnectPeers"></a>

Describes one or more Connect peers.

## Request Parameters
<a name="API_DescribeTransitGatewayConnectPeers_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. The possible values are:
+  `state` - The state of the Connect peer (`pending` \| `available` \| `deleting` \| `deleted`).
+  `transit-gateway-attachment-id` - The ID of the attachment.
+  `transit-gateway-connect-peer-id` - The ID of the Connect peer.
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

 **TransitGatewayConnectPeerIds.N**
The IDs of the Connect peers.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeTransitGatewayConnectPeers_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **transitGatewayConnectPeerSet**
Information about the Connect peers.
Type: Array of [TransitGatewayConnectPeer](API_TransitGatewayConnectPeer.md) objects

## Errors
<a name="API_DescribeTransitGatewayConnectPeers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeTransitGatewayConnectPeers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeTransitGatewayConnectPeers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeTransitGatewayConnectPeers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeTransitGatewayConnectPeers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeTransitGatewayConnectPeers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeTransitGatewayConnectPeers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeTransitGatewayConnectPeers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeTransitGatewayConnectPeers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeTransitGatewayConnectPeers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeTransitGatewayConnectPeers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeTransitGatewayConnectPeers)
