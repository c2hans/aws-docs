---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-user.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::User
<a name="aws-resource-connect-user"></a>

Specifies a user account for an Connect Customer instance.

For information about how to create user accounts using the Connect Customer console, see [Add Users](https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html) in the *Connect Customer Administrator Guide*.

## Syntax
<a name="aws-resource-connect-user-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-user-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::User",
  "Properties" : {
      "[AfterContactWorkConfigs](#cfn-connect-user-aftercontactworkconfigs)" : {{[ AfterContactWorkConfigPerChannel, ... ]}},
      "[AutoAcceptConfigs](#cfn-connect-user-autoacceptconfigs)" : {{[ AutoAcceptConfig, ... ]}},
      "[DirectoryUserId](#cfn-connect-user-directoryuserid)" : {{String}},
      "[HierarchyGroupArn](#cfn-connect-user-hierarchygrouparn)" : {{String}},
      "[IdentityInfo](#cfn-connect-user-identityinfo)" : {{UserIdentityInfo}},
      "[InstanceArn](#cfn-connect-user-instancearn)" : {{String}},
      "[Password](#cfn-connect-user-password)" : {{String}},
      "[PersistentConnectionConfigs](#cfn-connect-user-persistentconnectionconfigs)" : {{[ PersistentConnectionConfig, ... ]}},
      "[PhoneConfig](#cfn-connect-user-phoneconfig)" : {{UserPhoneConfig}},
      "[PhoneNumberConfigs](#cfn-connect-user-phonenumberconfigs)" : {{[ PhoneNumberConfig, ... ]}},
      "[RoutingProfileArn](#cfn-connect-user-routingprofilearn)" : {{String}},
      "[SecurityProfileArns](#cfn-connect-user-securityprofilearns)" : {{[ String, ... ]}},
      "[Tags](#cfn-connect-user-tags)" : {{[ Tag, ... ]}},
      "[Username](#cfn-connect-user-username)" : {{String}},
      "[UserProficiencies](#cfn-connect-user-userproficiencies)" : {{[ UserProficiency, ... ]}},
      "[VoiceEnhancementConfigs](#cfn-connect-user-voiceenhancementconfigs)" : {{[ VoiceEnhancementConfig, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-connect-user-syntax.yaml"></a>

```
Type: AWS::Connect::User
Properties:
  [AfterContactWorkConfigs](#cfn-connect-user-aftercontactworkconfigs): {{
    - AfterContactWorkConfigPerChannel}}
  [AutoAcceptConfigs](#cfn-connect-user-autoacceptconfigs): {{
    - AutoAcceptConfig}}
  [DirectoryUserId](#cfn-connect-user-directoryuserid): {{String}}
  [HierarchyGroupArn](#cfn-connect-user-hierarchygrouparn): {{String}}
  [IdentityInfo](#cfn-connect-user-identityinfo): {{
    UserIdentityInfo}}
  [InstanceArn](#cfn-connect-user-instancearn): {{String}}
  [Password](#cfn-connect-user-password): {{String}}
  [PersistentConnectionConfigs](#cfn-connect-user-persistentconnectionconfigs): {{
    - PersistentConnectionConfig}}
  [PhoneConfig](#cfn-connect-user-phoneconfig): {{
    UserPhoneConfig}}
  [PhoneNumberConfigs](#cfn-connect-user-phonenumberconfigs): {{
    - PhoneNumberConfig}}
  [RoutingProfileArn](#cfn-connect-user-routingprofilearn): {{String}}
  [SecurityProfileArns](#cfn-connect-user-securityprofilearns): {{
    - String}}
  [Tags](#cfn-connect-user-tags): {{
    - Tag}}
  [Username](#cfn-connect-user-username): {{String}}
  [UserProficiencies](#cfn-connect-user-userproficiencies): {{
    - UserProficiency}}
  [VoiceEnhancementConfigs](#cfn-connect-user-voiceenhancementconfigs): {{
    - VoiceEnhancementConfig}}
```

## Properties
<a name="aws-resource-connect-user-properties"></a>

`AfterContactWorkConfigs`  <a name="cfn-connect-user-aftercontactworkconfigs"></a>
The list of after contact work (ACW) timeout configuration settings for each channel.
*Required*: No
*Type*: Array of [AfterContactWorkConfigPerChannel](aws-properties-connect-user-aftercontactworkconfigperchannel.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoAcceptConfigs`  <a name="cfn-connect-user-autoacceptconfigs"></a>
The list of auto-accept configuration settings for each channel.
*Required*: No
*Type*: Array of [AutoAcceptConfig](aws-properties-connect-user-autoacceptconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DirectoryUserId`  <a name="cfn-connect-user-directoryuserid"></a>
The identifier of the user account in the directory used for identity management.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HierarchyGroupArn`  <a name="cfn-connect-user-hierarchygrouparn"></a>
The Amazon Resource Name (ARN) of the user's hierarchy group.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/agent-group/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityInfo`  <a name="cfn-connect-user-identityinfo"></a>
Information about the user identity.
*Required*: No
*Type*: [UserIdentityInfo](aws-properties-connect-user-useridentityinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-user-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Password`  <a name="cfn-connect-user-password"></a>
The user's password.
*Required*: No
*Type*: String
*Pattern*: `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\S]{8,64}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PersistentConnectionConfigs`  <a name="cfn-connect-user-persistentconnectionconfigs"></a>
The list of persistent connection configuration settings for each channel.
*Required*: No
*Type*: Array of [PersistentConnectionConfig](aws-properties-connect-user-persistentconnectionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhoneConfig`  <a name="cfn-connect-user-phoneconfig"></a>
Information about the phone configuration for the user.
*Required*: No
*Type*: [UserPhoneConfig](aws-properties-connect-user-userphoneconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhoneNumberConfigs`  <a name="cfn-connect-user-phonenumberconfigs"></a>
The list of phone number configuration settings for each channel.
*Required*: No
*Type*: Array of [PhoneNumberConfig](aws-properties-connect-user-phonenumberconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoutingProfileArn`  <a name="cfn-connect-user-routingprofilearn"></a>
The Amazon Resource Name (ARN) of the user's routing profile.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/routing-profile/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityProfileArns`  <a name="cfn-connect-user-securityprofilearns"></a>
The Amazon Resource Name (ARN) of the user's security profile.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-user-tags"></a>
The tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-user-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-connect-user-username"></a>
The user name assigned to the user account.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9\_\-\.\@]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserProficiencies`  <a name="cfn-connect-user-userproficiencies"></a>
One or more predefined attributes assigned to a user, with a numeric value that indicates how their level of skill in a specified area.
*Required*: No
*Type*: Array of [UserProficiency](aws-properties-connect-user-userproficiency.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VoiceEnhancementConfigs`  <a name="cfn-connect-user-voiceenhancementconfigs"></a>
The list of voice enhancement configuration settings for each channel.
*Required*: No
*Type*: Array of [VoiceEnhancementConfig](aws-properties-connect-user-voiceenhancementconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-user-return-values"></a>

### Ref
<a name="aws-resource-connect-user-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the user. For example:

 `{ "Ref": "myUser" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-user-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-user-return-values-fn--getatt-fn--getatt"></a>

`UserArn`  <a name="UserArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the user.

## Examples
<a name="aws-resource-connect-user--examples"></a>

### Specify a user resource
<a name="aws-resource-connect-user--examples--Specify_a_user_resource"></a>

The following example specifies a user resource for an Connect Customer instance. This example specifies a user under an Connect Customer instance. We recommend using a [dynamic reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/security-best-practices.html#creds) to specify a password value or mask the parameter with `NoEcho`.

#### YAML
<a name="aws-resource-connect-user--examples--Specify_a_user_resource--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Specifies a user for an Connect Customer instance
Resources:
    User:
      Type: 'AWS::Connect::User'
      Properties:
        IdentityInfo:
          FirstName: 'firstname'
          LastName: 'lastname'
          Email: 'example@email.com'
        PhoneConfig:
          PhoneType: 'DESK_PHONE'
          AutoAccept: true
          DeskPhoneNumber: '+12345678902'
          AfterContactWorkTimeLimit: 10
        Username: 'exampleuser'
        InstanceArn: 'arn:aws:connect:region-name:aws-account-id:instance/instance-arn'
        RoutingProfileArn: 'arn:aws:connect:region-name:aws-account-id:instance/instance-arn/routing-profile/routing-arn'
        SecurityProfileArns: [arn:aws:connect:region-name:aws-account-id:instance/instance-arn/security-profile/security-arn]
        Password: !Ref password
        Tags:
          - Key: 'tagKey'
            Value: 'tagValue'
```
