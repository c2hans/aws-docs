---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-applicationsettings-campaignhook.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::ApplicationSettings CampaignHook
<a name="aws-properties-pinpoint-applicationsettings-campaignhook"></a>

Specifies the Lambda function to use by default as a code hook for campaigns in the application.

## Syntax
<a name="aws-properties-pinpoint-applicationsettings-campaignhook-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-applicationsettings-campaignhook-syntax.json"></a>

```
{
  "[LambdaFunctionName](#cfn-pinpoint-applicationsettings-campaignhook-lambdafunctionname)" : {{String}},
  "[Mode](#cfn-pinpoint-applicationsettings-campaignhook-mode)" : {{String}},
  "[WebUrl](#cfn-pinpoint-applicationsettings-campaignhook-weburl)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpoint-applicationsettings-campaignhook-syntax.yaml"></a>

```
  [LambdaFunctionName](#cfn-pinpoint-applicationsettings-campaignhook-lambdafunctionname): {{String}}
  [Mode](#cfn-pinpoint-applicationsettings-campaignhook-mode): {{String}}
  [WebUrl](#cfn-pinpoint-applicationsettings-campaignhook-weburl): {{String}}
```

## Properties
<a name="aws-properties-pinpoint-applicationsettings-campaignhook-properties"></a>

`LambdaFunctionName`  <a name="cfn-pinpoint-applicationsettings-campaignhook-lambdafunctionname"></a>
The name or Amazon Resource Name (ARN) of the Lambda function that Amazon Pinpoint invokes to send messages for campaigns in the application.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-pinpoint-applicationsettings-campaignhook-mode"></a>
The mode that Amazon Pinpoint uses to invoke the Lambda function. Possible values are:
+ `FILTER` - Invoke the function to customize the segment that's used by a campaign.
+ `DELIVERY` - (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the `CustomDeliveryConfiguration` and `CampaignCustomMessage` objects of the campaign.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebUrl`  <a name="cfn-pinpoint-applicationsettings-campaignhook-weburl"></a>
The web URL that Amazon Pinpoint calls to invoke the Lambda function over HTTPS.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
