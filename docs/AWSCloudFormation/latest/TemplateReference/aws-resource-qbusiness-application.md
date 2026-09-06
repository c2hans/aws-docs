---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-qbusiness-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Application
<a name="aws-resource-qbusiness-application"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates an Amazon Q Business application.

**Note**
There are new tiers for Amazon Q Business. Not all features in Amazon Q Business Pro are also available in Amazon Q Business Lite. For information on what's included in Amazon Q Business Lite and what's included in Amazon Q Business Pro, see [Amazon Q Business tiers](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#user-sub-tiers). You must use the Amazon Q Business console to assign subscription tiers to users.
An Amazon Q Apps service linked role will be created if it's absent in the AWS account when `QAppsConfiguration` is enabled in the request. For more information, see [ Using service-linked roles for Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html).
When you create an application, Amazon Q Business may securely transmit data for processing from your selected AWS region, but within your geography. For more information, see [Cross region inference in Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html).

## Syntax
<a name="aws-resource-qbusiness-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-qbusiness-application-syntax.json"></a>

```
{
  "Type" : "AWS::QBusiness::Application",
  "Properties" : {
      "[AttachmentsConfiguration](#cfn-qbusiness-application-attachmentsconfiguration)" : {{AttachmentsConfiguration}},
      "[AutoSubscriptionConfiguration](#cfn-qbusiness-application-autosubscriptionconfiguration)" : {{AutoSubscriptionConfiguration}},
      "[ClientIdsForOIDC](#cfn-qbusiness-application-clientidsforoidc)" : {{[ String, ... ]}},
      "[Description](#cfn-qbusiness-application-description)" : {{String}},
      "[DisplayName](#cfn-qbusiness-application-displayname)" : {{String}},
      "[EncryptionConfiguration](#cfn-qbusiness-application-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[IamIdentityProviderArn](#cfn-qbusiness-application-iamidentityproviderarn)" : {{String}},
      "[IdentityCenterInstanceArn](#cfn-qbusiness-application-identitycenterinstancearn)" : {{String}},
      "[IdentityType](#cfn-qbusiness-application-identitytype)" : {{String}},
      "[PersonalizationConfiguration](#cfn-qbusiness-application-personalizationconfiguration)" : {{PersonalizationConfiguration}},
      "[QAppsConfiguration](#cfn-qbusiness-application-qappsconfiguration)" : {{QAppsConfiguration}},
      "[QuickSightConfiguration](#cfn-qbusiness-application-quicksightconfiguration)" : {{QuickSightConfiguration}},
      "[RoleArn](#cfn-qbusiness-application-rolearn)" : {{String}},
      "[Tags](#cfn-qbusiness-application-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-qbusiness-application-syntax.yaml"></a>

```
Type: AWS::QBusiness::Application
Properties:
  [AttachmentsConfiguration](#cfn-qbusiness-application-attachmentsconfiguration): {{
    AttachmentsConfiguration}}
  [AutoSubscriptionConfiguration](#cfn-qbusiness-application-autosubscriptionconfiguration): {{
    AutoSubscriptionConfiguration}}
  [ClientIdsForOIDC](#cfn-qbusiness-application-clientidsforoidc): {{
    - String}}
  [Description](#cfn-qbusiness-application-description): {{String}}
  [DisplayName](#cfn-qbusiness-application-displayname): {{String}}
  [EncryptionConfiguration](#cfn-qbusiness-application-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [IamIdentityProviderArn](#cfn-qbusiness-application-iamidentityproviderarn): {{String}}
  [IdentityCenterInstanceArn](#cfn-qbusiness-application-identitycenterinstancearn): {{String}}
  [IdentityType](#cfn-qbusiness-application-identitytype): {{String}}
  [PersonalizationConfiguration](#cfn-qbusiness-application-personalizationconfiguration): {{
    PersonalizationConfiguration}}
  [QAppsConfiguration](#cfn-qbusiness-application-qappsconfiguration): {{
    QAppsConfiguration}}
  [QuickSightConfiguration](#cfn-qbusiness-application-quicksightconfiguration): {{
    QuickSightConfiguration}}
  [RoleArn](#cfn-qbusiness-application-rolearn): {{String}}
  [Tags](#cfn-qbusiness-application-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-qbusiness-application-properties"></a>

`AttachmentsConfiguration`  <a name="cfn-qbusiness-application-attachmentsconfiguration"></a>
Configuration information for the file upload during chat feature.
*Required*: No
*Type*: [AttachmentsConfiguration](aws-properties-qbusiness-application-attachmentsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoSubscriptionConfiguration`  <a name="cfn-qbusiness-application-autosubscriptionconfiguration"></a>
Subscription configuration information for an Amazon Q Business application using IAM identity federation for user management.
*Required*: No
*Type*: [AutoSubscriptionConfiguration](aws-properties-qbusiness-application-autosubscriptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientIdsForOIDC`  <a name="cfn-qbusiness-application-clientidsforoidc"></a>
The OIDC client ID for a Amazon Q Business application.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-qbusiness-application-description"></a>
A description for the Amazon Q Business application.
*Required*: No
*Type*: String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-qbusiness-application-displayname"></a>
The name of the Amazon Q Business application.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfiguration`  <a name="cfn-qbusiness-application-encryptionconfiguration"></a>
Provides the identifier of the AWS KMS key used to encrypt data indexed by Amazon Q Business. Amazon Q Business doesn't support asymmetric keys.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-qbusiness-application-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IamIdentityProviderArn`  <a name="cfn-qbusiness-application-iamidentityproviderarn"></a>
The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):iam::\d{12}:(oidc-provider|saml-provider)/[a-zA-Z0-9_\.\/@\-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityCenterInstanceArn`  <a name="cfn-qbusiness-application-identitycenterinstancearn"></a>
 The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.
*Required*: `Yes`
*Required*: Conditional
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityType`  <a name="cfn-qbusiness-application-identitytype"></a>
The authentication type being used by a Amazon Q Business application.
*Required*: No
*Type*: String
*Allowed values*: `AWS_IAM_IDP_SAML | AWS_IAM_IDP_OIDC | AWS_IAM_IDC | AWS_QUICKSIGHT_IDP | ANONYMOUS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PersonalizationConfiguration`  <a name="cfn-qbusiness-application-personalizationconfiguration"></a>
Configuration information about chat response personalization. For more information, see [Personalizing chat responses](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html).
*Required*: No
*Type*: [PersonalizationConfiguration](aws-properties-qbusiness-application-personalizationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QAppsConfiguration`  <a name="cfn-qbusiness-application-qappsconfiguration"></a>
Configuration information about Amazon Q Apps.
*Required*: No
*Type*: [QAppsConfiguration](aws-properties-qbusiness-application-qappsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QuickSightConfiguration`  <a name="cfn-qbusiness-application-quicksightconfiguration"></a>
The Amazon Quick configuration for an Amazon Q Business application that uses Quick as the identity provider.
*Required*: No
*Type*: [QuickSightConfiguration](aws-properties-qbusiness-application-quicksightconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-qbusiness-application-rolearn"></a>
 The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics. If this property is not specified, Amazon Q Business will create a [service linked role (SLR)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html#slr-permissions) and use it as the application's role.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-qbusiness-application-tags"></a>
A list of key-value pairs that identify or categorize your Amazon Q Business application. You can also use tags to help control access to the application. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
*Required*: No
*Type*: Array of [Tag](aws-properties-qbusiness-application-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-qbusiness-application-return-values"></a>

### Ref
<a name="aws-resource-qbusiness-application-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application ID. For example:

 `{"Ref": "ApplicationId"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-qbusiness-application-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-qbusiness-application-return-values-fn--getatt-fn--getatt"></a>

`ApplicationArn`  <a name="ApplicationArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of the Amazon Q Business application.

`ApplicationId`  <a name="ApplicationId-fn::getatt"></a>
The identifier for the Amazon Q Business application.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp when the Amazon Q Business application was created.

`IdentityCenterApplicationArn`  <a name="IdentityCenterApplicationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AWSIAM Identity Center instance attached to your Amazon Q Business application.

`Status`  <a name="Status-fn::getatt"></a>
The status of the Amazon Q Business application. The application is ready to use when the status is `ACTIVE`.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The Unix timestamp when the Amazon Q Business application was last updated.
