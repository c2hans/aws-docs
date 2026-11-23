---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckSourceConfig.html
---

# HealthCheckSourceConfig

A complex type that contains the virtual private cloud (VPC), subnets, and security groups for a health check source. You can't change these values after you create the source.

## Contents
<a name="API_HealthCheckSourceConfig_Contents"></a>

 ** SubnetConfigurationList **   <a name="Route53-Type-HealthCheckSourceConfig-SubnetConfigurationList"></a>
A complex type that contains two or three `SubnetConfiguration` elements, one in each Availability Zone that Route 53 uses for private endpoint health checks in the AWS Region. The Availability Zones must be distinct. Route 53 creates network interfaces in each subnet and sends health check requests from all of them.
Type: Array of [SubnetConfiguration](API_SubnetConfiguration.md) objects
Array Members: Minimum number of 2 items. Maximum number of 3 items.
Required: Yes

 ** VpcId **   <a name="Route53-Type-HealthCheckSourceConfig-VpcId"></a>
The ID of the virtual private cloud (VPC) that contains the subnets for the health check source. All subnets in `SubnetConfigurationList` must belong to this VPC.
Type: String
Length Constraints: Maximum length of 1024.
Required: Yes

## See Also
<a name="API_HealthCheckSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HealthCheckSourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HealthCheckSourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HealthCheckSourceConfig)
