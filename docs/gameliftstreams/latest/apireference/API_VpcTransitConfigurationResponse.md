---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_VpcTransitConfigurationResponse.html
---

# VpcTransitConfigurationResponse
<a name="API_VpcTransitConfigurationResponse"></a>

The VPC transit configuration details for a stream group location, including the Transit Gateway information needed to complete the VPC attachment setup.

## Contents
<a name="API_VpcTransitConfigurationResponse_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Ipv4CidrBlocks **   <a name="gameliftstreams-Type-VpcTransitConfigurationResponse-Ipv4CidrBlocks"></a>
The IPv4 CIDR blocks in your VPC that the stream group can access.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Pattern: `(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])/([0-9]|[1-2][0-9]|3[0-2])`
Required: No

 ** TransitGatewayId **   <a name="gameliftstreams-Type-VpcTransitConfigurationResponse-TransitGatewayId"></a>
The ID of the Transit Gateway that Amazon GameLift Streams created for this VPC connection. Use this ID when creating your VPC attachment.
Type: String
Required: No

 ** TransitGatewayResourceShareArn **   <a name="gameliftstreams-Type-VpcTransitConfigurationResponse-TransitGatewayResourceShareArn"></a>
The ARN of the AWS Resource Access Manager resource share for the Transit Gateway. You must accept this resource share before you can create a VPC attachment.
Type: String
Required: No

 ** VpcId **   <a name="gameliftstreams-Type-VpcTransitConfigurationResponse-VpcId"></a>
The ID of the Amazon VPC that is connected to the stream group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

## See Also
<a name="API_VpcTransitConfigurationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/VpcTransitConfigurationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/VpcTransitConfigurationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/VpcTransitConfigurationResponse)
