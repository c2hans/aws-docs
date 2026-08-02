---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-chatbot-microsoftteamschannelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Chatbot::MicrosoftTeamsChannelConfiguration
<a name="aws-resource-chatbot-microsoftteamschannelconfiguration"></a>

**Note**
AWS Chatbot is now Amazon Q Developer. [Learn more](https://docs.aws.amazon.com//chatbot/latest/adminguide/service-rename.html)
`Type` attribute values remain unchanged.

The `AWS::Chatbot::MicrosoftTeamsChannelConfiguration` resource configures a Microsoft Teams channel to allow users to use Amazon Q Developer with CloudFormation templates.

This resource requires some setup to be done in the Amazon Q Developer in chat applications console. To provide the required Microsoft Teams team and tenant IDs, you must perform the initial authorization flow with Microsoft Teams in the Amazon Q Developer in chat applications console, then copy and paste the IDs from the console. For more details, see steps 1-3 in [Get started with Microsoft Teams](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup) in the *Amazon Q Developer in chat applications Administrator Guide*.

## Syntax
<a name="aws-resource-chatbot-microsoftteamschannelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-chatbot-microsoftteamschannelconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::Chatbot::MicrosoftTeamsChannelConfiguration",
  "Properties" : {
      "[ConfigurationName](#cfn-chatbot-microsoftteamschannelconfiguration-configurationname)" : {{String}},
      "[CustomizationResourceArns](#cfn-chatbot-microsoftteamschannelconfiguration-customizationresourcearns)" : {{[ String, ... ]}},
      "[GuardrailPolicies](#cfn-chatbot-microsoftteamschannelconfiguration-guardrailpolicies)" : {{[ String, ... ]}},
      "[IamRoleArn](#cfn-chatbot-microsoftteamschannelconfiguration-iamrolearn)" : {{String}},
      "[LoggingLevel](#cfn-chatbot-microsoftteamschannelconfiguration-logginglevel)" : {{String}},
      "[SnsTopicArns](#cfn-chatbot-microsoftteamschannelconfiguration-snstopicarns)" : {{[ String, ... ]}},
      "[Tags](#cfn-chatbot-microsoftteamschannelconfiguration-tags)" : {{[ Tag, ... ]}},
      "[TeamId](#cfn-chatbot-microsoftteamschannelconfiguration-teamid)" : {{String}},
      "[TeamsChannelId](#cfn-chatbot-microsoftteamschannelconfiguration-teamschannelid)" : {{String}},
      "[TeamsChannelName](#cfn-chatbot-microsoftteamschannelconfiguration-teamschannelname)" : {{String}},
      "[TeamsTenantId](#cfn-chatbot-microsoftteamschannelconfiguration-teamstenantid)" : {{String}},
      "[UserRoleRequired](#cfn-chatbot-microsoftteamschannelconfiguration-userrolerequired)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-chatbot-microsoftteamschannelconfiguration-syntax.yaml"></a>

```
Type: AWS::Chatbot::MicrosoftTeamsChannelConfiguration
Properties:
  [ConfigurationName](#cfn-chatbot-microsoftteamschannelconfiguration-configurationname): {{String}}
  [CustomizationResourceArns](#cfn-chatbot-microsoftteamschannelconfiguration-customizationresourcearns): {{
    - String}}
  [GuardrailPolicies](#cfn-chatbot-microsoftteamschannelconfiguration-guardrailpolicies): {{
    - String}}
  [IamRoleArn](#cfn-chatbot-microsoftteamschannelconfiguration-iamrolearn): {{String}}
  [LoggingLevel](#cfn-chatbot-microsoftteamschannelconfiguration-logginglevel): {{String}}
  [SnsTopicArns](#cfn-chatbot-microsoftteamschannelconfiguration-snstopicarns): {{
    - String}}
  [Tags](#cfn-chatbot-microsoftteamschannelconfiguration-tags): {{
    - Tag}}
  [TeamId](#cfn-chatbot-microsoftteamschannelconfiguration-teamid): {{String}}
  [TeamsChannelId](#cfn-chatbot-microsoftteamschannelconfiguration-teamschannelid): {{String}}
  [TeamsChannelName](#cfn-chatbot-microsoftteamschannelconfiguration-teamschannelname): {{String}}
  [TeamsTenantId](#cfn-chatbot-microsoftteamschannelconfiguration-teamstenantid): {{String}}
  [UserRoleRequired](#cfn-chatbot-microsoftteamschannelconfiguration-userrolerequired): {{Boolean}}
```

## Properties
<a name="aws-resource-chatbot-microsoftteamschannelconfiguration-properties"></a>

`ConfigurationName`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-configurationname"></a>
The name of the configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomizationResourceArns`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-customizationresourcearns"></a>
Links a list of resource ARNs (for example, custom action ARNs) to a Microsoft Teams channel configuration for Amazon Q Developer.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GuardrailPolicies`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-guardrailpolicies"></a>
The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamRoleArn`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-iamrolearn"></a>
The ARN of the IAM role that defines the permissions for Amazon Q Developer.
This is a user-defined role that Amazon Q Developer will assume. This is not the service-linked role. For more information, see [IAM Policies for Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoggingLevel`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-logginglevel"></a>
Specifies the logging level for this configuration. This property affects the log entries pushed to Amazon CloudWatch Logs.
Logging levels include `ERROR`, `INFO`, or `NONE`.
*Required*: No
*Type*: String
*Pattern*: `^(ERROR|INFO|NONE)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsTopicArns`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-snstopicarns"></a>
The ARNs of the SNS topics that deliver notifications to Amazon Q Developer.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-tags"></a>
The tags to add to the configuration.
*Required*: No
*Type*: Array of [Tag](aws-properties-chatbot-microsoftteamschannelconfiguration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TeamId`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-teamid"></a>
The ID of the Microsoft Team authorized with Amazon Q Developer.
To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the Amazon Q Developer in chat applications console. Then you can copy and paste the team ID from the console. For more details, see steps 1-3 in [Tutorial: Get started with Microsoft Teams ](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html) in the *Amazon Q Developer in chat applications Administrator Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TeamsChannelId`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-teamschannelid"></a>
The ID of the Microsoft Teams channel.
To get the channel ID, open Microsoft Teams, right click on the channel name in the left pane, then choose **Copy**. An example of the channel ID syntax is: `19%3ab6ef35dc342d56ba5654e6fc6d25a071%40thread.tacv2`.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9-_=+/.,])*%3[aA]([a-zA-Z0-9-_=+/.,])*%40([a-zA-Z0-9-_=+/.,])*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TeamsChannelName`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-teamschannelname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(.*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TeamsTenantId`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-teamstenantid"></a>
The ID of the Microsoft Teams tenant.
To get the tenant ID, you must perform the initial authorization flow with Microsoft Teams in the Amazon Q Developer in chat applications console. Then you can copy and paste the tenant ID from the console. For more details, see steps 1-3 in [Tutorial: Get started with Microsoft Teams ](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html) in the *Amazon Q Developer in chat applications Administrator Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserRoleRequired`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-userrolerequired"></a>
Enables use of a user role requirement in your chat configuration.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-chatbot-microsoftteamschannelconfiguration-return-values"></a>

### Ref
<a name="aws-resource-chatbot-microsoftteamschannelconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the ARN of the configuration created.

### Fn::GetAtt
<a name="aws-resource-chatbot-microsoftteamschannelconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-chatbot-microsoftteamschannelconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the resource.

## Remarks
<a name="aws-resource-chatbot-microsoftteamschannelconfiguration--remarks"></a>

Common troubleshooting scenarios:
+  *I don't have a teams, tenant, or channel ID.*

  If you don't have one or any of the aforementioned IDs, you must perform the initial authorization flow in the Amazon Q Developer in chat applications console. Then you will be able to copy and paste the IDs from the console. For more details, see steps 1-3 in [Tutorial: Get started with Microsoft Teams](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup) in the *Amazon Q Developer in chat applications Administrator Guide*.
+  *I have already done the initial authorization for my workspace. Do I need to do it again?*

  No, you can use your existing workspace. You must log into the Amazon Q Developer in chat applications console to get the workspace ID.
