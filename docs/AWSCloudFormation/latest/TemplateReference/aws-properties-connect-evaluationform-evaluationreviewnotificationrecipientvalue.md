---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationreviewnotificationrecipientvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationReviewNotificationRecipientValue
<a name="aws-properties-connect-evaluationform-evaluationreviewnotificationrecipientvalue"></a>

The value information for an evaluation review notification recipient.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationreviewnotificationrecipientvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationreviewnotificationrecipientvalue-syntax.json"></a>

```
{
  "[UserId](#cfn-connect-evaluationform-evaluationreviewnotificationrecipientvalue-userid)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationreviewnotificationrecipientvalue-syntax.yaml"></a>

```
  [UserId](#cfn-connect-evaluationform-evaluationreviewnotificationrecipientvalue-userid): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationreviewnotificationrecipientvalue-properties"></a>

`UserId`  <a name="cfn-connect-evaluationform-evaluationreviewnotificationrecipientvalue-userid"></a>
The user identifier for the notification recipient.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
