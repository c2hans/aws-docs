---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-internetmonitor-internetevent-clientlocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InternetMonitor::InternetEvent ClientLocation
<a name="aws-properties-internetmonitor-internetevent-clientlocation"></a>

The impacted location, such as a city, that AWS clients access application resources from.

## Syntax
<a name="aws-properties-internetmonitor-internetevent-clientlocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-internetmonitor-internetevent-clientlocation-syntax.json"></a>

```
{
  "[ASName](#cfn-internetmonitor-internetevent-clientlocation-asname)" : {{String}},
  "[ASNumber](#cfn-internetmonitor-internetevent-clientlocation-asnumber)" : {{Integer}},
  "[City](#cfn-internetmonitor-internetevent-clientlocation-city)" : {{String}},
  "[Country](#cfn-internetmonitor-internetevent-clientlocation-country)" : {{String}},
  "[Latitude](#cfn-internetmonitor-internetevent-clientlocation-latitude)" : {{Number}},
  "[Longitude](#cfn-internetmonitor-internetevent-clientlocation-longitude)" : {{Number}},
  "[Metro](#cfn-internetmonitor-internetevent-clientlocation-metro)" : {{String}},
  "[Subdivision](#cfn-internetmonitor-internetevent-clientlocation-subdivision)" : {{String}}
}
```

### YAML
<a name="aws-properties-internetmonitor-internetevent-clientlocation-syntax.yaml"></a>

```
  [ASName](#cfn-internetmonitor-internetevent-clientlocation-asname): {{String}}
  [ASNumber](#cfn-internetmonitor-internetevent-clientlocation-asnumber): {{Integer}}
  [City](#cfn-internetmonitor-internetevent-clientlocation-city): {{String}}
  [Country](#cfn-internetmonitor-internetevent-clientlocation-country): {{String}}
  [Latitude](#cfn-internetmonitor-internetevent-clientlocation-latitude): {{Number}}
  [Longitude](#cfn-internetmonitor-internetevent-clientlocation-longitude): {{Number}}
  [Metro](#cfn-internetmonitor-internetevent-clientlocation-metro): {{String}}
  [Subdivision](#cfn-internetmonitor-internetevent-clientlocation-subdivision): {{String}}
```

## Properties
<a name="aws-properties-internetmonitor-internetevent-clientlocation-properties"></a>

`ASName`  <a name="cfn-internetmonitor-internetevent-clientlocation-asname"></a>
The name of the internet service provider (ISP) or network (ASN).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ASNumber`  <a name="cfn-internetmonitor-internetevent-clientlocation-asnumber"></a>
The Autonomous System Number (ASN) of the network at an impacted location.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`City`  <a name="cfn-internetmonitor-internetevent-clientlocation-city"></a>
The name of the city where the internet event is located.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Country`  <a name="cfn-internetmonitor-internetevent-clientlocation-country"></a>
The name of the country where the internet event is located.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Latitude`  <a name="cfn-internetmonitor-internetevent-clientlocation-latitude"></a>
The latitude where the internet event is located.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Longitude`  <a name="cfn-internetmonitor-internetevent-clientlocation-longitude"></a>
The longitude where the internet event is located.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metro`  <a name="cfn-internetmonitor-internetevent-clientlocation-metro"></a>
The metro area where the health event is located.
Metro indicates a metropolitan region in the United States, such as the region around New York City. In non-US countries, this is a second-level subdivision. For example, in the United Kingdom, it could be a county, a London borough, a unitary authority, council area, and so on.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdivision`  <a name="cfn-internetmonitor-internetevent-clientlocation-subdivision"></a>
The subdivision location where the health event is located. The subdivision usually maps to states in most countries (including the United States). For United Kingdom, it maps to a country (England, Scotland, Wales) or province (Northern Ireland).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
