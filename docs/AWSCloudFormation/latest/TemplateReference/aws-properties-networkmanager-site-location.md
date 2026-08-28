---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-site-location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::Site Location
<a name="aws-properties-networkmanager-site-location"></a>

Describes a location.

## Syntax
<a name="aws-properties-networkmanager-site-location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-site-location-syntax.json"></a>

```
{
  "[Address](#cfn-networkmanager-site-location-address)" : {{String}},
  "[Latitude](#cfn-networkmanager-site-location-latitude)" : {{String}},
  "[Longitude](#cfn-networkmanager-site-location-longitude)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkmanager-site-location-syntax.yaml"></a>

```
  [Address](#cfn-networkmanager-site-location-address): {{String}}
  [Latitude](#cfn-networkmanager-site-location-latitude): {{String}}
  [Longitude](#cfn-networkmanager-site-location-longitude): {{String}}
```

## Properties
<a name="aws-properties-networkmanager-site-location-properties"></a>

`Address`  <a name="cfn-networkmanager-site-location-address"></a>
The physical address.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Latitude`  <a name="cfn-networkmanager-site-location-latitude"></a>
The latitude.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Longitude`  <a name="cfn-networkmanager-site-location-longitude"></a>
The longitude.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
