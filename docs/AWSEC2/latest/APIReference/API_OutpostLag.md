---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_OutpostLag.html
---

# OutpostLag
<a name="API_OutpostLag"></a>

Describes an Outpost link aggregation group (LAG).

## Contents
<a name="API_OutpostLag_Contents"></a>

 ** LocalGatewayVirtualInterfaceIdSet.N **
The IDs of the local gateway virtual interfaces associated with the Outpost LAG.
Type: Array of strings
Required: No

 ** outpostArn **
The Amazon Resource Number (ARN) of the Outpost LAG.
Type: String
Required: No

 ** outpostLagId **
The ID of the Outpost LAG.
Type: String
Required: No

 ** ownerId **
The ID of the Outpost LAG owner.
Type: String
Required: No

 ** ServiceLinkVirtualInterfaceIdSet.N **
The service link virtual interface IDs associated with the Outpost LAG.
Type: Array of strings
Required: No

 ** state **
The current state of the Outpost LAG.
Type: String
Required: No

 ** TagSet.N **
The tags associated with the Outpost LAG.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_OutpostLag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/OutpostLag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/OutpostLag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/OutpostLag)
