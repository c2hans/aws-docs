---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-notifications-eventrule-eventrulestatussummary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Notifications::EventRule EventRuleStatusSummary
<a name="aws-properties-notifications-eventrule-eventrulestatussummary"></a>

Provides additional information about the current `EventRule` status.

## Syntax
<a name="aws-properties-notifications-eventrule-eventrulestatussummary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-notifications-eventrule-eventrulestatussummary-syntax.json"></a>

```
{
  "[Reason](#cfn-notifications-eventrule-eventrulestatussummary-reason)" : {{String}},
  "[Status](#cfn-notifications-eventrule-eventrulestatussummary-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-notifications-eventrule-eventrulestatussummary-syntax.yaml"></a>

```
  [Reason](#cfn-notifications-eventrule-eventrulestatussummary-reason): {{String}}
  [Status](#cfn-notifications-eventrule-eventrulestatussummary-status): {{String}}
```

## Properties
<a name="aws-properties-notifications-eventrule-eventrulestatussummary-properties"></a>

`Reason`  <a name="cfn-notifications-eventrule-eventrulestatussummary-reason"></a>
A human-readable reason for `EventRuleStatus`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-notifications-eventrule-eventrulestatussummary-status"></a>
The status of the `EventRule`.
+ Values:
  +  `ACTIVE`
    + The `EventRule` can process events.
  +  `INACTIVE`
    + The `EventRule` may be unable to process events.
  +  `CREATING`
    + The `EventRule` is being created.

      Only `GET` and `LIST` calls can be run.
  +  `UPDATING`
    + The `EventRule` is being updated.

      Only `GET` and `LIST` calls can be run.
  +  `DELETING`
    + The `EventRule` is being deleted.

      Only `GET` and `LIST` calls can be run.
*Required*: Yes
*Type*: String
*Allowed values*: `ACTIVE | INACTIVE | CREATING | UPDATING | DELETING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
