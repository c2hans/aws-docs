---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_InstanceSummary.html
---

# InstanceSummary
<a name="API_InstanceSummary"></a>

A complex type that contains information about the instances that you registered by using a specified service.

## Contents
<a name="API_InstanceSummary_Contents"></a>

 ** Attributes **   <a name="cloudmap-Type-InstanceSummary-Attributes"></a>
A string map that contains the following information:
+ The attributes that are associated with the instance.
+ For each attribute, the applicable value.
Supported attribute keys include the following:
AWS\_ALIAS\_DNS\_NAME
For an alias record that routes traffic to an Elastic Load Balancing load balancer, the DNS name that's associated with the load balancer.
AWS\_EC2\_INSTANCE\_ID (HTTP namespaces only)
The Amazon EC2 instance ID for the instance. When the `AWS_EC2_INSTANCE_ID` attribute is specified, then the `AWS_INSTANCE_IPV4` attribute contains the primary private IPv4 address.
AWS\_INIT\_HEALTH\_STATUS
If the service configuration includes `HealthCheckCustomConfig`, you can optionally use `AWS_INIT_HEALTH_STATUS` to specify the initial status of the custom health check, `HEALTHY` or `UNHEALTHY`. If you don't specify a value for `AWS_INIT_HEALTH_STATUS`, the initial status is `HEALTHY`.
AWS\_INSTANCE\_CNAME
For a `CNAME` record, the domain name that Route 53 returns in response to DNS queries (for example, `example.com`).
AWS\_INSTANCE\_IPV4
For an `A` record, the IPv4 address that Route 53 returns in response to DNS queries (for example, `192.0.2.44`).
AWS\_INSTANCE\_IPV6
For an `AAAA` record, the IPv6 address that Route 53 returns in response to DNS queries (for example, `2001:0db8:85a3:0000:0000:abcd:0001:2345`).
AWS\_INSTANCE\_PORT
For an `SRV` record, the value that Route 53 returns for the port. In addition, if the service includes `HealthCheckConfig`, the port on the endpoint that Route 53 sends requests to.
Type: String to string map
Key Length Constraints: Maximum length of 255.
Key Pattern: `^[a-zA-Z0-9!-~]+$`
Value Length Constraints: Maximum length of 1024.
Value Pattern: `^([a-zA-Z0-9!-~][ \ta-zA-Z0-9!-~]*){0,1}[a-zA-Z0-9!-~]{0,1}$`
Required: No

 ** CreatedByAccount **   <a name="cloudmap-Type-InstanceSummary-CreatedByAccount"></a>
The ID of the AWS account that registered the instance. If this isn't your account ID, it's the ID of the account that shared the namespace with your account or the ID of another account with which the namespace has been shared. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** Id **   <a name="cloudmap-Type-InstanceSummary-Id"></a>
The ID for an instance that you created by using a specified service.
Type: String
Length Constraints: Maximum length of 64.
Required: No

## See Also
<a name="API_InstanceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/InstanceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/InstanceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/InstanceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
