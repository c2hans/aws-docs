---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_Instance.html
---

# Instance
<a name="API_Instance"></a>

A complex type that contains information about an instance that AWS Cloud Map creates when you submit a `RegisterInstance` request.

## Contents
<a name="API_Instance_Contents"></a>

 ** Id **   <a name="cloudmap-Type-Instance-Id"></a>
An identifier that you want to associate with the instance. Note the following:
+ If the service that's specified by `ServiceId` includes settings for an `SRV` record, the value of `InstanceId` is automatically included as part of the value for the `SRV` record. For more information, see [DnsRecord > Type](https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsRecord.html#cloudmap-Type-DnsRecord-Type).
+ You can use this value to update an existing instance.
+ To register a new instance, you must specify a value that's unique among instances that you register by using the same service.
+ If you specify an existing `InstanceId` and `ServiceId`, AWS Cloud Map updates the existing DNS records. If there's also an existing health check, AWS Cloud Map deletes the old health check and creates a new one.
**Note**
The health check isn't deleted immediately, so it will still appear for a while if you submit a `ListHealthChecks` request, for example.
Type: String
Length Constraints: Maximum length of 64.
Required: Yes

 ** Attributes **   <a name="cloudmap-Type-Instance-Attributes"></a>
A string map that contains the following information for the service that you specify in `ServiceId`:
+ The attributes that apply to the records that are defined in the service.
+ For each attribute, the applicable value.
Do not include sensitive information in the attributes if the namespace is discoverable by public DNS queries.
Supported attribute keys include the following:
AWS\_ALIAS\_DNS\_NAME
If you want AWS Cloud Map to create a Route 53 alias record that routes traffic to an Elastic Load Balancing load balancer, specify the DNS name that's associated with the load balancer. For information about how to get the DNS name, see [AliasTarget->DNSName](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-DNSName) in the *Route 53 API Reference*.
Note the following:
+ The configuration for the service that's specified by `ServiceId` must include settings for an `A` record, an `AAAA` record, or both.
+ In the service that's specified by `ServiceId`, the value of `RoutingPolicy` must be `WEIGHTED`.
+ If the service that's specified by `ServiceId` includes `HealthCheckConfig` settings, AWS Cloud Map creates the health check, but it won't associate the health check with the alias record.
+ Auto naming currently doesn't support creating alias records that route traffic to AWS resources other than ELB load balancers.
+ If you specify a value for `AWS_ALIAS_DNS_NAME`, don't specify values for any of the `AWS_INSTANCE` attributes.
AWS\_EC2\_INSTANCE\_ID
 *HTTP namespaces only.* The Amazon EC2 instance ID for the instance. The `AWS_INSTANCE_IPV4` attribute contains the primary private IPv4 address.
AWS\_INIT\_HEALTH\_STATUS
If the service configuration includes `HealthCheckCustomConfig`, you can optionally use `AWS_INIT_HEALTH_STATUS` to specify the initial status of the custom health check, `HEALTHY` or `UNHEALTHY`. If you don't specify a value for `AWS_INIT_HEALTH_STATUS`, the initial status is `HEALTHY`.
AWS\_INSTANCE\_CNAME
If the service configuration includes a `CNAME` record, the domain name that you want Route 53 to return in response to DNS queries (for example, `example.com`).
This value is required if the service specified by `ServiceId` includes settings for an `CNAME` record.
AWS\_INSTANCE\_IPV4
If the service configuration includes an `A` record, the IPv4 address that you want Route 53 to return in response to DNS queries (for example, `192.0.2.44`).
This value is required if the service specified by `ServiceId` includes settings for an `A` record. If the service includes settings for an `SRV` record, you must specify a value for `AWS_INSTANCE_IPV4`, `AWS_INSTANCE_IPV6`, or both.
AWS\_INSTANCE\_IPV6
If the service configuration includes an `AAAA` record, the IPv6 address that you want Route 53 to return in response to DNS queries (for example, `2001:0db8:85a3:0000:0000:abcd:0001:2345`).
This value is required if the service specified by `ServiceId` includes settings for an `AAAA` record. If the service includes settings for an `SRV` record, you must specify a value for `AWS_INSTANCE_IPV4`, `AWS_INSTANCE_IPV6`, or both.
AWS\_INSTANCE\_PORT
If the service includes an `SRV` record, the value that you want Route 53 to return for the port.
If the service includes `HealthCheckConfig`, the port on the endpoint that you want Route 53 to send requests to.
This value is required if you specified settings for an `SRV` record or a Route 53 health check when you created the service.
Type: String to string map
Key Length Constraints: Maximum length of 255.
Key Pattern: `^[a-zA-Z0-9!-~]+$`
Value Length Constraints: Maximum length of 1024.
Value Pattern: `^([a-zA-Z0-9!-~][ \ta-zA-Z0-9!-~]*){0,1}[a-zA-Z0-9!-~]{0,1}$`
Required: No

 ** CreatedByAccount **   <a name="cloudmap-Type-Instance-CreatedByAccount"></a>
The ID of the AWS account that registered the instance. If this isn't your account ID, it's the ID of the account that shared the namespace with your account or the ID of another account with which the namespace has been shared. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** CreatorRequestId **   <a name="cloudmap-Type-Instance-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed `RegisterInstance` requests to be retried without the risk of executing the operation twice. You must use a unique `CreatorRequestId` string every time you submit a `RegisterInstance` request if you're registering additional instances for the same namespace and service. `CreatorRequestId` can be any unique string (for example, a date/time stamp).
Type: String
Length Constraints: Maximum length of 64.
Required: No

## See Also
<a name="API_Instance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/Instance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/Instance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/Instance)
