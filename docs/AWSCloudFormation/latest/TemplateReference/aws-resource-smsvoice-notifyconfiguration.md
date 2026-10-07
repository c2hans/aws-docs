---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-notifyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::NotifyConfiguration
<a name="aws-resource-smsvoice-notifyconfiguration"></a>

Creates a new notify configuration for managed messaging. A notify configuration defines the settings for sending templated messages, including the display name, use case, enabled channels, and enabled countries.

## Syntax
<a name="aws-resource-smsvoice-notifyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-notifyconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::NotifyConfiguration",
  "Properties" : {
      "[DefaultTemplateId](#cfn-smsvoice-notifyconfiguration-defaulttemplateid)" : {{String}},
      "[DeletionProtectionEnabled](#cfn-smsvoice-notifyconfiguration-deletionprotectionenabled)" : {{Boolean}},
      "[DisplayName](#cfn-smsvoice-notifyconfiguration-displayname)" : {{String}},
      "[EnabledChannels](#cfn-smsvoice-notifyconfiguration-enabledchannels)" : {{[ String, ... ]}},
      "[EnabledCountries](#cfn-smsvoice-notifyconfiguration-enabledcountries)" : {{[ String, ... ]}},
      "[PoolId](#cfn-smsvoice-notifyconfiguration-poolid)" : {{String}},
      "[Tags](#cfn-smsvoice-notifyconfiguration-tags)" : {{[ Tag, ... ]}},
      "[UseCase](#cfn-smsvoice-notifyconfiguration-usecase)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-notifyconfiguration-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::NotifyConfiguration
Properties:
  [DefaultTemplateId](#cfn-smsvoice-notifyconfiguration-defaulttemplateid): {{String}}
  [DeletionProtectionEnabled](#cfn-smsvoice-notifyconfiguration-deletionprotectionenabled): {{Boolean}}
  [DisplayName](#cfn-smsvoice-notifyconfiguration-displayname): {{String}}
  [EnabledChannels](#cfn-smsvoice-notifyconfiguration-enabledchannels): {{
    - String}}
  [EnabledCountries](#cfn-smsvoice-notifyconfiguration-enabledcountries): {{
    - String}}
  [PoolId](#cfn-smsvoice-notifyconfiguration-poolid): {{String}}
  [Tags](#cfn-smsvoice-notifyconfiguration-tags): {{
    - Tag}}
  [UseCase](#cfn-smsvoice-notifyconfiguration-usecase): {{String}}
```

## Properties
<a name="aws-resource-smsvoice-notifyconfiguration-properties"></a>

`DefaultTemplateId`  <a name="cfn-smsvoice-notifyconfiguration-defaulttemplateid"></a>
The default template identifier associated with the notify configuration.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_-]*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtectionEnabled`  <a name="cfn-smsvoice-notifyconfiguration-deletionprotectionenabled"></a>
When set to true deletion protection is enabled. By default this is set to false.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-smsvoice-notifyconfiguration-displayname"></a>
The display name associated with the notify configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_ -]+$`
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnabledChannels`  <a name="cfn-smsvoice-notifyconfiguration-enabledchannels"></a>
An array of channels enabled for the notify configuration. Supported values include `SMS` and `VOICE`.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `SMS | VOICE | MMS | RCS`
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnabledCountries`  <a name="cfn-smsvoice-notifyconfiguration-enabledcountries"></a>
An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.
*Required*: No
*Type*: Array of String
*Minimum*: `2`
*Maximum*: `2 | 300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PoolId`  <a name="cfn-smsvoice-notifyconfiguration-poolid"></a>
The identifier of the pool associated with the notify configuration.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_:/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-smsvoice-notifyconfiguration-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-notifyconfiguration-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseCase`  <a name="cfn-smsvoice-notifyconfiguration-usecase"></a>
The use case for the notify configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `CODE_VERIFICATION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-smsvoice-notifyconfiguration-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-notifyconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-smsvoice-notifyconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-smsvoice-notifyconfiguration-return-values-fn--getatt-fn--getatt"></a>

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
The time when the notify configuration was created, in [UNIX epoch time](https://www.epochconverter.com/) format.

`NotifyConfigurationArn`  <a name="NotifyConfigurationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the notify configuration.

`NotifyConfigurationId`  <a name="NotifyConfigurationId-fn::getatt"></a>
The unique identifier for the notify configuration.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the notify configuration.

`Tier`  <a name="Tier-fn::getatt"></a>
The tier of the notify configuration.

`TierUpgradeStatus`  <a name="TierUpgradeStatus-fn::getatt"></a>
The tier upgrade status of the notify configuration.
