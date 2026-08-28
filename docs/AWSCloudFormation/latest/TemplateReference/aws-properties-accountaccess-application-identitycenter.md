---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accountaccess-application-identitycenter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccountAccess::Application IdentityCenter
<a name="aws-properties-accountaccess-application-identitycenter"></a>

Specifies the IAM Identity Center instance to use as the identity source for an application.

## Syntax
<a name="aws-properties-accountaccess-application-identitycenter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accountaccess-application-identitycenter-syntax.json"></a>

```
{
  "[ApplicationArn](#cfn-accountaccess-application-identitycenter-applicationarn)" : {{String}},
  "[InstanceArn](#cfn-accountaccess-application-identitycenter-instancearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-accountaccess-application-identitycenter-syntax.yaml"></a>

```
  [ApplicationArn](#cfn-accountaccess-application-identitycenter-applicationarn): {{String}}
  [InstanceArn](#cfn-accountaccess-application-identitycenter-instancearn): {{String}}
```

## Properties
<a name="aws-properties-accountaccess-application-identitycenter-properties"></a>

`ApplicationArn`  <a name="cfn-accountaccess-application-identitycenter-applicationarn"></a>
The ARN of the IAM Identity Center application created for this account access manager application. This property is not required or supported as input. It can be read after creation.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9-]+:sso::[0-9]{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}$`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceArn`  <a name="cfn-accountaccess-application-identitycenter-instancearn"></a>
The ARN of the IAM Identity Center instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-]+:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
