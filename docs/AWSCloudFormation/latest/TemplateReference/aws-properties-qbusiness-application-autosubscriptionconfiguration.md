---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-application-autosubscriptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Application AutoSubscriptionConfiguration
<a name="aws-properties-qbusiness-application-autosubscriptionconfiguration"></a>

Subscription configuration information for an Amazon Q Business application using IAM identity federation for user management.

## Syntax
<a name="aws-properties-qbusiness-application-autosubscriptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-application-autosubscriptionconfiguration-syntax.json"></a>

```
{
  "[AutoSubscribe](#cfn-qbusiness-application-autosubscriptionconfiguration-autosubscribe)" : {{String}},
  "[DefaultSubscriptionType](#cfn-qbusiness-application-autosubscriptionconfiguration-defaultsubscriptiontype)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-application-autosubscriptionconfiguration-syntax.yaml"></a>

```
  [AutoSubscribe](#cfn-qbusiness-application-autosubscriptionconfiguration-autosubscribe): {{String}}
  [DefaultSubscriptionType](#cfn-qbusiness-application-autosubscriptionconfiguration-defaultsubscriptiontype): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-application-autosubscriptionconfiguration-properties"></a>

`AutoSubscribe`  <a name="cfn-qbusiness-application-autosubscriptionconfiguration-autosubscribe"></a>
Describes whether automatic subscriptions are enabled for an Amazon Q Business application using IAM identity federation for user management.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultSubscriptionType`  <a name="cfn-qbusiness-application-autosubscriptionconfiguration-defaultsubscriptiontype"></a>
Describes the default subscription type assigned to an Amazon Q Business application using IAM identity federation for user management. If the value for `autoSubscribe` is set to `ENABLED` you must select a value for this field.
*Required*: No
*Type*: String
*Allowed values*: `Q_LITE | Q_BUSINESS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
