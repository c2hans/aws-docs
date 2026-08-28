---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::ServiceNetworkServiceAssociation DnsEntry
<a name="aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry"></a>

The DNS information.

## Syntax
<a name="aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry-syntax.json"></a>

```
{
  "[DomainName](#cfn-vpclattice-servicenetworkserviceassociation-dnsentry-domainname)" : {{String}},
  "[HostedZoneId](#cfn-vpclattice-servicenetworkserviceassociation-dnsentry-hostedzoneid)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry-syntax.yaml"></a>

```
  [DomainName](#cfn-vpclattice-servicenetworkserviceassociation-dnsentry-domainname): {{String}}
  [HostedZoneId](#cfn-vpclattice-servicenetworkserviceassociation-dnsentry-hostedzoneid): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry-properties"></a>

`DomainName`  <a name="cfn-vpclattice-servicenetworkserviceassociation-dnsentry-domainname"></a>
The domain name of the service.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostedZoneId`  <a name="cfn-vpclattice-servicenetworkserviceassociation-dnsentry-hostedzoneid"></a>
The ID of the hosted zone.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
