---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-fleet-computecapacity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Fleet ComputeCapacity
<a name="aws-properties-appstream-fleet-computecapacity"></a>

The desired capacity for a fleet.

## Syntax
<a name="aws-properties-appstream-fleet-computecapacity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-fleet-computecapacity-syntax.json"></a>

```
{
  "[DesiredInstances](#cfn-appstream-fleet-computecapacity-desiredinstances)" : {{Integer}},
  "[DesiredSessions](#cfn-appstream-fleet-computecapacity-desiredsessions)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appstream-fleet-computecapacity-syntax.yaml"></a>

```
  [DesiredInstances](#cfn-appstream-fleet-computecapacity-desiredinstances): {{Integer}}
  [DesiredSessions](#cfn-appstream-fleet-computecapacity-desiredsessions): {{Integer}}
```

## Properties
<a name="aws-properties-appstream-fleet-computecapacity-properties"></a>

`DesiredInstances`  <a name="cfn-appstream-fleet-computecapacity-desiredinstances"></a>
The desired number of streaming instances.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DesiredSessions`  <a name="cfn-appstream-fleet-computecapacity-desiredsessions"></a>
The desired capacity in terms of number of user sessions, for the multi-session fleet. This is not allowed for single-session fleets.
When you create a fleet, you must set define either the DesiredSessions or DesiredInstances attribute, based on the type of fleet you create. You can’t define both attributes or leave both attributes blank.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
