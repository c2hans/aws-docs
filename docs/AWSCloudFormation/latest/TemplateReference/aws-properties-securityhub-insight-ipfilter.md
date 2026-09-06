---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-insight-ipfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::Insight IpFilter
<a name="aws-properties-securityhub-insight-ipfilter"></a>

The IP filter for querying findings.

## Syntax
<a name="aws-properties-securityhub-insight-ipfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-insight-ipfilter-syntax.json"></a>

```
{
  "[Cidr](#cfn-securityhub-insight-ipfilter-cidr)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-insight-ipfilter-syntax.yaml"></a>

```
  [Cidr](#cfn-securityhub-insight-ipfilter-cidr): {{String}}
```

## Properties
<a name="aws-properties-securityhub-insight-ipfilter-properties"></a>

`Cidr`  <a name="cfn-securityhub-insight-ipfilter-cidr"></a>
A finding's CIDR value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
