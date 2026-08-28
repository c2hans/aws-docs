---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-accountaccess-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccountAccess::Application
<a name="aws-resource-accountaccess-application"></a>

Specifies the identity source for the application. The identity source defines the IAM Identity Center instance that provides principals for entitlements.

## Syntax
<a name="aws-resource-accountaccess-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-accountaccess-application-syntax.json"></a>

```
{
  "Type" : "AWS::AccountAccess::Application",
  "Properties" : {
      "[IdentitySource](#cfn-accountaccess-application-identitysource)" : {{IdentitySource}},
      "[Tags](#cfn-accountaccess-application-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-accountaccess-application-syntax.yaml"></a>

```
Type: AWS::AccountAccess::Application
Properties:
  [IdentitySource](#cfn-accountaccess-application-identitysource): {{
    IdentitySource}}
  [Tags](#cfn-accountaccess-application-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-accountaccess-application-properties"></a>

`IdentitySource`  <a name="cfn-accountaccess-application-identitysource"></a>
Specifies the identity source for the application. The identity source defines the IAM Identity Center instance that provides principals for entitlements.
*Required*: Yes
*Type*: [IdentitySource](aws-properties-accountaccess-application-identitysource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-accountaccess-application-tags"></a>
Specifies the tags to assign to the application.
*Required*: No
*Type*: Array of [Tag](aws-properties-accountaccess-application-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-accountaccess-application-return-values"></a>

### Ref
<a name="aws-resource-accountaccess-application-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the application.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-accountaccess-application-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-accountaccess-application-return-values-fn--getatt-fn--getatt"></a>

`ApplicationArn`  <a name="ApplicationArn-fn::getatt"></a>
The ARN of the IAM Identity Center application created for this account access manager application.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the application was created.

`IdentitySource.IdentityCenter.ApplicationArn`  <a name="IdentitySource.IdentityCenter.ApplicationArn-fn::getatt"></a>
The ARN of the IAM Identity Center application created for this account access manager application. This property is not required or supported as input. It can be read after creation.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the application.

`TenantId`  <a name="TenantId-fn::getatt"></a>
The tenant identifier associated with the application.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the application was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
