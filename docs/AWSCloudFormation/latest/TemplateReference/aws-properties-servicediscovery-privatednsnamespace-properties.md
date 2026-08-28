---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-servicediscovery-privatednsnamespace-properties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceDiscovery::PrivateDnsNamespace Properties
<a name="aws-properties-servicediscovery-privatednsnamespace-properties"></a>

Properties for the private DNS namespace.

## Syntax
<a name="aws-properties-servicediscovery-privatednsnamespace-properties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-servicediscovery-privatednsnamespace-properties-syntax.json"></a>

```
{
  "[DnsProperties](#cfn-servicediscovery-privatednsnamespace-properties-dnsproperties)" : {{PrivateDnsPropertiesMutable}}
}
```

### YAML
<a name="aws-properties-servicediscovery-privatednsnamespace-properties-syntax.yaml"></a>

```
  [DnsProperties](#cfn-servicediscovery-privatednsnamespace-properties-dnsproperties): {{
    PrivateDnsPropertiesMutable}}
```

## Properties
<a name="aws-properties-servicediscovery-privatednsnamespace-properties-properties"></a>

`DnsProperties`  <a name="cfn-servicediscovery-privatednsnamespace-properties-dnsproperties"></a>
DNS properties for the private DNS namespace.
*Required*: No
*Type*: [PrivateDnsPropertiesMutable](aws-properties-servicediscovery-privatednsnamespace-privatednspropertiesmutable.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
