---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_PrivateLinkConfig.html
---

# PrivateLinkConfig
<a name="API_PrivateLinkConfig"></a>

Specifies how your AWS DataSync agent connects to AWS using a [virtual private cloud (VPC) service endpoint](https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html#choose-service-endpoint-vpc). An agent that uses a VPC endpoint isn't accessible over the public internet.

## Contents
<a name="API_PrivateLinkConfig_Contents"></a>

 ** PrivateLinkEndpoint **   <a name="DataSync-Type-PrivateLinkConfig-PrivateLinkEndpoint"></a>
Specifies the VPC endpoint provided by [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html) that your agent connects to.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 15.
Pattern: `\A(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\z`
Required: No

 ** SecurityGroupArns **   <a name="DataSync-Type-PrivateLinkConfig-SecurityGroupArns"></a>
Specifies the Amazon Resource Names (ARN) of the security group that provides DataSync access to your VPC endpoint. You can only specify one ARN.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`
Required: No

 ** SubnetArns **   <a name="DataSync-Type-PrivateLinkConfig-SubnetArns"></a>
Specifies the ARN of the subnet where DataSync creates the network interfaces that handle data transfer traffic for your tasks. You can only specify one ARN.
The subnet doesn't have to be the subnet that contains your VPC endpoint.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:subnet/subnet-[a-f0-9]+$`
Required: No

 ** VpcEndpointId **   <a name="DataSync-Type-PrivateLinkConfig-VpcEndpointId"></a>
Specifies the ID of the VPC service endpoint that's recorded for your agent. The endpoint ID is informational and isn't verified by DataSync. Your agent communicates through the private IP address in `PrivateLinkEndpoint`, which is set when you activate the agent.
Type: String
Pattern: `^vpce-[0-9a-f]{17}$`
Required: No

## See Also
<a name="API_PrivateLinkConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/PrivateLinkConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/PrivateLinkConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/PrivateLinkConfig)
