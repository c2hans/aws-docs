---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-accountaccess-entitlement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccountAccess::Entitlement
<a name="aws-resource-accountaccess-entitlement"></a>

Specifies the entitlement configuration, including the principal and the IAM role to grant access to.

## Syntax
<a name="aws-resource-accountaccess-entitlement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-accountaccess-entitlement-syntax.json"></a>

```
{
  "Type" : "AWS::AccountAccess::Entitlement",
  "Properties" : {
      "[ApplicationArn](#cfn-accountaccess-entitlement-applicationarn)" : {{String}},
      "[Entitlement](#cfn-accountaccess-entitlement-entitlement)" : {{Entitlement}}
    }
}
```

### YAML
<a name="aws-resource-accountaccess-entitlement-syntax.yaml"></a>

```
Type: AWS::AccountAccess::Entitlement
Properties:
  [ApplicationArn](#cfn-accountaccess-entitlement-applicationarn): {{String}}
  [Entitlement](#cfn-accountaccess-entitlement-entitlement): {{
    Entitlement}}
```

## Properties
<a name="aws-resource-accountaccess-entitlement-properties"></a>

`ApplicationArn`  <a name="cfn-accountaccess-entitlement-applicationarn"></a>
Specifies the ARN of the application to create the entitlement for.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-]+:account-access:[a-z0-9]+(-[a-z0-9]+)*:[0-9]{12}:application/[a-zA-Z0-9-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Entitlement`  <a name="cfn-accountaccess-entitlement-entitlement"></a>
Specifies the entitlement configuration, including the principal and the IAM role to grant access to.
*Required*: Yes
*Type*: [Entitlement](aws-properties-accountaccess-entitlement-entitlement.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-accountaccess-entitlement-return-values"></a>

### Ref
<a name="aws-resource-accountaccess-entitlement-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier of the entitlement.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-accountaccess-entitlement-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-accountaccess-entitlement-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the entitlement was created.

`Entitlement.PrincipalRole.Account`  <a name="Entitlement.PrincipalRole.Account-fn::getatt"></a>
The 12-digit AWS account ID where the IAM role resides.

`EntitlementId`  <a name="EntitlementId-fn::getatt"></a>
The unique identifier of the entitlement.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
