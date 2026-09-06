---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehub-app-eventsubscription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHub::App EventSubscription
<a name="aws-properties-resiliencehub-app-eventsubscription"></a>

Indicates an event you would like to subscribe and get notification for. Currently, AWS Resilience Hub supports notifications only for **Drift detected** and **Scheduled assessment failure** events.

## Syntax
<a name="aws-properties-resiliencehub-app-eventsubscription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehub-app-eventsubscription-syntax.json"></a>

```
{
  "[EventType](#cfn-resiliencehub-app-eventsubscription-eventtype)" : {{String}},
  "[Name](#cfn-resiliencehub-app-eventsubscription-name)" : {{String}},
  "[SnsTopicArn](#cfn-resiliencehub-app-eventsubscription-snstopicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-resiliencehub-app-eventsubscription-syntax.yaml"></a>

```
  [EventType](#cfn-resiliencehub-app-eventsubscription-eventtype): {{String}}
  [Name](#cfn-resiliencehub-app-eventsubscription-name): {{String}}
  [SnsTopicArn](#cfn-resiliencehub-app-eventsubscription-snstopicarn): {{String}}
```

## Properties
<a name="aws-properties-resiliencehub-app-eventsubscription-properties"></a>

`EventType`  <a name="cfn-resiliencehub-app-eventsubscription-eventtype"></a>
The type of event you would like to subscribe and get notification for. Currently, AWS Resilience Hub supports notifications only for **Drift detected** (`DriftDetected`) and **Scheduled assessment failure** (`ScheduledAssessmentFailure`) events.
*Required*: Yes
*Type*: String
*Allowed values*: `ScheduledAssessmentFailure | DriftDetected`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-resiliencehub-app-eventsubscription-name"></a>
Unique name to identify an event subscription.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsTopicArn`  <a name="cfn-resiliencehub-app-eventsubscription-snstopicarn"></a>
Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic. The format for this ARN is: `arn:partition:sns:region:account:topic-name`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference* guide.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
