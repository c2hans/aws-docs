---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_VpcTransitConfiguration.html
---

# VpcTransitConfiguration
<a name="API_VpcTransitConfiguration"></a>

Configuration for connecting a stream group location to resources in your Amazon VPC using AWS Transit Gateway. When you specify a VPC transit configuration, Amazon GameLift Streams creates a Transit Gateway and shares it with your account using AWS Resource Access Manager. After the stream group is active, you must complete the setup by accepting the resource share, creating a VPC attachment, and configuring routing.

## Contents
<a name="API_VpcTransitConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Ipv4CidrBlocks **   <a name="gameliftstreams-Type-VpcTransitConfiguration-Ipv4CidrBlocks"></a>
A list of IPv4 CIDR blocks in your VPC that you want the stream group to be able to access. You can specify up to 5 CIDR blocks. The CIDR blocks must be valid subsets of the VPC's CIDR blocks and cannot overlap with the service VPC CIDR block.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Pattern: `(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])/([0-9]|[1-2][0-9]|3[0-2])`
Required: Yes

 ** VpcId **   <a name="gameliftstreams-Type-VpcTransitConfiguration-VpcId"></a>
The ID of the Amazon VPC that you want to connect to the stream group. The VPC must be in the same AWS account as the stream group. This value cannot be changed after the stream group is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## See Also
<a name="API_VpcTransitConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/VpcTransitConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/VpcTransitConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/VpcTransitConfiguration)
