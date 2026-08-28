---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DomainEntry.html
---

# DomainEntry
<a name="API_DomainEntry"></a>

Describes a domain recordset entry.

## Contents
<a name="API_DomainEntry_Contents"></a>

 ** id **   <a name="Lightsail-Type-DomainEntry-id"></a>
The ID of the domain recordset entry.
Type: String
Pattern: `.*\S.*`
Required: No

 ** isAlias **   <a name="Lightsail-Type-DomainEntry-isAlias"></a>
When `true`, specifies whether the domain entry is an alias used by the Lightsail load balancer, Lightsail container service, Lightsail content delivery network (CDN) distribution, or another AWS resource. You can include an alias (A type) record in your request, which points to the DNS name of a load balancer, container service, CDN distribution, or other AWS resource and routes traffic to that resource.
Type: Boolean
Required: No

 ** name **   <a name="Lightsail-Type-DomainEntry-name"></a>
The name of the domain.
Type: String
Required: No

 ** options **   <a name="Lightsail-Type-DomainEntry-options"></a>
 *This member has been deprecated.*
(Discontinued) The options for the domain entry.
In releases prior to November 29, 2017, this parameter was not included in the API response. It is now discontinued.
Type: String to string map
Required: No

 ** target **   <a name="Lightsail-Type-DomainEntry-target"></a>
The target IP address (`192.0.2.0`), or AWS name server (`ns-111.awsdns-22.com.`).
For Lightsail load balancers, the value looks like `ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com`. For Lightsail distributions, the value looks like `exampled1182ne.cloudfront.net`. For Lightsail container services, the value looks like `container-service-1.example23scljs.us-west-2.cs.amazonlightsail.com`. Be sure to also set `isAlias` to `true` when setting up an A record for a Lightsail load balancer, distribution, or container service.
Type: String
Required: No

 ** type **   <a name="Lightsail-Type-DomainEntry-type"></a>
The type of domain entry, such as address for IPv4 (A), address for IPv6 (AAAA), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locator (SRV), or text (TXT).
The following domain entry types can be used:
+  `A`
+  `AAAA`
+  `CNAME`
+  `MX`
+  `NS`
+  `SOA`
+  `SRV`
+  `TXT`
Type: String
Required: No

## See Also
<a name="API_DomainEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DomainEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DomainEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DomainEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
