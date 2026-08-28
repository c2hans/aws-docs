---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventtrigger-eventtriggerlimits.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventTrigger EventTriggerLimits
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggerlimits"></a>

Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.

## Syntax
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggerlimits-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggerlimits-syntax.json"></a>

```
{
  "[EventExpiration](#cfn-customerprofiles-eventtrigger-eventtriggerlimits-eventexpiration)" : {{Integer}},
  "[Periods](#cfn-customerprofiles-eventtrigger-eventtriggerlimits-periods)" : {{[ Period, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggerlimits-syntax.yaml"></a>

```
  [EventExpiration](#cfn-customerprofiles-eventtrigger-eventtriggerlimits-eventexpiration): {{Integer}}
  [Periods](#cfn-customerprofiles-eventtrigger-eventtriggerlimits-periods): {{
    - Period}}
```

## Properties
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggerlimits-properties"></a>

`EventExpiration`  <a name="cfn-customerprofiles-eventtrigger-eventtriggerlimits-eventexpiration"></a>
Specifies that an event will only trigger the destination if it is processed within a certain latency period.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Periods`  <a name="cfn-customerprofiles-eventtrigger-eventtriggerlimits-periods"></a>
A list of time periods during which the limits apply.
*Required*: No
*Type*: Array of [Period](aws-properties-customerprofiles-eventtrigger-period.md)
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
