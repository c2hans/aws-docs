---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-ruletriggereventsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule RuleTriggerEventSource
<a name="aws-properties-connect-rule-ruletriggereventsource"></a>

The name of the event source.

## Syntax
<a name="aws-properties-connect-rule-ruletriggereventsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-ruletriggereventsource-syntax.json"></a>

```
{
  "[EventSourceName](#cfn-connect-rule-ruletriggereventsource-eventsourcename)" : {{String}},
  "[IntegrationAssociationArn](#cfn-connect-rule-ruletriggereventsource-integrationassociationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-rule-ruletriggereventsource-syntax.yaml"></a>

```
  [EventSourceName](#cfn-connect-rule-ruletriggereventsource-eventsourcename): {{String}}
  [IntegrationAssociationArn](#cfn-connect-rule-ruletriggereventsource-integrationassociationarn): {{String}}
```

## Properties
<a name="aws-properties-connect-rule-ruletriggereventsource-properties"></a>

`EventSourceName`  <a name="cfn-connect-rule-ruletriggereventsource-eventsourcename"></a>
The name of the event source.
*Required*: Yes
*Type*: String
*Allowed values*: `OnEmailAnalysisAvailable | OnContactEvaluationSubmit | OnPostCallAnalysisAvailable | OnRealTimeCallAnalysisAvailable | OnRealTimeChatAnalysisAvailable | OnPostChatAnalysisAvailable | OnZendeskTicketCreate | OnZendeskTicketStatusUpdate | OnSalesforceCaseCreate | OnMetricDataUpdate | OnCaseCreate | OnCaseUpdate | OnSlaBreach | OnSchedulePublish | OnScheduleUpdate | OnScheduleTimeOffRequestActivity`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IntegrationAssociationArn`  <a name="cfn-connect-rule-ruletriggereventsource-integrationassociationarn"></a>
 The Amazon Resource Name (ARN) of the integration association. `IntegrationAssociationArn` is required if `TriggerEventSource` is one of the following values: `OnZendeskTicketCreate` \| `OnZendeskTicketStatusUpdate` \| `OnSalesforceCaseCreate`
*Required*: No
*Type*: String
*Pattern*: `^$|arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/integration-association/[-a-zA-Z0-9]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
