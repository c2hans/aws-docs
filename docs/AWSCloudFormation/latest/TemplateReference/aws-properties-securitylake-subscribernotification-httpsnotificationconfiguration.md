---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-subscribernotification-httpsnotificationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::SubscriberNotification HttpsNotificationConfiguration
<a name="aws-properties-securitylake-subscribernotification-httpsnotificationconfiguration"></a>

Specify the configurations you want to use for HTTPS subscriber notification.

## Syntax
<a name="aws-properties-securitylake-subscribernotification-httpsnotificationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-subscribernotification-httpsnotificationconfiguration-syntax.json"></a>

```
{
  "[AuthorizationApiKeyName](#cfn-securitylake-subscribernotification-httpsnotificationconfiguration-authorizationapikeyname)" : {{String}},
  "[AuthorizationApiKeyValue](#cfn-securitylake-subscribernotification-httpsnotificationconfiguration-authorizationapikeyvalue)" : {{String}},
  "[Endpoint](#cfn-securitylake-subscribernotification-httpsnotificationconfiguration-endpoint)" : {{String}},
  "[HttpMethod](#cfn-securitylake-subscribernotification-httpsnotificationconfiguration-httpmethod)" : {{String}},
  "[TargetRoleArn](#cfn-securitylake-subscribernotification-httpsnotificationconfiguration-targetrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-securitylake-subscribernotification-httpsnotificationconfiguration-syntax.yaml"></a>

```
  [AuthorizationApiKeyName](#cfn-securitylake-subscribernotification-httpsnotificationconfiguration-authorizationapikeyname): {{String}}
  [AuthorizationApiKeyValue](#cfn-securitylake-subscribernotification-httpsnotificationconfiguration-authorizationapikeyvalue): {{String}}
  [Endpoint](#cfn-securitylake-subscribernotification-httpsnotificationconfiguration-endpoint): {{String}}
  [HttpMethod](#cfn-securitylake-subscribernotification-httpsnotificationconfiguration-httpmethod): {{String}}
  [TargetRoleArn](#cfn-securitylake-subscribernotification-httpsnotificationconfiguration-targetrolearn): {{String}}
```

## Properties
<a name="aws-properties-securitylake-subscribernotification-httpsnotificationconfiguration-properties"></a>

`AuthorizationApiKeyName`  <a name="cfn-securitylake-subscribernotification-httpsnotificationconfiguration-authorizationapikeyname"></a>
The key name for the notification subscription.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationApiKeyValue`  <a name="cfn-securitylake-subscribernotification-httpsnotificationconfiguration-authorizationapikeyvalue"></a>
The key value for the notification subscription.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-securitylake-subscribernotification-httpsnotificationconfiguration-endpoint"></a>
The subscription endpoint in Security Lake. If you prefer notification with an HTTPS endpoint, populate this field.
*Required*: Yes
*Type*: String
*Pattern*: `^https?://.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpMethod`  <a name="cfn-securitylake-subscribernotification-httpsnotificationconfiguration-httpmethod"></a>
The HTTPS method used for the notification subscription.
*Required*: No
*Type*: String
*Allowed values*: `POST | PUT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRoleArn`  <a name="cfn-securitylake-subscribernotification-httpsnotificationconfiguration-targetrolearn"></a>
The Amazon Resource Name (ARN) of the EventBridge API destinations IAM role that you created. For more information about ARNs and how to use them in policies, see [Managing data access](https://docs.aws.amazon.com//security-lake/latest/userguide/subscriber-data-access.html) and [AWS Managed Policies](https://docs.aws.amazon.com/security-lake/latest/userguide/security-iam-awsmanpol.html) in the *Amazon Security Lake User Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
