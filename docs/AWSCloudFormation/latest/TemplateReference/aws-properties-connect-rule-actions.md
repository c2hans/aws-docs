---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-actions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule Actions
<a name="aws-properties-connect-rule-actions"></a>

 A list of actions to be run when the rule is triggered.

## Syntax
<a name="aws-properties-connect-rule-actions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-actions-syntax.json"></a>

```
{
  "[AssignContactCategoryActions](#cfn-connect-rule-actions-assigncontactcategoryactions)" : {{[ Json, ... ]}},
  "[AssignSlaActions](#cfn-connect-rule-actions-assignslaactions)" : {{[ AssignSlaAction, ... ]}},
  "[CreateCaseActions](#cfn-connect-rule-actions-createcaseactions)" : {{[ CreateCaseAction, ... ]}},
  "[EndAssociatedTasksActions](#cfn-connect-rule-actions-endassociatedtasksactions)" : {{[ Json, ... ]}},
  "[EventBridgeActions](#cfn-connect-rule-actions-eventbridgeactions)" : {{[ EventBridgeAction, ... ]}},
  "[SendNotificationActions](#cfn-connect-rule-actions-sendnotificationactions)" : {{[ SendNotificationAction, ... ]}},
  "[SubmitAutoEvaluationActions](#cfn-connect-rule-actions-submitautoevaluationactions)" : {{[ SubmitAutoEvaluationAction, ... ]}},
  "[TaskActions](#cfn-connect-rule-actions-taskactions)" : {{[ TaskAction, ... ]}},
  "[UpdateCaseActions](#cfn-connect-rule-actions-updatecaseactions)" : {{[ UpdateCaseAction, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-rule-actions-syntax.yaml"></a>

```
  [AssignContactCategoryActions](#cfn-connect-rule-actions-assigncontactcategoryactions): {{
    - Json}}
  [AssignSlaActions](#cfn-connect-rule-actions-assignslaactions): {{
    - AssignSlaAction}}
  [CreateCaseActions](#cfn-connect-rule-actions-createcaseactions): {{
    - CreateCaseAction}}
  [EndAssociatedTasksActions](#cfn-connect-rule-actions-endassociatedtasksactions): {{
    - Json}}
  [EventBridgeActions](#cfn-connect-rule-actions-eventbridgeactions): {{
    - EventBridgeAction}}
  [SendNotificationActions](#cfn-connect-rule-actions-sendnotificationactions): {{
    - SendNotificationAction}}
  [SubmitAutoEvaluationActions](#cfn-connect-rule-actions-submitautoevaluationactions): {{
    - SubmitAutoEvaluationAction}}
  [TaskActions](#cfn-connect-rule-actions-taskactions): {{
    - TaskAction}}
  [UpdateCaseActions](#cfn-connect-rule-actions-updatecaseactions): {{
    - UpdateCaseAction}}
```

## Properties
<a name="aws-properties-connect-rule-actions-properties"></a>

`AssignContactCategoryActions`  <a name="cfn-connect-rule-actions-assigncontactcategoryactions"></a>
Information about the contact category action. The syntax can be empty, for example, `{}`.
*Required*: No
*Type*: Array of Json
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssignSlaActions`  <a name="cfn-connect-rule-actions-assignslaactions"></a>
Property description not available.
*Required*: No
*Type*: Array of [AssignSlaAction](aws-properties-connect-rule-assignslaaction.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateCaseActions`  <a name="cfn-connect-rule-actions-createcaseactions"></a>
Property description not available.
*Required*: No
*Type*: Array of [CreateCaseAction](aws-properties-connect-rule-createcaseaction.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndAssociatedTasksActions`  <a name="cfn-connect-rule-actions-endassociatedtasksactions"></a>
Property description not available.
*Required*: No
*Type*: Array of Json
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventBridgeActions`  <a name="cfn-connect-rule-actions-eventbridgeactions"></a>
Information about the EventBridge action.
*Required*: No
*Type*: Array of [EventBridgeAction](aws-properties-connect-rule-eventbridgeaction.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SendNotificationActions`  <a name="cfn-connect-rule-actions-sendnotificationactions"></a>
Information about the send notification action.
*Required*: No
*Type*: Array of [SendNotificationAction](aws-properties-connect-rule-sendnotificationaction.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubmitAutoEvaluationActions`  <a name="cfn-connect-rule-actions-submitautoevaluationactions"></a>
Property description not available.
*Required*: No
*Type*: Array of [SubmitAutoEvaluationAction](aws-properties-connect-rule-submitautoevaluationaction.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskActions`  <a name="cfn-connect-rule-actions-taskactions"></a>
Information about the task action. This field is required if `TriggerEventSource` is one of the following values: `OnZendeskTicketCreate` \| `OnZendeskTicketStatusUpdate` \| `OnSalesforceCaseCreate`
*Required*: No
*Type*: Array of [TaskAction](aws-properties-connect-rule-taskaction.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateCaseActions`  <a name="cfn-connect-rule-actions-updatecaseactions"></a>
Property description not available.
*Required*: No
*Type*: Array of [UpdateCaseAction](aws-properties-connect-rule-updatecaseaction.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
