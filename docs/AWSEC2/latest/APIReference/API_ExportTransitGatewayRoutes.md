---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportTransitGatewayRoutes.html
---

# ExportTransitGatewayRoutes
<a name="API_ExportTransitGatewayRoutes"></a>

Exports routes from the specified transit gateway route table to the specified S3 bucket. By default, all routes are exported. Alternatively, you can filter by CIDR range.

The routes are saved to the specified bucket in a JSON file. For more information, see [Export route tables to Amazon S3](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#tgw-export-route-tables) in the * AWS Transit Gateways Guide*.

## Request Parameters
<a name="API_ExportTransitGatewayRoutes_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. The possible values are:
+  `attachment.transit-gateway-attachment-id` - The id of the transit gateway attachment.
+  `attachment.resource-id` - The resource id of the transit gateway attachment.
+  `route-search.exact-match` - The exact match of the specified filter.
+  `route-search.longest-prefix-match` - The longest prefix that matches the route.
+  `route-search.subnet-of-match` - The routes with a subnet that match the specified CIDR filter.
+  `route-search.supernet-of-match` - The routes with a CIDR that encompass the CIDR filter. For example, if you have 10.0.1.0/29 and 10.0.1.0/31 routes in your route table and you specify supernet-of-match as 10.0.1.0/30, then the result returns 10.0.1.0/29.
+  `state` - The state of the route (`active` \| `blackhole`).
+  `transit-gateway-route-destination-cidr-block` - The CIDR range.
+  `type` - The type of route (`propagated` \| `static`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **S3Bucket**
The name of the S3 bucket.
Type: String
Required: Yes

 **TransitGatewayRouteTableId**
The ID of the route table.
Type: String
Required: Yes

## Response Elements
<a name="API_ExportTransitGatewayRoutes_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **s3Location**
The URL of the exported file in Amazon S3. For example, s3://*bucket\_name*/VPCTransitGateway/TransitGatewayRouteTables/*file\_name*.
Type: String

## Errors
<a name="API_ExportTransitGatewayRoutes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ExportTransitGatewayRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ExportTransitGatewayRoutes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ExportTransitGatewayRoutes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ExportTransitGatewayRoutes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ExportTransitGatewayRoutes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ExportTransitGatewayRoutes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ExportTransitGatewayRoutes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ExportTransitGatewayRoutes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ExportTransitGatewayRoutes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ExportTransitGatewayRoutes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ExportTransitGatewayRoutes)
