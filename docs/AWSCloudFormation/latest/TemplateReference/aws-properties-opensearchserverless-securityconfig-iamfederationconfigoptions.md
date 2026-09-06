---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-securityconfig-iamfederationconfigoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::SecurityConfig IamFederationConfigOptions
<a name="aws-properties-opensearchserverless-securityconfig-iamfederationconfigoptions"></a>

Describes IAM federation options for an OpenSearch Serverless security configuration in the form of a key-value map. These options define how OpenSearch Serverless integrates with external identity providers using federation.

## Syntax
<a name="aws-properties-opensearchserverless-securityconfig-iamfederationconfigoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-securityconfig-iamfederationconfigoptions-syntax.json"></a>

```
{
  "[GroupAttribute](#cfn-opensearchserverless-securityconfig-iamfederationconfigoptions-groupattribute)" : {{String}},
  "[UserAttribute](#cfn-opensearchserverless-securityconfig-iamfederationconfigoptions-userattribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-securityconfig-iamfederationconfigoptions-syntax.yaml"></a>

```
  [GroupAttribute](#cfn-opensearchserverless-securityconfig-iamfederationconfigoptions-groupattribute): {{String}}
  [UserAttribute](#cfn-opensearchserverless-securityconfig-iamfederationconfigoptions-userattribute): {{String}}
```

## Properties
<a name="aws-properties-opensearchserverless-securityconfig-iamfederationconfigoptions-properties"></a>

`GroupAttribute`  <a name="cfn-opensearchserverless-securityconfig-iamfederationconfigoptions-groupattribute"></a>
The group attribute for this IAM federation integration. This attribute is used to map identity provider groups to OpenSearch Serverless permissions.
*Required*: No
*Type*: String
*Pattern*: `[A-Za-z][A-Za-z0-9_.:/=+\-@]*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserAttribute`  <a name="cfn-opensearchserverless-securityconfig-iamfederationconfigoptions-userattribute"></a>
The user attribute for this IAM federation integration. This attribute is used to identify users in the federated authentication process.
*Required*: No
*Type*: String
*Pattern*: `[A-Za-z][A-Za-z0-9_.:/=+\-@]*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
