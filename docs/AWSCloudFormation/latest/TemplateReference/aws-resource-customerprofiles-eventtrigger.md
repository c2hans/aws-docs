---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-eventtrigger.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventTrigger
<a name="aws-resource-customerprofiles-eventtrigger"></a>

Specifies the rules to perform an action based on customer ingested data.

## Syntax
<a name="aws-resource-customerprofiles-eventtrigger-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-eventtrigger-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::EventTrigger",
  "Properties" : {
      "[Description](#cfn-customerprofiles-eventtrigger-description)" : {{String}},
      "[DomainName](#cfn-customerprofiles-eventtrigger-domainname)" : {{String}},
      "[EventTriggerConditions](#cfn-customerprofiles-eventtrigger-eventtriggerconditions)" : {{[ EventTriggerCondition, ... ]}},
      "[EventTriggerLimits](#cfn-customerprofiles-eventtrigger-eventtriggerlimits)" : {{EventTriggerLimits}},
      "[EventTriggerName](#cfn-customerprofiles-eventtrigger-eventtriggername)" : {{String}},
      "[ObjectTypeName](#cfn-customerprofiles-eventtrigger-objecttypename)" : {{String}},
      "[SegmentFilter](#cfn-customerprofiles-eventtrigger-segmentfilter)" : {{String}},
      "[Tags](#cfn-customerprofiles-eventtrigger-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-eventtrigger-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::EventTrigger
Properties:
  [Description](#cfn-customerprofiles-eventtrigger-description): {{String}}
  [DomainName](#cfn-customerprofiles-eventtrigger-domainname): {{String}}
  [EventTriggerConditions](#cfn-customerprofiles-eventtrigger-eventtriggerconditions): {{
    - EventTriggerCondition}}
  [EventTriggerLimits](#cfn-customerprofiles-eventtrigger-eventtriggerlimits): {{
    EventTriggerLimits}}
  [EventTriggerName](#cfn-customerprofiles-eventtrigger-eventtriggername): {{String}}
  [ObjectTypeName](#cfn-customerprofiles-eventtrigger-objecttypename): {{String}}
  [SegmentFilter](#cfn-customerprofiles-eventtrigger-segmentfilter): {{String}}
  [Tags](#cfn-customerprofiles-eventtrigger-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-customerprofiles-eventtrigger-properties"></a>

`Description`  <a name="cfn-customerprofiles-eventtrigger-description"></a>
The description of the event trigger.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-customerprofiles-eventtrigger-domainname"></a>
The unique name of the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventTriggerConditions`  <a name="cfn-customerprofiles-eventtrigger-eventtriggerconditions"></a>
A list of conditions that determine when an event should trigger the destination.
*Required*: Yes
*Type*: Array of [EventTriggerCondition](aws-properties-customerprofiles-eventtrigger-eventtriggercondition.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventTriggerLimits`  <a name="cfn-customerprofiles-eventtrigger-eventtriggerlimits"></a>
Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.
*Required*: No
*Type*: [EventTriggerLimits](aws-properties-customerprofiles-eventtrigger-eventtriggerlimits.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventTriggerName`  <a name="cfn-customerprofiles-eventtrigger-eventtriggername"></a>
The unique name of the event trigger.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ObjectTypeName`  <a name="cfn-customerprofiles-eventtrigger-objecttypename"></a>
The unique name of the object type.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentFilter`  <a name="cfn-customerprofiles-eventtrigger-segmentfilter"></a>
The destination is triggered only for profiles that meet the criteria of a segment definition.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-customerprofiles-eventtrigger-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-customerprofiles-eventtrigger-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-customerprofiles-eventtrigger-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-eventtrigger-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-customerprofiles-eventtrigger-return-values-fn--getatt"></a>

####
<a name="aws-resource-customerprofiles-eventtrigger-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the event trigger was created.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp of when the event trigger was most recently updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
