---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-zoneawarenessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain ZoneAwarenessConfig
<a name="aws-properties-opensearchservice-domain-zoneawarenessconfig"></a>

Specifies zone awareness configuration options. Only use if `ZoneAwarenessEnabled` is `true`.

## Syntax
<a name="aws-properties-opensearchservice-domain-zoneawarenessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-zoneawarenessconfig-syntax.json"></a>

```
{
  "[AvailabilityZoneCount](#cfn-opensearchservice-domain-zoneawarenessconfig-availabilityzonecount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-zoneawarenessconfig-syntax.yaml"></a>

```
  [AvailabilityZoneCount](#cfn-opensearchservice-domain-zoneawarenessconfig-availabilityzonecount): {{Integer}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-zoneawarenessconfig-properties"></a>

`AvailabilityZoneCount`  <a name="cfn-opensearchservice-domain-zoneawarenessconfig-availabilityzonecount"></a>
If you enabled multiple Availability Zones (AZs), the number of AZs that you want the domain to use.
Valid values are `2` and `3`. Default is 2.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
