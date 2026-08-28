---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LightsailDistribution.html
---

# LightsailDistribution
<a name="API_LightsailDistribution"></a>

Describes an Amazon Lightsail content delivery network (CDN) distribution.

## Contents
<a name="API_LightsailDistribution_Contents"></a>

 ** ableToUpdateBundle **   <a name="Lightsail-Type-LightsailDistribution-ableToUpdateBundle"></a>
Indicates whether the bundle that is currently applied to your distribution, specified using the `distributionName` parameter, can be changed to another bundle.
Use the `UpdateDistributionBundle` action to change your distribution's bundle.
Type: Boolean
Required: No

 ** alternativeDomainNames **   <a name="Lightsail-Type-LightsailDistribution-alternativeDomainNames"></a>
The alternate domain names of the distribution.
Type: Array of strings
Required: No

 ** arn **   <a name="Lightsail-Type-LightsailDistribution-arn"></a>
The Amazon Resource Name (ARN) of the distribution.
Type: String
Pattern: `.*\S.*`
Required: No

 ** bundleId **   <a name="Lightsail-Type-LightsailDistribution-bundleId"></a>
The ID of the bundle currently applied to the distribution.
Type: String
Required: No

 ** cacheBehaviors **   <a name="Lightsail-Type-LightsailDistribution-cacheBehaviors"></a>
An array of objects that describe the per-path cache behavior of the distribution.
Type: Array of [CacheBehaviorPerPath](API_CacheBehaviorPerPath.md) objects
Required: No

 ** cacheBehaviorSettings **   <a name="Lightsail-Type-LightsailDistribution-cacheBehaviorSettings"></a>
An object that describes the cache behavior settings of the distribution.
Type: [CacheSettings](API_CacheSettings.md) object
Required: No

 ** certificateName **   <a name="Lightsail-Type-LightsailDistribution-certificateName"></a>
The name of the SSL/TLS certificate attached to the distribution, if any.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** createdAt **   <a name="Lightsail-Type-LightsailDistribution-createdAt"></a>
The timestamp when the distribution was created.
Type: Timestamp
Required: No

 ** defaultCacheBehavior **   <a name="Lightsail-Type-LightsailDistribution-defaultCacheBehavior"></a>
An object that describes the default cache behavior of the distribution.
Type: [CacheBehavior](API_CacheBehavior.md) object
Required: No

 ** domainName **   <a name="Lightsail-Type-LightsailDistribution-domainName"></a>
The domain name of the distribution.
Type: String
Required: No

 ** ipAddressType **   <a name="Lightsail-Type-LightsailDistribution-ipAddressType"></a>
The IP address type of the distribution.
The possible values are `ipv4` for IPv4 only, and `dualstack` for IPv4 and IPv6.
Type: String
Valid Values: `dualstack | ipv4 | ipv6`
Required: No

 ** isEnabled **   <a name="Lightsail-Type-LightsailDistribution-isEnabled"></a>
Indicates whether the distribution is enabled.
Type: Boolean
Required: No

 ** location **   <a name="Lightsail-Type-LightsailDistribution-location"></a>
An object that describes the location of the distribution, such as the AWS Region and Availability Zone.
Lightsail distributions are global resources that can reference an origin in any AWS Region, and distribute its content globally. However, all distributions are located in the `us-east-1` Region.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-LightsailDistribution-name"></a>
The name of the distribution.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** origin **   <a name="Lightsail-Type-LightsailDistribution-origin"></a>
An object that describes the origin resource of the distribution, such as a Lightsail instance, bucket, or load balancer.
The distribution pulls, caches, and serves content from the origin.
Type: [Origin](API_Origin.md) object
Required: No

 ** originPublicDNS **   <a name="Lightsail-Type-LightsailDistribution-originPublicDNS"></a>
The public DNS of the origin.
Type: String
Required: No

 ** resourceType **   <a name="Lightsail-Type-LightsailDistribution-resourceType"></a>
The Lightsail resource type (`Distribution`).
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** status **   <a name="Lightsail-Type-LightsailDistribution-status"></a>
The status of the distribution.
Type: String
Required: No

 ** supportCode **   <a name="Lightsail-Type-LightsailDistribution-supportCode"></a>
The support code. Include this code in your email to support when you have questions about your Lightsail distribution. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-LightsailDistribution-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** viewerMinimumTlsProtocolVersion **   <a name="Lightsail-Type-LightsailDistribution-viewerMinimumTlsProtocolVersion"></a>
The minimum TLS protocol version that the distribution can use to communicate with viewers.
Type: String
Required: No

## See Also
<a name="API_LightsailDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/LightsailDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/LightsailDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/LightsailDistribution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
