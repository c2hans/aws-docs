---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancer.html
---

# LoadBalancer
<a name="API_LoadBalancer"></a>

Describes a load balancer.

## Contents
<a name="API_LoadBalancer_Contents"></a>

 ** arn **   <a name="Lightsail-Type-LoadBalancer-arn"></a>
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** configurationOptions **   <a name="Lightsail-Type-LoadBalancer-configurationOptions"></a>
A string to string map of the configuration options for your load balancer. Valid values are listed below.
Type: String to string map
Valid Keys: `HealthCheckPath | SessionStickinessEnabled | SessionStickiness_LB_CookieDurationSeconds | HttpsRedirectionEnabled | TlsPolicyName`
Required: No

 ** createdAt **   <a name="Lightsail-Type-LoadBalancer-createdAt"></a>
The date when your load balancer was created.
Type: Timestamp
Required: No

 ** dnsName **   <a name="Lightsail-Type-LoadBalancer-dnsName"></a>
The DNS name of your Lightsail load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** healthCheckPath **   <a name="Lightsail-Type-LoadBalancer-healthCheckPath"></a>
The path you specified to perform your health checks. If no path is specified, the load balancer tries to make a request to the default (root) page.
Type: String
Pattern: `.*\S.*`
Required: No

 ** httpsRedirectionEnabled **   <a name="Lightsail-Type-LoadBalancer-httpsRedirectionEnabled"></a>
A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.
Type: Boolean
Required: No

 ** instanceHealthSummary **   <a name="Lightsail-Type-LoadBalancer-instanceHealthSummary"></a>
An array of InstanceHealthSummary objects describing the health of the load balancer.
Type: Array of [InstanceHealthSummary](API_InstanceHealthSummary.md) objects
Required: No

 ** instancePort **   <a name="Lightsail-Type-LoadBalancer-instancePort"></a>
The port where the load balancer will direct traffic to your Lightsail instances. For HTTP traffic, it's port 80. For HTTPS traffic, it's port 443.
Type: Integer
Required: No

 ** ipAddressType **   <a name="Lightsail-Type-LoadBalancer-ipAddressType"></a>
The IP address type of the load balancer.
The possible values are `ipv4` for IPv4 only, `ipv6` for IPv6 only, and `dualstack` for IPv4 and IPv6.
Type: String
Valid Values: `dualstack | ipv4 | ipv6`
Required: No

 ** location **   <a name="Lightsail-Type-LoadBalancer-location"></a>
The AWS Region where your load balancer was created (`us-east-2a`). Lightsail automatically creates your load balancer across Availability Zones.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-LoadBalancer-name"></a>
The name of the load balancer (`my-load-balancer`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** protocol **   <a name="Lightsail-Type-LoadBalancer-protocol"></a>
The protocol you have enabled for your load balancer. Valid values are below.
You can't just have `HTTP_HTTPS`, but you can have just `HTTP`.
Type: String
Valid Values: `HTTP_HTTPS | HTTP`
Required: No

 ** publicPorts **   <a name="Lightsail-Type-LoadBalancer-publicPorts"></a>
An array of public port settings for your load balancer. For HTTP, use port 80. For HTTPS, use port 443.
Type: Array of integers
Valid Range: Minimum value of -1. Maximum value of 65535.
Required: No

 ** resourceType **   <a name="Lightsail-Type-LoadBalancer-resourceType"></a>
The resource type (`LoadBalancer`.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** state **   <a name="Lightsail-Type-LoadBalancer-state"></a>
The status of your load balancer. Valid values are below.
Type: String
Valid Values: `active | provisioning | active_impaired | failed | unknown`
Required: No

 ** supportCode **   <a name="Lightsail-Type-LoadBalancer-supportCode"></a>
The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-LoadBalancer-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** tlsCertificateSummaries **   <a name="Lightsail-Type-LoadBalancer-tlsCertificateSummaries"></a>
An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the SSL/TLS certificates. For example, if `true`, the certificate is attached to the load balancer.
Type: Array of [LoadBalancerTlsCertificateSummary](API_LoadBalancerTlsCertificateSummary.md) objects
Required: No

 ** tlsPolicyName **   <a name="Lightsail-Type-LoadBalancer-tlsPolicyName"></a>
The name of the TLS security policy for the load balancer.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

## See Also
<a name="API_LoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/LoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/LoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/LoadBalancer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
