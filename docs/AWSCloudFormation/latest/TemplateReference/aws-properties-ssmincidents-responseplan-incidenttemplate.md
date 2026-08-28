---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-responseplan-incidenttemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ResponsePlan IncidentTemplate
<a name="aws-properties-ssmincidents-responseplan-incidenttemplate"></a>

The `IncidentTemplate` property type specifies details used to create an incident when using this response plan.

## Syntax
<a name="aws-properties-ssmincidents-responseplan-incidenttemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-responseplan-incidenttemplate-syntax.json"></a>

```
{
  "[DedupeString](#cfn-ssmincidents-responseplan-incidenttemplate-dedupestring)" : {{String}},
  "[Impact](#cfn-ssmincidents-responseplan-incidenttemplate-impact)" : {{Integer}},
  "[IncidentTags](#cfn-ssmincidents-responseplan-incidenttemplate-incidenttags)" : {{[ Tag, ... ]}},
  "[NotificationTargets](#cfn-ssmincidents-responseplan-incidenttemplate-notificationtargets)" : {{[ NotificationTargetItem, ... ]}},
  "[Summary](#cfn-ssmincidents-responseplan-incidenttemplate-summary)" : {{String}},
  "[Title](#cfn-ssmincidents-responseplan-incidenttemplate-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmincidents-responseplan-incidenttemplate-syntax.yaml"></a>

```
  [DedupeString](#cfn-ssmincidents-responseplan-incidenttemplate-dedupestring): {{
    String}}
  [Impact](#cfn-ssmincidents-responseplan-incidenttemplate-impact): {{Integer}}
  [IncidentTags](#cfn-ssmincidents-responseplan-incidenttemplate-incidenttags): {{
    - Tag}}
  [NotificationTargets](#cfn-ssmincidents-responseplan-incidenttemplate-notificationtargets): {{
    - NotificationTargetItem}}
  [Summary](#cfn-ssmincidents-responseplan-incidenttemplate-summary): {{String}}
  [Title](#cfn-ssmincidents-responseplan-incidenttemplate-title): {{String}}
```

## Properties
<a name="aws-properties-ssmincidents-responseplan-incidenttemplate-properties"></a>

`DedupeString`  <a name="cfn-ssmincidents-responseplan-incidenttemplate-dedupestring"></a>
Used to create only one incident record for an incident.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Impact`  <a name="cfn-ssmincidents-responseplan-incidenttemplate-impact"></a>
Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan.

**Possible impacts:**
+ `1` - Critical impact, this typically relates to full application failure that impacts many to all customers.
+ `2` - High impact, partial application failure with impact to many customers.
+ `3` - Medium impact, the application is providing reduced service to customers.
+ `4` - Low impact, customer might aren't impacted by the problem yet.
+ `5` - No impact, customers aren't currently impacted but urgent action is needed to avoid impact.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncidentTags`  <a name="cfn-ssmincidents-responseplan-incidenttemplate-incidenttags"></a>
Tags to assign to the template. When the `StartIncident` API action is called, Incident Manager assigns the tags specified in the template to the incident.
*Required*: No
*Type*: Array of [Tag](aws-properties-ssmincidents-responseplan-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationTargets`  <a name="cfn-ssmincidents-responseplan-incidenttemplate-notificationtargets"></a>
The Amazon Simple Notification Service (Amazon SNS) targets that Amazon Q Developer in chat applications uses to notify the chat channel of updates to an incident. You can also make updates to the incident through the chat channel using the Amazon SNS topics.
*Required*: No
*Type*: Array of [NotificationTargetItem](aws-properties-ssmincidents-responseplan-notificationtargetitem.md)
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Summary`  <a name="cfn-ssmincidents-responseplan-incidenttemplate-summary"></a>
The summary describes what has happened during the incident.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-ssmincidents-responseplan-incidenttemplate-title"></a>
The title of the incident is a brief and easily recognizable.
*Required*: Yes
*Type*: String
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
