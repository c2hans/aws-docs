---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationreviewconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationReviewConfiguration
<a name="aws-properties-connect-evaluationform-evaluationreviewconfiguration"></a>

Configuration settings for evaluation reviews.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationreviewconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationreviewconfiguration-syntax.json"></a>

```
{
  "[EligibilityDays](#cfn-connect-evaluationform-evaluationreviewconfiguration-eligibilitydays)" : {{Integer}},
  "[ReviewNotificationRecipients](#cfn-connect-evaluationform-evaluationreviewconfiguration-reviewnotificationrecipients)" : {{[ EvaluationReviewNotificationRecipient, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationreviewconfiguration-syntax.yaml"></a>

```
  [EligibilityDays](#cfn-connect-evaluationform-evaluationreviewconfiguration-eligibilitydays): {{Integer}}
  [ReviewNotificationRecipients](#cfn-connect-evaluationform-evaluationreviewconfiguration-reviewnotificationrecipients): {{
    - EvaluationReviewNotificationRecipient}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationreviewconfiguration-properties"></a>

`EligibilityDays`  <a name="cfn-connect-evaluationform-evaluationreviewconfiguration-eligibilitydays"></a>
Number of days during which a request for review can be submitted for evaluations created from this form.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `90`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReviewNotificationRecipients`  <a name="cfn-connect-evaluationform-evaluationreviewconfiguration-reviewnotificationrecipients"></a>
List of recipients who should be notified when a review is requested.
*Required*: Yes
*Type*: Array of [EvaluationReviewNotificationRecipient](aws-properties-connect-evaluationform-evaluationreviewnotificationrecipient.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
