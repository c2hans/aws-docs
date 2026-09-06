---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mpa-identitysource-iamidentitycenter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MPA::IdentitySource IamIdentityCenter
<a name="aws-properties-mpa-identitysource-iamidentitycenter"></a>

AWS IAM Identity Center credentials. For more information see, [AWS IAM Identity Center](https://aws.amazon.com/identity-center/) .

## Syntax
<a name="aws-properties-mpa-identitysource-iamidentitycenter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mpa-identitysource-iamidentitycenter-syntax.json"></a>

```
{
  "[ApprovalPortalUrl](#cfn-mpa-identitysource-iamidentitycenter-approvalportalurl)" : {{String}},
  "[InstanceArn](#cfn-mpa-identitysource-iamidentitycenter-instancearn)" : {{String}},
  "[Region](#cfn-mpa-identitysource-iamidentitycenter-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-mpa-identitysource-iamidentitycenter-syntax.yaml"></a>

```
  [ApprovalPortalUrl](#cfn-mpa-identitysource-iamidentitycenter-approvalportalurl): {{String}}
  [InstanceArn](#cfn-mpa-identitysource-iamidentitycenter-instancearn): {{String}}
  [Region](#cfn-mpa-identitysource-iamidentitycenter-region): {{String}}
```

## Properties
<a name="aws-properties-mpa-identitysource-iamidentitycenter-properties"></a>

`ApprovalPortalUrl`  <a name="cfn-mpa-identitysource-iamidentitycenter-approvalportalurl"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceArn`  <a name="cfn-mpa-identitysource-iamidentitycenter-instancearn"></a>
Amazon Resource Name (ARN) for the IAM Identity Center instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.+:sso:::instance/(?:sso)?ins-[a-zA-Z0-9-.]{16}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Region`  <a name="cfn-mpa-identitysource-iamidentitycenter-region"></a>
AWS Region where the IAM Identity Center instance is located.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
