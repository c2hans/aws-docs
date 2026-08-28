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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
