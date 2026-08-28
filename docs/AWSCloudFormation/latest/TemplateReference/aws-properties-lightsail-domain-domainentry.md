---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-domain-domainentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Domain DomainEntry
<a name="aws-properties-lightsail-domain-domainentry"></a>

Describes a domain recordset entry.

## Syntax
<a name="aws-properties-lightsail-domain-domainentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-domain-domainentry-syntax.json"></a>

```
{
  "[Id](#cfn-lightsail-domain-domainentry-id)" : {{String}},
  "[IsAlias](#cfn-lightsail-domain-domainentry-isalias)" : {{Boolean}},
  "[Name](#cfn-lightsail-domain-domainentry-name)" : {{String}},
  "[Target](#cfn-lightsail-domain-domainentry-target)" : {{String}},
  "[Type](#cfn-lightsail-domain-domainentry-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-domain-domainentry-syntax.yaml"></a>

```
  [Id](#cfn-lightsail-domain-domainentry-id): {{String}}
  [IsAlias](#cfn-lightsail-domain-domainentry-isalias): {{Boolean}}
  [Name](#cfn-lightsail-domain-domainentry-name): {{String}}
  [Target](#cfn-lightsail-domain-domainentry-target): {{String}}
  [Type](#cfn-lightsail-domain-domainentry-type): {{String}}
```

## Properties
<a name="aws-properties-lightsail-domain-domainentry-properties"></a>

`Id`  <a name="cfn-lightsail-domain-domainentry-id"></a>
The ID of the domain recordset entry.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsAlias`  <a name="cfn-lightsail-domain-domainentry-isalias"></a>
When `true`, specifies whether the domain entry is an alias used by the Lightsail load balancer, Lightsail container service, Lightsail content delivery network (CDN) distribution, or another AWS resource. You can include an alias (A type) record in your request, which points to the DNS name of a load balancer, container service, CDN distribution, or other AWS resource and routes traffic to that resource.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-lightsail-domain-domainentry-name"></a>
The name of the domain.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-lightsail-domain-domainentry-target"></a>
The target IP address (`192.0.2.0`), or AWS name server (`ns-111.awsdns-22.com.`).
For Lightsail load balancers, the value looks like `ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com`. For Lightsail distributions, the value looks like `exampled1182ne.cloudfront.net`. For Lightsail container services, the value looks like `container-service-1.example23scljs.us-west-2.cs.amazonlightsail.com`. Be sure to also set `isAlias` to `true` when setting up an A record for a Lightsail load balancer, distribution, or container service.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-lightsail-domain-domainentry-type"></a>
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
*Required*: Yes
*Type*: String
*Allowed values*: `A | AAAA | CNAME | MX | NS | SOA | SRV | TXT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
