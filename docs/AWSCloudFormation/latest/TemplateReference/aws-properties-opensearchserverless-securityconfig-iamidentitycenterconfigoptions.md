---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::SecurityConfig IamIdentityCenterConfigOptions
<a name="aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions"></a>

Describes IAM Identity Center options for an OpenSearch Serverless security configuration in the form of a key-value map.

## Syntax
<a name="aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-syntax.json"></a>

```
{
  "[ApplicationArn](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationarn)" : {{String}},
  "[ApplicationDescription](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationdescription)" : {{String}},
  "[ApplicationName](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationname)" : {{String}},
  "[GroupAttribute](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-groupattribute)" : {{String}},
  "[InstanceArn](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-instancearn)" : {{String}},
  "[UserAttribute](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-userattribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-syntax.yaml"></a>

```
  [ApplicationArn](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationarn): {{String}}
  [ApplicationDescription](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationdescription): {{String}}
  [ApplicationName](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationname): {{String}}
  [GroupAttribute](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-groupattribute): {{String}}
  [InstanceArn](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-instancearn): {{String}}
  [UserAttribute](#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-userattribute): {{String}}
```

## Properties
<a name="aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-properties"></a>

`ApplicationArn`  <a name="cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationarn"></a>
The ARN of the IAM Identity Center application used to integrate with OpenSearch Serverless.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationDescription`  <a name="cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationdescription"></a>
The description of the IAM Identity Center application used to integrate with OpenSearch Serverless.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationName`  <a name="cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationname"></a>
The name of the IAM Identity Center application used to integrate with OpenSearch Serverless.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupAttribute`  <a name="cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-groupattribute"></a>
The group attribute for this IAM Identity Center integration. Defaults to `GroupId`.
*Required*: No
*Type*: String
*Allowed values*: `GroupId | GroupName`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-instancearn"></a>
The ARN of the IAM Identity Center instance used to integrate with OpenSearch Serverless.
*Required*: Yes
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserAttribute`  <a name="cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-userattribute"></a>
The user attribute for this IAM Identity Center integration. Defaults to `UserId`
*Required*: No
*Type*: String
*Allowed values*: `UserId | UserName | Email`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
