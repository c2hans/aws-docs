---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appstream-entitlement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Entitlement
<a name="aws-resource-appstream-entitlement"></a>

Creates an entitlement to control access, based on user attributes, to specific applications within a stack. Entitlements apply to SAML 2.0 federated user identities. Amazon WorkSpaces Applications user pool and streaming URL users are entitled to all applications in a stack. Entitlements don't apply to the desktop stream view application or to applications managed by a dynamic app provider using the Dynamic Application Framework.

## Syntax
<a name="aws-resource-appstream-entitlement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appstream-entitlement-syntax.json"></a>

```
{
  "Type" : "AWS::AppStream::Entitlement",
  "Properties" : {
      "[AppVisibility](#cfn-appstream-entitlement-appvisibility)" : {{String}},
      "[Attributes](#cfn-appstream-entitlement-attributes)" : {{[ Attribute, ... ]}},
      "[Description](#cfn-appstream-entitlement-description)" : {{String}},
      "[Name](#cfn-appstream-entitlement-name)" : {{String}},
      "[StackName](#cfn-appstream-entitlement-stackname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-appstream-entitlement-syntax.yaml"></a>

```
Type: AWS::AppStream::Entitlement
Properties:
  [AppVisibility](#cfn-appstream-entitlement-appvisibility): {{String}}
  [Attributes](#cfn-appstream-entitlement-attributes): {{
    - Attribute}}
  [Description](#cfn-appstream-entitlement-description): {{String}}
  [Name](#cfn-appstream-entitlement-name): {{String}}
  [StackName](#cfn-appstream-entitlement-stackname): {{String}}
```

## Properties
<a name="aws-resource-appstream-entitlement-properties"></a>

`AppVisibility`  <a name="cfn-appstream-entitlement-appvisibility"></a>
Specifies whether to entitle all apps or only selected apps.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL | ASSOCIATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attributes`  <a name="cfn-appstream-entitlement-attributes"></a>
The attributes of the entitlement.
*Required*: Yes
*Type*: Array of [Attribute](aws-properties-appstream-entitlement-attribute.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-appstream-entitlement-description"></a>
The description of the entitlement.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appstream-entitlement-name"></a>
The name of the entitlement.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StackName`  <a name="cfn-appstream-entitlement-stackname"></a>
The name of the stack.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-appstream-entitlement-return-values"></a>

### Ref
<a name="aws-resource-appstream-entitlement-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the combination of the `StackName` and `Name`, such as `abcdefStack|abcdefEntitlement`.

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-appstream-entitlement-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-appstream-entitlement-return-values-fn--getatt-fn--getatt"></a>

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time when the entitlement was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time when the entitlement was last modified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
