---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LocalGatewayRouteTable.html
---

# LocalGatewayRouteTable
<a name="API_LocalGatewayRouteTable"></a>

Describes a local gateway route table.

## Contents
<a name="API_LocalGatewayRouteTable_Contents"></a>

 ** localGatewayId **
The ID of the local gateway.
Type: String
Required: No

 ** localGatewayRouteTableArn **
The Amazon Resource Name (ARN) of the local gateway route table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** localGatewayRouteTableId **
The ID of the local gateway route table.
Type: String
Required: No

 ** mode **
The mode of the local gateway route table.
Type: String
Valid Values: `direct-vpc-routing | coip`
Required: No

 ** outpostArn **
The Amazon Resource Name (ARN) of the Outpost.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the local gateway route table.
Type: String
Required: No

 ** state **
The state of the local gateway route table.
Type: String
Required: No

 ** stateReason **
Information about the state change.
Type: [StateReason](API_StateReason.md) object
Required: No

 ** TagSet.N **
The tags assigned to the local gateway route table.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_LocalGatewayRouteTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LocalGatewayRouteTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LocalGatewayRouteTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LocalGatewayRouteTable)
