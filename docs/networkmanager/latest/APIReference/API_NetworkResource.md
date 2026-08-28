---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_NetworkResource.html
---

# NetworkResource
<a name="API_NetworkResource"></a>

Describes a network resource.

## Contents
<a name="API_NetworkResource_Contents"></a>

 ** AccountId **   <a name="networkmanager-Type-NetworkResource-AccountId"></a>
The AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[\s\S]*`
Required: No

 ** AwsRegion **   <a name="networkmanager-Type-NetworkResource-AwsRegion"></a>
The AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** CoreNetworkId **   <a name="networkmanager-Type-NetworkResource-CoreNetworkId"></a>
The ID of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** Definition **   <a name="networkmanager-Type-NetworkResource-Definition"></a>
Information about the resource, in JSON format. Network Manager gets this information by describing the resource using its Describe API call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** DefinitionTimestamp **   <a name="networkmanager-Type-NetworkResource-DefinitionTimestamp"></a>
The time that the resource definition was retrieved.
Type: Timestamp
Required: No

 ** Metadata **   <a name="networkmanager-Type-NetworkResource-Metadata"></a>
The resource metadata.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `[\s\S]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

 ** RegisteredGatewayArn **   <a name="networkmanager-Type-NetworkResource-RegisteredGatewayArn"></a>
The ARN of the gateway.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`
Required: No

 ** ResourceArn **   <a name="networkmanager-Type-NetworkResource-ResourceArn"></a>
The ARN of the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`
Required: No

 ** ResourceId **   <a name="networkmanager-Type-NetworkResource-ResourceId"></a>
The ID of the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** ResourceType **   <a name="networkmanager-Type-NetworkResource-ResourceType"></a>
The resource type.
The following are the supported resource types for Direct Connect:
+  `dxcon`
+  `dx-gateway`
+  `dx-vif`
The following are the supported resource types for Network Manager:
+  `attachment`
+  `connect-peer`
+  `connection`
+  `core-network`
+  `device`
+  `link`
+  `peering`
+  `site`
The following are the supported resource types for Amazon VPC:
+  `customer-gateway`
+  `transit-gateway`
+  `transit-gateway-attachment`
+  `transit-gateway-connect-peer`
+  `transit-gateway-route-table`
+  `vpn-connection`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Tags **   <a name="networkmanager-Type-NetworkResource-Tags"></a>
The tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_NetworkResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
