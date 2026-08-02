---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-servicediscovery-publicdnsnamespace-soa.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceDiscovery::PublicDnsNamespace SOA
<a name="aws-properties-servicediscovery-publicdnsnamespace-soa"></a>

Start of Authority (SOA) properties for a public or private DNS namespace.

## Syntax
<a name="aws-properties-servicediscovery-publicdnsnamespace-soa-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-servicediscovery-publicdnsnamespace-soa-syntax.json"></a>

```
{
  "[TTL](#cfn-servicediscovery-publicdnsnamespace-soa-ttl)" : {{Number}}
}
```

### YAML
<a name="aws-properties-servicediscovery-publicdnsnamespace-soa-syntax.yaml"></a>

```
  [TTL](#cfn-servicediscovery-publicdnsnamespace-soa-ttl): {{Number}}
```

## Properties
<a name="aws-properties-servicediscovery-publicdnsnamespace-soa-properties"></a>

`TTL`  <a name="cfn-servicediscovery-publicdnsnamespace-soa-ttl"></a>
The time to live (TTL) for purposes of negative caching.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
