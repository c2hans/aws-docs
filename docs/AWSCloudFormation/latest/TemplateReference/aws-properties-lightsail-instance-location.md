---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-instance-location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Instance Location
<a name="aws-properties-lightsail-instance-location"></a>

`Location` is a property of the [AWS::Lightsail::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html) resource. It describes the location for an instance.

## Syntax
<a name="aws-properties-lightsail-instance-location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-instance-location-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-lightsail-instance-location-availabilityzone)" : {{String}},
  "[RegionName](#cfn-lightsail-instance-location-regionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-instance-location-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-lightsail-instance-location-availabilityzone): {{String}}
  [RegionName](#cfn-lightsail-instance-location-regionname): {{String}}
```

## Properties
<a name="aws-properties-lightsail-instance-location-properties"></a>

`AvailabilityZone`  <a name="cfn-lightsail-instance-location-availabilityzone"></a>
The Availability Zone for the instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionName`  <a name="cfn-lightsail-instance-location-regionname"></a>
The name of the AWS Region for the instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
