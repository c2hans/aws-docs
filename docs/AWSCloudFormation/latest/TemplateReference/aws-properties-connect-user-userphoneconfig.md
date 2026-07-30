---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-user-userphoneconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::User UserPhoneConfig
<a name="aws-properties-connect-user-userphoneconfig"></a>

Contains information about the phone configuration settings for a user.

## Syntax
<a name="aws-properties-connect-user-userphoneconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-user-userphoneconfig-syntax.json"></a>

```
{
  "[AfterContactWorkTimeLimit](#cfn-connect-user-userphoneconfig-aftercontactworktimelimit)" : {{Integer}},
  "[AutoAccept](#cfn-connect-user-userphoneconfig-autoaccept)" : {{Boolean}},
  "[DeskPhoneNumber](#cfn-connect-user-userphoneconfig-deskphonenumber)" : {{String}},
  "[PersistentConnection](#cfn-connect-user-userphoneconfig-persistentconnection)" : {{Boolean}},
  "[PhoneType](#cfn-connect-user-userphoneconfig-phonetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-user-userphoneconfig-syntax.yaml"></a>

```
  [AfterContactWorkTimeLimit](#cfn-connect-user-userphoneconfig-aftercontactworktimelimit): {{Integer}}
  [AutoAccept](#cfn-connect-user-userphoneconfig-autoaccept): {{Boolean}}
  [DeskPhoneNumber](#cfn-connect-user-userphoneconfig-deskphonenumber): {{String}}
  [PersistentConnection](#cfn-connect-user-userphoneconfig-persistentconnection): {{Boolean}}
  [PhoneType](#cfn-connect-user-userphoneconfig-phonetype): {{String}}
```

## Properties
<a name="aws-properties-connect-user-userphoneconfig-properties"></a>

`AfterContactWorkTimeLimit`  <a name="cfn-connect-user-userphoneconfig-aftercontactworktimelimit"></a>
The After Call Work (ACW) timeout setting, in seconds. This parameter has a minimum value of 0 and a maximum value of 2,000,000 seconds (24 days). Enter 0 if you don't want to allocate a specific amount of ACW time. It essentially means an indefinite amount of time. When the conversation ends, ACW starts; the agent must choose Close contact to end ACW.
When returned by a `SearchUsers` call, `AfterContactWorkTimeLimit` is returned in milliseconds.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoAccept`  <a name="cfn-connect-user-userphoneconfig-autoaccept"></a>
The Auto accept setting.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeskPhoneNumber`  <a name="cfn-connect-user-userphoneconfig-deskphonenumber"></a>
The phone number for the user's desk phone.
*Required*: No
*Type*: String
*Pattern*: `\+[1-9]\d{1,14}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PersistentConnection`  <a name="cfn-connect-user-userphoneconfig-persistentconnection"></a>
The persistent connection setting for the user.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhoneType`  <a name="cfn-connect-user-userphoneconfig-phonetype"></a>
The phone type.
*Required*: No
*Type*: String
*Allowed values*: `SOFT_PHONE | DESK_PHONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
