---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicediscovery-publicdnsnamespace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceDiscovery::PublicDnsNamespace
<a name="aws-resource-servicediscovery-publicdnsnamespace"></a>

Creates a public namespace based on DNS, which is visible on the internet. The namespace defines your service naming scheme. For example, if you name your namespace `example.com` and name your service `backend`, the resulting DNS name for the service is `backend.example.com`. You can discover instances that were registered with a public DNS namespace by using either a `DiscoverInstances` request or using DNS. For the current quota on the number of namespaces that you can create using the same AWS account, see [AWS Cloud Map quotas](https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html) in the *AWS Cloud Map Developer Guide*.

**Important**
The `CreatePublicDnsNamespace` API operation is not supported in the AWS GovCloud (US) Regions.

## Syntax
<a name="aws-resource-servicediscovery-publicdnsnamespace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-servicediscovery-publicdnsnamespace-syntax.json"></a>

```
{
  "Type" : "AWS::ServiceDiscovery::PublicDnsNamespace",
  "Properties" : {
      "[Description](#cfn-servicediscovery-publicdnsnamespace-description)" : {{String}},
      "[Name](#cfn-servicediscovery-publicdnsnamespace-name)" : {{String}},
      "[Properties](#cfn-servicediscovery-publicdnsnamespace-properties)" : {{Properties}},
      "[Tags](#cfn-servicediscovery-publicdnsnamespace-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-servicediscovery-publicdnsnamespace-syntax.yaml"></a>

```
Type: AWS::ServiceDiscovery::PublicDnsNamespace
Properties:
  [Description](#cfn-servicediscovery-publicdnsnamespace-description): {{String}}
  [Name](#cfn-servicediscovery-publicdnsnamespace-name): {{String}}
  [Properties](#cfn-servicediscovery-publicdnsnamespace-properties): {{
    Properties}}
  [Tags](#cfn-servicediscovery-publicdnsnamespace-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-servicediscovery-publicdnsnamespace-properties"></a>

`Description`  <a name="cfn-servicediscovery-publicdnsnamespace-description"></a>
A description for the namespace.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-servicediscovery-publicdnsnamespace-name"></a>
The name that you want to assign to this namespace.
Do not include sensitive information in the name. The name is publicly available using DNS queries.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Properties`  <a name="cfn-servicediscovery-publicdnsnamespace-properties"></a>
Properties for the public DNS namespace.
*Required*: No
*Type*: [Properties](aws-properties-servicediscovery-publicdnsnamespace-properties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-servicediscovery-publicdnsnamespace-tags"></a>
The tags for the namespace. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
*Required*: No
*Type*: Array of [Tag](aws-properties-servicediscovery-publicdnsnamespace-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: Updates are not supported.

## Return values
<a name="aws-resource-servicediscovery-publicdnsnamespace-return-values"></a>

### Ref
<a name="aws-resource-servicediscovery-publicdnsnamespace-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the value of `Id` for the namespace, such as `ns-e4anhexample0004`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-servicediscovery-publicdnsnamespace-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-servicediscovery-publicdnsnamespace-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the public namespace.

`HostedZoneId`  <a name="HostedZoneId-fn::getatt"></a>
The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a namespace.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the public namespace.

## Examples
<a name="aws-resource-servicediscovery-publicdnsnamespace--examples"></a>

### Create a public DNS namespace
<a name="aws-resource-servicediscovery-publicdnsnamespace--examples--Create_a_public_DNS_namespace"></a>

The following example creates a public DNS namespace named `example.com`.

#### JSON
<a name="aws-resource-servicediscovery-publicdnsnamespace--examples--Create_a_public_DNS_namespace--json"></a>

```
{
    "Resources": {
        "PublicDnsNamespace": {
            "Type": "AWS::ServiceDiscovery::PublicDnsNamespace",
            "Properties": {
                "Description": "AWS Cloud Map public DNS namespace for example.com website",
                "Name": "example-public-http.com",
                "Properties": {
                    "DnsProperties": {
                        "SOA": {
                            "TTL": 100
                        }
                    }
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-servicediscovery-publicdnsnamespace--examples--Create_a_public_DNS_namespace--yaml"></a>

```
Resources:
  PublicDnsNamespace:
    Type: AWS::ServiceDiscovery::PublicDnsNamespace
    Properties:
      Description: AWS Cloud Map public DNS namespace for example.com website
      Name: example-public-http.com
      Properties:
        DnsProperties:
          SOA:
            TTL: 100
```

## See also
<a name="aws-resource-servicediscovery-publicdnsnamespace--seealso"></a>
+ [CreatePublicDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePublicDnsNamespace.html) in the * AWS Cloud Map API Reference *

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
