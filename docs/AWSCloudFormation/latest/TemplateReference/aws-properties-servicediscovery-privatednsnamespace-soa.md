---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-servicediscovery-privatednsnamespace-soa.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceDiscovery::PrivateDnsNamespace SOA
<a name="aws-properties-servicediscovery-privatednsnamespace-soa"></a>

Start of Authority (SOA) properties for a public or private DNS namespace.

## Syntax
<a name="aws-properties-servicediscovery-privatednsnamespace-soa-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-servicediscovery-privatednsnamespace-soa-syntax.json"></a>

```
{
  "[TTL](#cfn-servicediscovery-privatednsnamespace-soa-ttl)" : {{Number}}
}
```

### YAML
<a name="aws-properties-servicediscovery-privatednsnamespace-soa-syntax.yaml"></a>

```
  [TTL](#cfn-servicediscovery-privatednsnamespace-soa-ttl): {{Number}}
```

## Properties
<a name="aws-properties-servicediscovery-privatednsnamespace-soa-properties"></a>

`TTL`  <a name="cfn-servicediscovery-privatednsnamespace-soa-ttl"></a>
The time to live (TTL) for purposes of negative caching.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
