---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::SecurityConfig SamlConfigOptions
<a name="aws-properties-opensearchserverless-securityconfig-samlconfigoptions"></a>

Describes SAML options for an OpenSearch Serverless security configuration in the form of a key-value map.

## Syntax
<a name="aws-properties-opensearchserverless-securityconfig-samlconfigoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-securityconfig-samlconfigoptions-syntax.json"></a>

```
{
  "[GroupAttribute](#cfn-opensearchserverless-securityconfig-samlconfigoptions-groupattribute)" : {{String}},
  "[Metadata](#cfn-opensearchserverless-securityconfig-samlconfigoptions-metadata)" : {{String}},
  "[OpenSearchServerlessEntityId](#cfn-opensearchserverless-securityconfig-samlconfigoptions-opensearchserverlessentityid)" : {{String}},
  "[SessionTimeout](#cfn-opensearchserverless-securityconfig-samlconfigoptions-sessiontimeout)" : {{Integer}},
  "[UserAttribute](#cfn-opensearchserverless-securityconfig-samlconfigoptions-userattribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-securityconfig-samlconfigoptions-syntax.yaml"></a>

```
  [GroupAttribute](#cfn-opensearchserverless-securityconfig-samlconfigoptions-groupattribute): {{String}}
  [Metadata](#cfn-opensearchserverless-securityconfig-samlconfigoptions-metadata): {{String}}
  [OpenSearchServerlessEntityId](#cfn-opensearchserverless-securityconfig-samlconfigoptions-opensearchserverlessentityid): {{String}}
  [SessionTimeout](#cfn-opensearchserverless-securityconfig-samlconfigoptions-sessiontimeout): {{Integer}}
  [UserAttribute](#cfn-opensearchserverless-securityconfig-samlconfigoptions-userattribute): {{String}}
```

## Properties
<a name="aws-properties-opensearchserverless-securityconfig-samlconfigoptions-properties"></a>

`GroupAttribute`  <a name="cfn-opensearchserverless-securityconfig-samlconfigoptions-groupattribute"></a>
The group attribute for this SAML integration.
*Required*: No
*Type*: String
*Pattern*: `[\w+=,.@-]+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metadata`  <a name="cfn-opensearchserverless-securityconfig-samlconfigoptions-metadata"></a>
The XML IdP metadata file generated from your identity provider.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+`
*Minimum*: `1`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenSearchServerlessEntityId`  <a name="cfn-opensearchserverless-securityconfig-samlconfigoptions-opensearchserverlessentityid"></a>
Custom entity ID attribute to override the default entity ID for this SAML integration.
*Required*: No
*Type*: String
*Pattern*: `^aws:opensearch:[0-9]{12}:*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionTimeout`  <a name="cfn-opensearchserverless-securityconfig-samlconfigoptions-sessiontimeout"></a>
The session timeout, in minutes. Default is 60 minutes (12 hours).
*Required*: No
*Type*: Integer
*Minimum*: `5`
*Maximum*: `720`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserAttribute`  <a name="cfn-opensearchserverless-securityconfig-samlconfigoptions-userattribute"></a>
A user attribute for this SAML integration.
*Required*: No
*Type*: String
*Pattern*: `[\w+=,.@-]+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
