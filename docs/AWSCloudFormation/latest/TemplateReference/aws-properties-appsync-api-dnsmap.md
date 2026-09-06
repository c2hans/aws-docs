---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-api-dnsmap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Api DnsMap
<a name="aws-properties-appsync-api-dnsmap"></a>

A map of DNS names for the Api.

## Syntax
<a name="aws-properties-appsync-api-dnsmap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-api-dnsmap-syntax.json"></a>

```
{
  "[Http](#cfn-appsync-api-dnsmap-http)" : {{String}},
  "[Realtime](#cfn-appsync-api-dnsmap-realtime)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-api-dnsmap-syntax.yaml"></a>

```
  [Http](#cfn-appsync-api-dnsmap-http): {{String}}
  [Realtime](#cfn-appsync-api-dnsmap-realtime): {{String}}
```

## Properties
<a name="aws-properties-appsync-api-dnsmap-properties"></a>

`Http`  <a name="cfn-appsync-api-dnsmap-http"></a>
The domain name of the Api's HTTP endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Realtime`  <a name="cfn-appsync-api-dnsmap-realtime"></a>
The domain name of the Api's real-time endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
