---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-recordsetgroup-coordinates.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::RecordSetGroup Coordinates
<a name="aws-properties-route53-recordsetgroup-coordinates"></a>

 A complex type that lists the coordinates for a geoproximity resource record.

## Syntax
<a name="aws-properties-route53-recordsetgroup-coordinates-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-recordsetgroup-coordinates-syntax.json"></a>

```
{
  "[Latitude](#cfn-route53-recordsetgroup-coordinates-latitude)" : {{String}},
  "[Longitude](#cfn-route53-recordsetgroup-coordinates-longitude)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-recordsetgroup-coordinates-syntax.yaml"></a>

```
  [Latitude](#cfn-route53-recordsetgroup-coordinates-latitude): {{String}}
  [Longitude](#cfn-route53-recordsetgroup-coordinates-longitude): {{String}}
```

## Properties
<a name="aws-properties-route53-recordsetgroup-coordinates-properties"></a>

`Latitude`  <a name="cfn-route53-recordsetgroup-coordinates-latitude"></a>
 Specifies a coordinate of the north–south position of a geographic point on the surface of the Earth (-90 - 90).
*Required*: Yes
*Type*: String
*Pattern*: `[-+]?[0-9]{1,2}(\.[0-9]{0,2})?`
*Minimum*: `1`
*Maximum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Longitude`  <a name="cfn-route53-recordsetgroup-coordinates-longitude"></a>
 Specifies a coordinate of the east–west position of a geographic point on the surface of the Earth (-180 - 180).
*Required*: Yes
*Type*: String
*Pattern*: `[-+]?[0-9]{1,3}(\.[0-9]{0,2})?`
*Minimum*: `1`
*Maximum*: `7`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
