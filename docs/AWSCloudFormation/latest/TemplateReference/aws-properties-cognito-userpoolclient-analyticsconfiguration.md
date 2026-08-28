---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolclient-analyticsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolClient AnalyticsConfiguration
<a name="aws-properties-cognito-userpoolclient-analyticsconfiguration"></a>

The settings for Amazon Pinpoint analytics configuration. With an analytics configuration, your application can collect user-activity metrics for user notifications with a Amazon Pinpoint campaign.

Amazon Pinpoint isn't available in all AWS Regions. For a list of available Regions, see [Amazon Cognito and Amazon Pinpoint Region availability](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-pinpoint-integration.html#cognito-user-pools-find-region-mappings).

## Syntax
<a name="aws-properties-cognito-userpoolclient-analyticsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolclient-analyticsconfiguration-syntax.json"></a>

```
{
  "[ApplicationArn](#cfn-cognito-userpoolclient-analyticsconfiguration-applicationarn)" : {{String}},
  "[ApplicationId](#cfn-cognito-userpoolclient-analyticsconfiguration-applicationid)" : {{String}},
  "[ExternalId](#cfn-cognito-userpoolclient-analyticsconfiguration-externalid)" : {{String}},
  "[RoleArn](#cfn-cognito-userpoolclient-analyticsconfiguration-rolearn)" : {{String}},
  "[UserDataShared](#cfn-cognito-userpoolclient-analyticsconfiguration-userdatashared)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolclient-analyticsconfiguration-syntax.yaml"></a>

```
  [ApplicationArn](#cfn-cognito-userpoolclient-analyticsconfiguration-applicationarn): {{String}}
  [ApplicationId](#cfn-cognito-userpoolclient-analyticsconfiguration-applicationid): {{String}}
  [ExternalId](#cfn-cognito-userpoolclient-analyticsconfiguration-externalid): {{String}}
  [RoleArn](#cfn-cognito-userpoolclient-analyticsconfiguration-rolearn): {{String}}
  [UserDataShared](#cfn-cognito-userpoolclient-analyticsconfiguration-userdatashared): {{Boolean}}
```

## Properties
<a name="aws-properties-cognito-userpoolclient-analyticsconfiguration-properties"></a>

`ApplicationArn`  <a name="cfn-cognito-userpoolclient-analyticsconfiguration-applicationarn"></a>
The Amazon Resource Name (ARN) of an Amazon Pinpoint project that you want to connect to your user pool app client. Amazon Cognito publishes events to the Amazon Pinpoint project that `ApplicationArn` declares. You can also configure your application to pass an endpoint ID in the `AnalyticsMetadata` parameter of sign-in operations. The endpoint ID is information about the destination for push notifications
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationId`  <a name="cfn-cognito-userpoolclient-analyticsconfiguration-applicationid"></a>
Your Amazon Pinpoint project ID.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-fA-F]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-cognito-userpoolclient-analyticsconfiguration-externalid"></a>
The [external ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) of the role that Amazon Cognito assumes to send analytics data to Amazon Pinpoint.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-cognito-userpoolclient-analyticsconfiguration-rolearn"></a>
The ARN of an AWS Identity and Access Management role that has the permissions required for Amazon Cognito to publish events to Amazon Pinpoint analytics.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserDataShared`  <a name="cfn-cognito-userpoolclient-analyticsconfiguration-userdatashared"></a>
If `UserDataShared` is `true`, Amazon Cognito includes user data in the events that it publishes to Amazon Pinpoint analytics.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
