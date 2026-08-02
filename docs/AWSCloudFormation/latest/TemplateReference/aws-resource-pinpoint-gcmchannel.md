---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pinpoint-gcmchannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::GCMChannel
<a name="aws-resource-pinpoint-gcmchannel"></a>

A *channel* is a type of platform that you can deliver messages to. You can use the GCM channel to send push notification messages to the Firebase Cloud Messaging (FCM) service, which replaced the Google Cloud Messaging (GCM) service. Before you use Amazon Pinpoint to send notifications to FCM, you have to enable the GCM channel for an Amazon Pinpoint application.

The GCMChannel resource represents the status and authentication settings of the GCM channel for an application.

## Syntax
<a name="aws-resource-pinpoint-gcmchannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pinpoint-gcmchannel-syntax.json"></a>

```
{
  "Type" : "AWS::Pinpoint::GCMChannel",
  "Properties" : {
      "[ApiKey](#cfn-pinpoint-gcmchannel-apikey)" : {{String}},
      "[ApplicationId](#cfn-pinpoint-gcmchannel-applicationid)" : {{String}},
      "[DefaultAuthenticationMethod](#cfn-pinpoint-gcmchannel-defaultauthenticationmethod)" : {{String}},
      "[Enabled](#cfn-pinpoint-gcmchannel-enabled)" : {{Boolean}},
      "[ServiceJson](#cfn-pinpoint-gcmchannel-servicejson)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-pinpoint-gcmchannel-syntax.yaml"></a>

```
Type: AWS::Pinpoint::GCMChannel
Properties:
  [ApiKey](#cfn-pinpoint-gcmchannel-apikey): {{String}}
  [ApplicationId](#cfn-pinpoint-gcmchannel-applicationid): {{String}}
  [DefaultAuthenticationMethod](#cfn-pinpoint-gcmchannel-defaultauthenticationmethod): {{String}}
  [Enabled](#cfn-pinpoint-gcmchannel-enabled): {{Boolean}}
  [ServiceJson](#cfn-pinpoint-gcmchannel-servicejson): {{String}}
```

## Properties
<a name="aws-resource-pinpoint-gcmchannel-properties"></a>

`ApiKey`  <a name="cfn-pinpoint-gcmchannel-apikey"></a>
The Web API key, also called the *server key*, that you received from Google to communicate with Google services.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationId`  <a name="cfn-pinpoint-gcmchannel-applicationid"></a>
The unique identifier for the Amazon Pinpoint application that the GCM channel applies to.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultAuthenticationMethod`  <a name="cfn-pinpoint-gcmchannel-defaultauthenticationmethod"></a>
The default authentication method used for GCM. Values are either "TOKEN" or "KEY". Defaults to "KEY".
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-pinpoint-gcmchannel-enabled"></a>
Specifies whether to enable the GCM channel for the Amazon Pinpoint application.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceJson`  <a name="cfn-pinpoint-gcmchannel-servicejson"></a>
The contents of the JSON file provided by Google during registration in order to generate an access token for authentication. For more information see [Migrate from legacy FCM APIs to HTTP v1](https://firebase.google.com/docs/cloud-messaging/migrate-v1).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-pinpoint-gcmchannel-return-values"></a>

### Ref
<a name="aws-resource-pinpoint-gcmchannel-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier (`ApplicationId`) for the Amazon Pinpoint application that the channel is associated with.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-pinpoint-gcmchannel-return-values-fn--getatt"></a>

####
<a name="aws-resource-pinpoint-gcmchannel-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
(Deprecated) An identifier for the GCM channel. This property is retained only for backward compatibility.
