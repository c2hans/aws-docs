---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsConfig.html
---

# DnsConfig
<a name="API_DnsConfig"></a>

A complex type that contains information about the Amazon Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.

## Contents
<a name="API_DnsConfig_Contents"></a>

 ** DnsRecords **   <a name="cloudmap-Type-DnsConfig-DnsRecords"></a>
An array that contains one `DnsRecord` object for each Route 53 DNS record that you want AWS Cloud Map to create when you register an instance.
The record type of a service specified in a `DnsRecord` object can't be updated. To change a record type, you need to delete the service and recreate it with a new `DnsConfig`.
Type: Array of [DnsRecord](API_DnsRecord.md) objects
Required: Yes

 ** NamespaceId **   <a name="cloudmap-Type-DnsConfig-NamespaceId"></a>
 *This member has been deprecated.*
 *Use NamespaceId in [Service](https://docs.aws.amazon.com/cloud-map/latest/api/API_Service.html) instead.*
The ID of the namespace to use for DNS configuration.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** RoutingPolicy **   <a name="cloudmap-Type-DnsConfig-RoutingPolicy"></a>
The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map creates when you register an instance and specify this service.
If you want to use this service to register instances that create alias records, specify `WEIGHTED` for the routing policy.
You can specify the following values:
MULTIVALUE
If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.
For example, suppose that the service includes configurations for one `A` record and a health check. You use the service to register 10 instances. Route 53 responds to DNS queries with IP addresses for up to eight healthy instances. If fewer than eight instances are healthy, Route 53 responds to every DNS query with the IP addresses for all of the healthy instances.
If you don't define a health check for the service, Route 53 assumes that all instances are healthy and returns the values for up to eight instances.
For more information about the multivalue routing policy, see [Multivalue Answer Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue) in the *Route 53 Developer Guide*.
WEIGHTED
Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service. Currently, all records have the same weight, so you can't route more or less traffic to any instances.
For example, suppose that the service includes configurations for one `A` record and a health check. You use the service to register 10 instances. Route 53 responds to DNS queries with the IP address for one randomly selected instance from among the healthy instances. If no instances are healthy, Route 53 responds to DNS queries as if all of the instances were healthy.
If you don't define a health check for the service, Route 53 assumes that all instances are healthy and returns the applicable value for one randomly selected instance.
For more information about the weighted routing policy, see [Weighted Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted) in the *Route 53 Developer Guide*.
Type: String
Valid Values: `MULTIVALUE | WEIGHTED`
Required: No

## See Also
<a name="API_DnsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/DnsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/DnsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/DnsConfig)
