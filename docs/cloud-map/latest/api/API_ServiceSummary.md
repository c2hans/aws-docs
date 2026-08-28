---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_ServiceSummary.html
---

# ServiceSummary
<a name="API_ServiceSummary"></a>

A complex type that contains information about a specified service.

## Contents
<a name="API_ServiceSummary_Contents"></a>

 ** Arn **   <a name="cloudmap-Type-ServiceSummary-Arn"></a>
The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create it.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** CreateDate **   <a name="cloudmap-Type-ServiceSummary-CreateDate"></a>
The date and time that the service was created.
Type: Timestamp
Required: No

 ** CreatedByAccount **   <a name="cloudmap-Type-ServiceSummary-CreatedByAccount"></a>
The ID of the AWS account that created the service. If this isn't your account ID, it is the account ID of the namespace owner or of another account with which the namespace has been shared. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** Description **   <a name="cloudmap-Type-ServiceSummary-Description"></a>
The description that you specify when you create the service.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** DnsConfig **   <a name="cloudmap-Type-ServiceSummary-DnsConfig"></a>
Information about the Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
Type: [DnsConfig](API_DnsConfig.md) object
Required: No

 ** HealthCheckConfig **   <a name="cloudmap-Type-ServiceSummary-HealthCheckConfig"></a>
 *Public DNS and HTTP namespaces only.* Settings for an optional health check. If you specify settings for a health check, AWS Cloud Map associates the health check with the records that you specify in `DnsConfig`.
Type: [HealthCheckConfig](API_HealthCheckConfig.md) object
Required: No

 ** HealthCheckCustomConfig **   <a name="cloudmap-Type-ServiceSummary-HealthCheckCustomConfig"></a>
Information about an optional custom health check. A custom health check, which requires that you use a third-party health checker to evaluate the health of your resources, is useful in the following circumstances:
+ You can't use a health check that's defined by `HealthCheckConfig` because the resource isn't available over the internet. For example, you can use a custom health check when the instance is in an Amazon VPC. (To check the health of resources in a VPC, the health checker must also be in the VPC.)
+ You want to use a third-party health checker regardless of where your resources are located.
If you specify a health check configuration, you can specify either `HealthCheckCustomConfig` or `HealthCheckConfig` but not both.
Type: [HealthCheckCustomConfig](API_HealthCheckCustomConfig.md) object
Required: No

 ** Id **   <a name="cloudmap-Type-ServiceSummary-Id"></a>
The ID that AWS Cloud Map assigned to the service when you created it.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** InstanceCount **   <a name="cloudmap-Type-ServiceSummary-InstanceCount"></a>
The number of instances that are currently associated with the service. Instances that were previously associated with the service but that are deleted aren't included in the count. The count might not reflect pending registrations and deregistrations.
Type: Integer
Required: No

 ** Name **   <a name="cloudmap-Type-ServiceSummary-Name"></a>
The name of the service.
Type: String
Pattern: `((?=^.{1,127}$)^([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9])(\.([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9]))*$)|(^\.$)`
Required: No

 ** ResourceOwner **   <a name="cloudmap-Type-ServiceSummary-ResourceOwner"></a>
The ID of the AWS account that created the namespace with which the service is associated. If this isn't your account ID, it is the ID of the account that shared the namespace with your account. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** Type **   <a name="cloudmap-Type-ServiceSummary-Type"></a>
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
<a name="API_ServiceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/ServiceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/ServiceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/ServiceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
