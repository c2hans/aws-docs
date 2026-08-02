---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-webapp-identityproviderdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::WebApp IdentityProviderDetails
<a name="aws-properties-transfer-webapp-identityproviderdetails"></a>

 A structure that describes the values to use for the IAM Identity Center settings when you create or update a web app.

## Syntax
<a name="aws-properties-transfer-webapp-identityproviderdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-webapp-identityproviderdetails-syntax.json"></a>

```
{
  "[ApplicationArn](#cfn-transfer-webapp-identityproviderdetails-applicationarn)" : {{String}},
  "[InstanceArn](#cfn-transfer-webapp-identityproviderdetails-instancearn)" : {{String}},
  "[Role](#cfn-transfer-webapp-identityproviderdetails-role)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-webapp-identityproviderdetails-syntax.yaml"></a>

```
  [ApplicationArn](#cfn-transfer-webapp-identityproviderdetails-applicationarn): {{String}}
  [InstanceArn](#cfn-transfer-webapp-identityproviderdetails-instancearn): {{String}}
  [Role](#cfn-transfer-webapp-identityproviderdetails-role): {{String}}
```

## Properties
<a name="aws-properties-transfer-webapp-identityproviderdetails-properties"></a>

`ApplicationArn`  <a name="cfn-transfer-webapp-identityproviderdetails-applicationarn"></a>
The Amazon Resource Name (ARN) for the IAM Identity Center application: this value is set automatically when you create your web app.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w-]+:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}$`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-transfer-webapp-identityproviderdetails-instancearn"></a>
The Amazon Resource Name (ARN) for the IAM Identity Center used for the web app.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w-]+:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Role`  <a name="cfn-transfer-webapp-identityproviderdetails-role"></a>
The IAM role in IAM Identity Center used for the web app.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z-]+:iam::[0-9]{12}:role[:/]\S+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
