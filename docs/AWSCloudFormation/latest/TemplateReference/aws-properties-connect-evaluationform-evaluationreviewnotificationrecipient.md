---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationreviewnotificationrecipient.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationReviewNotificationRecipient
<a name="aws-properties-connect-evaluationform-evaluationreviewnotificationrecipient"></a>

Information about a recipient who should be notified when an evaluation review is requested.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationreviewnotificationrecipient-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationreviewnotificationrecipient-syntax.json"></a>

```
{
  "[Type](#cfn-connect-evaluationform-evaluationreviewnotificationrecipient-type)" : {{String}},
  "[Value](#cfn-connect-evaluationform-evaluationreviewnotificationrecipient-value)" : {{EvaluationReviewNotificationRecipientValue}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationreviewnotificationrecipient-syntax.yaml"></a>

```
  [Type](#cfn-connect-evaluationform-evaluationreviewnotificationrecipient-type): {{String}}
  [Value](#cfn-connect-evaluationform-evaluationreviewnotificationrecipient-value): {{
    EvaluationReviewNotificationRecipientValue}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationreviewnotificationrecipient-properties"></a>

`Type`  <a name="cfn-connect-evaluationform-evaluationreviewnotificationrecipient-type"></a>
The type of notification recipient.
*Required*: Yes
*Type*: String
*Allowed values*: `USER_ID`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-connect-evaluationform-evaluationreviewnotificationrecipient-value"></a>
The value associated with the notification recipient type.
*Required*: Yes
*Type*: [EvaluationReviewNotificationRecipientValue](aws-properties-connect-evaluationform-evaluationreviewnotificationrecipientvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
