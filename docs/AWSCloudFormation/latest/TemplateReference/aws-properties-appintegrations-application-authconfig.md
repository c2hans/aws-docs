---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appintegrations-application-authconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppIntegrations::Application AuthConfig

<a name="aws-properties-appintegrations-application-authconfig-description"></a>The `AuthConfig` property type specifies Property description not available. for an [AWS::AppIntegrations::Application](aws-resource-appintegrations-application.md).

## Syntax
<a name="aws-properties-appintegrations-application-authconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appintegrations-application-authconfig-syntax.json"></a>

```json
{
  "[AudienceOverride](#cfn-appintegrations-application-authconfig-audienceoverride)" : {{String}},
  "[AuthType](#cfn-appintegrations-application-authconfig-authtype)" : {{String}},
  "[CredentialProviderIdentifier](#cfn-appintegrations-application-authconfig-credentialprovideridentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-appintegrations-application-authconfig-syntax.yaml"></a>

```yaml
  [AudienceOverride](#cfn-appintegrations-application-authconfig-audienceoverride): {{String}}
  [AuthType](#cfn-appintegrations-application-authconfig-authtype): {{String}}
  [CredentialProviderIdentifier](#cfn-appintegrations-application-authconfig-credentialprovideridentifier): {{String}}
```

## Properties
<a name="aws-properties-appintegrations-application-authconfig-properties"></a>

`AudienceOverride`  <a name="cfn-appintegrations-application-authconfig-audienceoverride"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthType`  <a name="cfn-appintegrations-application-authconfig-authtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `API_KEY | CONNECT_JWT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialProviderIdentifier`  <a name="cfn-appintegrations-application-authconfig-credentialprovideridentifier"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
