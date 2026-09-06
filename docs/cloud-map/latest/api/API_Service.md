---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_Service.html
---

# Service
<a name="API_Service"></a>

A complex type that contains information about the specified service.

## Contents
<a name="API_Service_Contents"></a>

 ** Arn **   <a name="cloudmap-Type-Service-Arn"></a>
The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create it.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** CreateDate **   <a name="cloudmap-Type-Service-CreateDate"></a>
The date and time that the service was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreateDate` is accurate to milliseconds. For example, the value `1516925490.087` represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** CreatedByAccount **   <a name="cloudmap-Type-Service-CreatedByAccount"></a>
The ID of the AWS account that created the service. If this isn't your account ID, it is the ID of account of the namespace owner or of another account with which the namespace has been shared. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** CreatorRequestId **   <a name="cloudmap-Type-Service-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string (for example, a date/timestamp).
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** Description **   <a name="cloudmap-Type-Service-Description"></a>
The description of the service.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** DnsConfig **   <a name="cloudmap-Type-Service-DnsConfig"></a>
A complex type that contains information about the Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
The record types of a service can only be changed by deleting the service and recreating it with a new `Dnsconfig`.
Type: [DnsConfig](API_DnsConfig.md) object
Required: No

 ** HealthCheckConfig **   <a name="cloudmap-Type-Service-HealthCheckConfig"></a>
 *Public DNS and HTTP namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, AWS Cloud Map associates the health check with the records that you specify in `DnsConfig`.
For information about the charges for health checks, see [Amazon Route 53 Pricing](http://aws.amazon.com/route53/pricing/).
Type: [HealthCheckConfig](API_HealthCheckConfig.md) object
Required: No

 ** HealthCheckCustomConfig **   <a name="cloudmap-Type-Service-HealthCheckCustomConfig"></a>
A complex type that contains information about an optional custom health check.
If you specify a health check configuration, you can specify either `HealthCheckCustomConfig` or `HealthCheckConfig` but not both.
Type: [HealthCheckCustomConfig](API_HealthCheckCustomConfig.md) object
Required: No

 ** Id **   <a name="cloudmap-Type-Service-Id"></a>
The ID that AWS Cloud Map assigned to the service when you created it.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** InstanceCount **   <a name="cloudmap-Type-Service-InstanceCount"></a>
The number of instances that are currently associated with the service. Instances that were previously associated with the service but that are deleted aren't included in the count. The count might not reflect pending registrations and deregistrations.
Type: Integer
Required: No

 ** Name **   <a name="cloudmap-Type-Service-Name"></a>
The name of the service.
Type: String
Pattern: `((?=^.{1,127}$)^([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9])(\.([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9]))*$)|(^\.$)`
Required: No

 ** NamespaceId **   <a name="cloudmap-Type-Service-NamespaceId"></a>
The ID of the namespace that was used to create the service.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** ResourceOwner **   <a name="cloudmap-Type-Service-ResourceOwner"></a>
The ID of the AWS account that created the namespace with which the service is associated. If this isn't your account ID, it is the ID of the account that shared the namespace with your account. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** Type **   <a name="cloudmap-Type-Service-Type"></a>
Describes the systems that can be used to discover the service instances.
DNS\_HTTP
The service instances can be discovered using either DNS queries or the `DiscoverInstances` API operation.
HTTP
The service instances can only be discovered using the `DiscoverInstances` API operation.
DNS
Reserved.
Type: String
Valid Values: `HTTP | DNS_HTTP | DNS`
Required: No

## See Also
<a name="API_Service_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/Service)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/Service)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/Service)
