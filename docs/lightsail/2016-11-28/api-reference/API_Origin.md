---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Origin.html
---

# Origin
<a name="API_Origin"></a>

Describes the origin resource of an Amazon Lightsail content delivery network (CDN) distribution.

An origin can be a Lightsail instance, bucket, or load balancer. A distribution pulls content from an origin, caches it, and serves it to viewers via a worldwide network of edge servers.

## Contents
<a name="API_Origin_Contents"></a>

 ** ipAddressType **   <a name="Lightsail-Type-Origin-ipAddressType"></a>
The IP address type that the distribution uses when connecting to the origin.
The possible values are `ipv4` for IPv4 only, `ipv6` for IPv6 only, and `dualstack` for IPv4 and IPv6.
Type: String
Valid Values: `ipv4 | ipv6 | dualstack`
Required: No

 ** name **   <a name="Lightsail-Type-Origin-name"></a>
The name of the origin resource.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** protocolPolicy **   <a name="Lightsail-Type-Origin-protocolPolicy"></a>
The protocol that your Amazon Lightsail distribution uses when establishing a connection with your origin to pull content.
Type: String
Valid Values: `http-only | https-only`
Required: No

 ** regionName **   <a name="Lightsail-Type-Origin-regionName"></a>
The AWS Region name of the origin resource.
Type: String
Valid Values: `us-east-1 | us-east-2 | us-west-1 | us-west-2 | eu-west-1 | eu-west-2 | eu-west-3 | eu-central-1 | eu-north-1 | ca-central-1 | ap-south-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | ap-northeast-2 | ap-southeast-3 | ap-southeast-5`
Required: No

 ** resourceType **   <a name="Lightsail-Type-Origin-resourceType"></a>
The resource type of the origin resource (*Instance*).
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** responseTimeout **   <a name="Lightsail-Type-Origin-responseTimeout"></a>
The amount of time, in seconds, that the distribution waits for a response after forwarding a request to the origin. The minimum timeout is 1 second, the maximum is 60 seconds, and the default (if you don't specify otherwise) is 30 seconds.
Type: Integer
Required: No

## See Also
<a name="API_Origin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Origin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Origin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Origin)
