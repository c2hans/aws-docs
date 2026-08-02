---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-qbusiness-permission.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Permission
<a name="aws-resource-qbusiness-permission"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Adds or updates a permission policy for a Amazon Q Business application, allowing cross-account access for an ISV. This operation creates a new policy statement for the specified Amazon Q Business application. The policy statement defines the IAM actions that the ISV is allowed to perform on the Amazon Q Business application's resources.

## Syntax
<a name="aws-resource-qbusiness-permission-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-qbusiness-permission-syntax.json"></a>

```
{
  "Type" : "AWS::QBusiness::Permission",
  "Properties" : {
      "[Actions](#cfn-qbusiness-permission-actions)" : {{[ String, ... ]}},
      "[ApplicationId](#cfn-qbusiness-permission-applicationid)" : {{String}},
      "[Conditions](#cfn-qbusiness-permission-conditions)" : {{[ Condition, ... ]}},
      "[Principal](#cfn-qbusiness-permission-principal)" : {{String}},
      "[StatementId](#cfn-qbusiness-permission-statementid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-qbusiness-permission-syntax.yaml"></a>

```
Type: AWS::QBusiness::Permission
Properties:
  [Actions](#cfn-qbusiness-permission-actions): {{
    - String}}
  [ApplicationId](#cfn-qbusiness-permission-applicationid): {{String}}
  [Conditions](#cfn-qbusiness-permission-conditions): {{
    - Condition}}
  [Principal](#cfn-qbusiness-permission-principal): {{String}}
  [StatementId](#cfn-qbusiness-permission-statementid): {{String}}
```

## Properties
<a name="aws-resource-qbusiness-permission-properties"></a>

`Actions`  <a name="cfn-qbusiness-permission-actions"></a>
The list of Amazon Q Business actions that the ISV is allowed to perform.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ApplicationId`  <a name="cfn-qbusiness-permission-applicationid"></a>
The unique identifier of the Amazon Q Business application.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Conditions`  <a name="cfn-qbusiness-permission-conditions"></a>
Property description not available.
*Required*: No
*Type*: Array of [Condition](aws-properties-qbusiness-permission-condition.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Principal`  <a name="cfn-qbusiness-permission-principal"></a>
Provides user and group information used for filtering documents to use for generating Amazon Q Business conversation responses.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:iam::[0-9]{12}:role/[a-zA-Z0-9_/+=,.@-]+$`
*Minimum*: `1`
*Maximum*: `1284`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StatementId`  <a name="cfn-qbusiness-permission-statementid"></a>
A unique identifier for the policy statement.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-qbusiness-permission-return-values"></a>

### Ref
<a name="aws-resource-qbusiness-permission-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application and statement ID. For example:

 `{"Ref": "ApplicationId|StatementId"}`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
