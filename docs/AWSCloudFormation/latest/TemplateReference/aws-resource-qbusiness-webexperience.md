---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-qbusiness-webexperience.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::WebExperience
<a name="aws-resource-qbusiness-webexperience"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates an Amazon Q Business web experience.

## Syntax
<a name="aws-resource-qbusiness-webexperience-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-qbusiness-webexperience-syntax.json"></a>

```
{
  "Type" : "AWS::QBusiness::WebExperience",
  "Properties" : {
      "[ApplicationId](#cfn-qbusiness-webexperience-applicationid)" : {{String}},
      "[BrowserExtensionConfiguration](#cfn-qbusiness-webexperience-browserextensionconfiguration)" : {{BrowserExtensionConfiguration}},
      "[CustomizationConfiguration](#cfn-qbusiness-webexperience-customizationconfiguration)" : {{CustomizationConfiguration}},
      "[IdentityProviderConfiguration](#cfn-qbusiness-webexperience-identityproviderconfiguration)" : {{IdentityProviderConfiguration}},
      "[Origins](#cfn-qbusiness-webexperience-origins)" : {{[ String, ... ]}},
      "[RoleArn](#cfn-qbusiness-webexperience-rolearn)" : {{String}},
      "[SamplePromptsControlMode](#cfn-qbusiness-webexperience-samplepromptscontrolmode)" : {{String}},
      "[Subtitle](#cfn-qbusiness-webexperience-subtitle)" : {{String}},
      "[Tags](#cfn-qbusiness-webexperience-tags)" : {{[ Tag, ... ]}},
      "[Title](#cfn-qbusiness-webexperience-title)" : {{String}},
      "[WelcomeMessage](#cfn-qbusiness-webexperience-welcomemessage)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-qbusiness-webexperience-syntax.yaml"></a>

```
Type: AWS::QBusiness::WebExperience
Properties:
  [ApplicationId](#cfn-qbusiness-webexperience-applicationid): {{String}}
  [BrowserExtensionConfiguration](#cfn-qbusiness-webexperience-browserextensionconfiguration): {{
    BrowserExtensionConfiguration}}
  [CustomizationConfiguration](#cfn-qbusiness-webexperience-customizationconfiguration): {{
    CustomizationConfiguration}}
  [IdentityProviderConfiguration](#cfn-qbusiness-webexperience-identityproviderconfiguration): {{
    IdentityProviderConfiguration}}
  [Origins](#cfn-qbusiness-webexperience-origins): {{
    - String}}
  [RoleArn](#cfn-qbusiness-webexperience-rolearn): {{String}}
  [SamplePromptsControlMode](#cfn-qbusiness-webexperience-samplepromptscontrolmode): {{String}}
  [Subtitle](#cfn-qbusiness-webexperience-subtitle): {{String}}
  [Tags](#cfn-qbusiness-webexperience-tags): {{
    - Tag}}
  [Title](#cfn-qbusiness-webexperience-title): {{String}}
  [WelcomeMessage](#cfn-qbusiness-webexperience-welcomemessage): {{String}}
```

## Properties
<a name="aws-resource-qbusiness-webexperience-properties"></a>

`ApplicationId`  <a name="cfn-qbusiness-webexperience-applicationid"></a>
The identifier of the Amazon Q Business web experience.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BrowserExtensionConfiguration`  <a name="cfn-qbusiness-webexperience-browserextensionconfiguration"></a>
The container for browser extension configuration for an Amazon Q Business web experience.
*Required*: No
*Type*: [BrowserExtensionConfiguration](aws-properties-qbusiness-webexperience-browserextensionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomizationConfiguration`  <a name="cfn-qbusiness-webexperience-customizationconfiguration"></a>
Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.
*Required*: No
*Type*: [CustomizationConfiguration](aws-properties-qbusiness-webexperience-customizationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviderConfiguration`  <a name="cfn-qbusiness-webexperience-identityproviderconfiguration"></a>
Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
*Required*: No
*Type*: [IdentityProviderConfiguration](aws-properties-qbusiness-webexperience-identityproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Origins`  <a name="cfn-qbusiness-webexperience-origins"></a>
Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the base URL for accessing a website including the protocol (`http/https`), the domain name, and the port number (if specified).
You must only submit a *base URL* and not a full path. For example, `https://docs.aws.amazon.com`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-qbusiness-webexperience-rolearn"></a>
The Amazon Resource Name (ARN) of the service role attached to your web experience.
The `roleArn` parameter is required when your Amazon Q Business application is created with IAM Identity Center. It is not required for SAML-based applications.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SamplePromptsControlMode`  <a name="cfn-qbusiness-webexperience-samplepromptscontrolmode"></a>
Determines whether sample prompts are enabled in the web experience for an end user.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-qbusiness-webexperience-subtitle"></a>
A subtitle to personalize your Amazon Q Business web experience.
*Required*: No
*Type*: String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-qbusiness-webexperience-tags"></a>
A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
*Required*: No
*Type*: Array of [Tag](aws-properties-qbusiness-webexperience-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-qbusiness-webexperience-title"></a>
The title for your Amazon Q Business web experience.
*Required*: No
*Type*: String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WelcomeMessage`  <a name="cfn-qbusiness-webexperience-welcomemessage"></a>
A message in an Amazon Q Business web experience.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-qbusiness-webexperience-return-values"></a>

### Ref
<a name="aws-resource-qbusiness-webexperience-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application and web experience ID. For example:

 `{"Ref": "ApplicationId|WebExperienceId"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-qbusiness-webexperience-return-values-fn--getatt"></a>

####
<a name="aws-resource-qbusiness-webexperience-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp when the Amazon Q Business application was last updated.

`DefaultEndpoint`  <a name="DefaultEndpoint-fn::getatt"></a>
The endpoint URLs for your Amazon Q Business web experience. The URLs are unique and fully hosted by AWS.

`Status`  <a name="Status-fn::getatt"></a>
The status of your Amazon Q Business web experience.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The Unix timestamp when your Amazon Q Business web experience was updated.

`WebExperienceArn`  <a name="WebExperienceArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of an Amazon Q Business web experience.

`WebExperienceId`  <a name="WebExperienceId-fn::getatt"></a>
The identifier of your Amazon Q Business web experience.
