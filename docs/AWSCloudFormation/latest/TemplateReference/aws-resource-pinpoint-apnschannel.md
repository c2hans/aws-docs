---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pinpoint-apnschannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::APNSChannel
<a name="aws-resource-pinpoint-apnschannel"></a>

A *channel* is a type of platform that you can deliver messages to. You can use the APNs channel to send push notification messages to the Apple Push Notification service (APNs). Before you can use Amazon Pinpoint to send notifications to APNs, you have to enable the APNs channel for an Amazon Pinpoint application.

The APNSChannel resource represents the status and authentication settings for the APNs channel for an application.

## Syntax
<a name="aws-resource-pinpoint-apnschannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pinpoint-apnschannel-syntax.json"></a>

```
{
  "Type" : "AWS::Pinpoint::APNSChannel",
  "Properties" : {
      "[ApplicationId](#cfn-pinpoint-apnschannel-applicationid)" : {{String}},
      "[BundleId](#cfn-pinpoint-apnschannel-bundleid)" : {{String}},
      "[Certificate](#cfn-pinpoint-apnschannel-certificate)" : {{String}},
      "[DefaultAuthenticationMethod](#cfn-pinpoint-apnschannel-defaultauthenticationmethod)" : {{String}},
      "[Enabled](#cfn-pinpoint-apnschannel-enabled)" : {{Boolean}},
      "[PrivateKey](#cfn-pinpoint-apnschannel-privatekey)" : {{String}},
      "[TeamId](#cfn-pinpoint-apnschannel-teamid)" : {{String}},
      "[TokenKey](#cfn-pinpoint-apnschannel-tokenkey)" : {{String}},
      "[TokenKeyId](#cfn-pinpoint-apnschannel-tokenkeyid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-pinpoint-apnschannel-syntax.yaml"></a>

```
Type: AWS::Pinpoint::APNSChannel
Properties:
  [ApplicationId](#cfn-pinpoint-apnschannel-applicationid): {{String}}
  [BundleId](#cfn-pinpoint-apnschannel-bundleid): {{String}}
  [Certificate](#cfn-pinpoint-apnschannel-certificate): {{String}}
  [DefaultAuthenticationMethod](#cfn-pinpoint-apnschannel-defaultauthenticationmethod): {{String}}
  [Enabled](#cfn-pinpoint-apnschannel-enabled): {{Boolean}}
  [PrivateKey](#cfn-pinpoint-apnschannel-privatekey): {{String}}
  [TeamId](#cfn-pinpoint-apnschannel-teamid): {{String}}
  [TokenKey](#cfn-pinpoint-apnschannel-tokenkey): {{String}}
  [TokenKeyId](#cfn-pinpoint-apnschannel-tokenkeyid): {{String}}
```

## Properties
<a name="aws-resource-pinpoint-apnschannel-properties"></a>

`ApplicationId`  <a name="cfn-pinpoint-apnschannel-applicationid"></a>
The unique identifier for the Amazon Pinpoint application that the APNs channel applies to.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BundleId`  <a name="cfn-pinpoint-apnschannel-bundleid"></a>
The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Certificate`  <a name="cfn-pinpoint-apnschannel-certificate"></a>
The APNs client certificate that you received from Apple. Specify this value if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultAuthenticationMethod`  <a name="cfn-pinpoint-apnschannel-defaultauthenticationmethod"></a>
The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs. Valid options are `key` or `certificate`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-pinpoint-apnschannel-enabled"></a>
Specifies whether to enable the APNs channel for the application.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateKey`  <a name="cfn-pinpoint-apnschannel-privatekey"></a>
The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TeamId`  <a name="cfn-pinpoint-apnschannel-teamid"></a>
The identifier that's assigned to your Apple Developer Account team. This identifier is used for APNs tokens.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenKey`  <a name="cfn-pinpoint-apnschannel-tokenkey"></a>
The authentication key to use for APNs tokens.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenKeyId`  <a name="cfn-pinpoint-apnschannel-tokenkeyid"></a>
The key identifier that's assigned to your APNs signing key. Specify this value if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-pinpoint-apnschannel-return-values"></a>

### Ref
<a name="aws-resource-pinpoint-apnschannel-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier (`ApplicationId`) for the Amazon Pinpoint application that the channel is associated with.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-pinpoint-apnschannel-return-values-fn--getatt"></a>

####
<a name="aws-resource-pinpoint-apnschannel-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
(Deprecated) An identifier for the APNs channel. This property is retained only for backward compatibility.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
