---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-hostedconfigurationversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::HostedConfigurationVersion
<a name="aws-resource-appconfig-hostedconfigurationversion"></a>

Create a new configuration in the AWS AppConfig hosted configuration store. Configurations must be 1 MB or smaller. The AWS AppConfig hosted configuration store provides the following benefits over other configuration store options.
+ You don't need to set up and configure other services such as Amazon Simple Storage Service (Amazon S3) or Parameter Store.
+ You don't need to configure AWS Identity and Access Management (IAM) permissions to use the configuration store.
+ You can store configurations in any content type.
+ There is no cost to use the store.
+ You can create a configuration and add it to the store when you create a configuration profile.

## Syntax
<a name="aws-resource-appconfig-hostedconfigurationversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appconfig-hostedconfigurationversion-syntax.json"></a>

```
{
  "Type" : "AWS::AppConfig::HostedConfigurationVersion",
  "Properties" : {
      "[ApplicationId](#cfn-appconfig-hostedconfigurationversion-applicationid)" : {{String}},
      "[ConfigurationProfileId](#cfn-appconfig-hostedconfigurationversion-configurationprofileid)" : {{String}},
      "[Content](#cfn-appconfig-hostedconfigurationversion-content)" : {{String}},
      "[ContentType](#cfn-appconfig-hostedconfigurationversion-contenttype)" : {{String}},
      "[Description](#cfn-appconfig-hostedconfigurationversion-description)" : {{String}},
      "[LatestVersionNumber](#cfn-appconfig-hostedconfigurationversion-latestversionnumber)" : {{Integer}},
      "[VersionLabel](#cfn-appconfig-hostedconfigurationversion-versionlabel)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-appconfig-hostedconfigurationversion-syntax.yaml"></a>

```
Type: AWS::AppConfig::HostedConfigurationVersion
Properties:
  [ApplicationId](#cfn-appconfig-hostedconfigurationversion-applicationid): {{String}}
  [ConfigurationProfileId](#cfn-appconfig-hostedconfigurationversion-configurationprofileid): {{String}}
  [Content](#cfn-appconfig-hostedconfigurationversion-content): {{String}}
  [ContentType](#cfn-appconfig-hostedconfigurationversion-contenttype): {{String}}
  [Description](#cfn-appconfig-hostedconfigurationversion-description): {{String}}
  [LatestVersionNumber](#cfn-appconfig-hostedconfigurationversion-latestversionnumber): {{Integer}}
  [VersionLabel](#cfn-appconfig-hostedconfigurationversion-versionlabel): {{String}}
```

## Properties
<a name="aws-resource-appconfig-hostedconfigurationversion-properties"></a>

`ApplicationId`  <a name="cfn-appconfig-hostedconfigurationversion-applicationid"></a>
The ID or name of the application.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z0-9]{4,7}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConfigurationProfileId`  <a name="cfn-appconfig-hostedconfigurationversion-configurationprofileid"></a>
The ID or name of the configuration profile.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z0-9]{4,7}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Content`  <a name="cfn-appconfig-hostedconfigurationversion-content"></a>
The configuration data, as bytes.
AWS AppConfig accepts any type of data, including text formats like JSON or TOML, or binary formats like protocol buffers or compressed data.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContentType`  <a name="cfn-appconfig-hostedconfigurationversion-contenttype"></a>
A standard MIME type describing the format of the configuration content. For more information, see [Content-Type](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-appconfig-hostedconfigurationversion-description"></a>
A description of the configuration.
Due to HTTP limitations, this field only supports ASCII characters.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LatestVersionNumber`  <a name="cfn-appconfig-hostedconfigurationversion-latestversionnumber"></a>
An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VersionLabel`  <a name="cfn-appconfig-hostedconfigurationversion-versionlabel"></a>
A user-defined label for an AWS AppConfig hosted configuration version.
*Required*: No
*Type*: String
*Pattern*: `^$|.*[^0-9].*`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-appconfig-hostedconfigurationversion-return-values"></a>

### Ref
<a name="aws-resource-appconfig-hostedconfigurationversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the version number.

### Fn::GetAtt
<a name="aws-resource-appconfig-hostedconfigurationversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-appconfig-hostedconfigurationversion-return-values-fn--getatt-fn--getatt"></a>

`VersionNumber`  <a name="VersionNumber-fn::getatt"></a>
The configuration version.

## Examples
<a name="aws-resource-appconfig-hostedconfigurationversion--examples"></a>

**Topics**
+ [AWS AppConfig feature flag](#aws-resource-appconfig-hostedconfigurationversion--examples--feature_flag)
+ [AWS AppConfig hosted configuration](#aws-resource-appconfig-hostedconfigurationversion--examples--hosted_configuration)

### AWS AppConfig feature flag
<a name="aws-resource-appconfig-hostedconfigurationversion--examples--feature_flag"></a>

The following example creates an AWS AppConfig configuration profile of type `HostedConfigurationVersion`. The feature flag created by this example enables cryptocurrency at checkout. AWS AppConfig stores the configuration data for this profile in the AWS AppConfig hosted configuration store.

#### JSON
<a name="aws-resource-appconfig-hostedconfigurationversion--examples--feature_flag--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Transform": "AWS::LanguageExtensions",
  "Resources": {
    "MySuperCoolApp": {
      "Type": "AWS::AppConfig::Application",
      "Properties": {
        "Name": "MySuperCoolApp"
      }
    },
    "MyFeatureFlags": {
      "Type": "AWS::AppConfig::ConfigurationProfile",
      "Properties": {
        "Name": "MyFeatureFlags",
        "ApplicationId": "MySuperCoolApp",
        "LocationUri": "hosted",
        "Type": "AWS.AppConfig.FeatureFlags"
      }
    },
    "MyFeatureFlagsVersion": {
      "Type": "AWS::AppConfig::HostedConfigurationVersion",
      "Properties": {
        "ApplicationId": "MySuperCoolApp",
        "ConfigurationProfileId": "MyFeatureFlags",
        "ContentType": "application/json",
        "VersionLabel": "v1.0.0",
        "Content": {
          "Fn::ToJsonString": {
            "flags": {
              "allow-cryptocurrency-at-checkout": {
                "attributes": {
                  "allowed-currency": {
                    "constraints": {
                      "elements": {
                        "enum": [
                          "BTC",
                          "ETH",
                          "XRP"
                        ],
                        "type": "string"
                      },
                      "type": "array"
                    }
                  },
                  "bitcoin-discount-percentage": {
                    "constraints": {
                      "maximum": 25,
                      "minimum": 0,
                      "type": "number"
                    }
                  }
                },
                "name": "Allow Cryptocurrency at Checkout"
              }
            },
            "values": {
              "allow-cryptocurrency-at-checkout": {
                "allowed-currency": [
                  "BTC",
                  "ETH"
                ],
                "bitcoin-discount-percentage": 5,
                "enabled": true
              }
            },
            "version": "1"
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-appconfig-hostedconfigurationversion--examples--feature_flag--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Transform: 'AWS::LanguageExtensions'
Resources:
  MySuperCoolApp:
    Type: 'AWS::AppConfig::Application'
    Properties:
      Name: MySuperCoolApp

  MyFeatureFlags:
    Type: 'AWS::AppConfig::ConfigurationProfile'
    Properties:
      Name: MyFeatureFlags
      ApplicationId: !Ref MySuperCoolApp
      LocationUri: hosted
      Type: AWS.AppConfig.FeatureFlags

  MyFeatureFlagsVersion:
    Type: 'AWS::AppConfig::HostedConfigurationVersion'
    Properties:
      ApplicationId: !Ref MySuperCoolApp
      ConfigurationProfileId: !Ref MyFeatureFlags
      ContentType: application/json
      VersionLabel: "v1.0.0"
      Content:
        Fn::ToJsonString:
            flags:
              allow-cryptocurrency-at-checkout:
                attributes:
                  allowed-currency:
                    constraints:
                      elements:
                        enum:
                          - BTC
                          - ETH
                          - XRP
                        type: string
                      type: array
                  bitcoin-discount-percentage:
                    constraints:
                      maximum: 25
                      minimum: 0
                      type: number
                name: Allow Cryptocurrency at Checkout
            values:
              allow-cryptocurrency-at-checkout:
                allowed-currency:
                  - BTC
                  - ETH
                bitcoin-discount-percentage: 5
                enabled: true
            version: '1'
```

### AWS AppConfig hosted configuration
<a name="aws-resource-appconfig-hostedconfigurationversion--examples--hosted_configuration"></a>

The following example creates an AWS AppConfig configuration profile named `MyTestProfile` for an application called `MyApplication`. AWS AppConfig stores the configuration data for this profile in the AWS AppConfig hosted configuration store.

#### JSON
<a name="aws-resource-appconfig-hostedconfigurationversion--examples--hosted_configuration--json"></a>

```
{
  "Resources": {
    "DependentApplication": {
      "Type": "AWS::AppConfig::Application",
      "Properties": {
        "Name": "MyApplication"
      }
    },
    "DependentConfigurationProfile": {
      "Type": "AWS::AppConfig::ConfigurationProfile",
      "Properties": {
        "ApplicationId": "DependentApplication",
        "Name": "MyTestProfile",
        "LocationUri": "hosted"
      }
    },
    "BasicHostedConfigurationVersion": {
      "Type": "AWS::AppConfig::HostedConfigurationVersion",
      "Properties": {
        "ApplicationId": "DependentApplication",
        "ConfigurationProfileId": "DependentConfigurationProfile",
        "Description": "A sample hosted configuration version",
        "Content": "My hosted configuration content",
        "ContentType": "text/plain"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-appconfig-hostedconfigurationversion--examples--hosted_configuration--yaml"></a>

```
Resources:
  DependentApplication:
    Type: AWS::AppConfig::Application
    Properties:
      Name: "MyApplication"
  DependentConfigurationProfile:
    Type: AWS::AppConfig::ConfigurationProfile
    Properties:
      ApplicationId: !Ref DependentApplication
      Name: "MyTestProfile"
      LocationUri: "hosted"
  BasicHostedConfigurationVersion:
    Type: AWS::AppConfig::HostedConfigurationVersion
    Properties:
      ApplicationId: !Ref DependentApplication
      ConfigurationProfileId: !Ref DependentConfigurationProfile
      Description: 'A sample hosted configuration version'
      Content: 'My hosted configuration content'
      ContentType: 'text/plain'
```

## See also
<a name="aws-resource-appconfig-hostedconfigurationversion--seealso"></a>
+  [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)
+  [Creating a configuration and a configuration profile ](https://docs.aws.amazon.com/systems-manager/latest/userguide/appconfig-creating-configuration-and-profile.html)
+  [About the AWS AppConfig hosted configuration store](https://docs.aws.amazon.com/systems-manager/latest/userguide/appconfig-creating-configuration-and-profile.html#appconfig-creating-configuration-and-profile-about-hosted-store)
