---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicecatalog-launchroleconstraint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::LaunchRoleConstraint
<a name="aws-resource-servicecatalog-launchroleconstraint"></a>

Specifies a launch constraint.

## Syntax
<a name="aws-resource-servicecatalog-launchroleconstraint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-servicecatalog-launchroleconstraint-syntax.json"></a>

```
{
  "Type" : "AWS::ServiceCatalog::LaunchRoleConstraint",
  "Properties" : {
      "[AcceptLanguage](#cfn-servicecatalog-launchroleconstraint-acceptlanguage)" : {{String}},
      "[Description](#cfn-servicecatalog-launchroleconstraint-description)" : {{String}},
      "[LocalRoleName](#cfn-servicecatalog-launchroleconstraint-localrolename)" : {{String}},
      "[PortfolioId](#cfn-servicecatalog-launchroleconstraint-portfolioid)" : {{String}},
      "[ProductId](#cfn-servicecatalog-launchroleconstraint-productid)" : {{String}},
      "[RoleArn](#cfn-servicecatalog-launchroleconstraint-rolearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-servicecatalog-launchroleconstraint-syntax.yaml"></a>

```
Type: AWS::ServiceCatalog::LaunchRoleConstraint
Properties:
  [AcceptLanguage](#cfn-servicecatalog-launchroleconstraint-acceptlanguage): {{String}}
  [Description](#cfn-servicecatalog-launchroleconstraint-description): {{String}}
  [LocalRoleName](#cfn-servicecatalog-launchroleconstraint-localrolename): {{String}}
  [PortfolioId](#cfn-servicecatalog-launchroleconstraint-portfolioid): {{String}}
  [ProductId](#cfn-servicecatalog-launchroleconstraint-productid): {{String}}
  [RoleArn](#cfn-servicecatalog-launchroleconstraint-rolearn): {{String}}
```

## Properties
<a name="aws-resource-servicecatalog-launchroleconstraint-properties"></a>

`AcceptLanguage`  <a name="cfn-servicecatalog-launchroleconstraint-acceptlanguage"></a>
The language code.
+ `jp` - Japanese
+ `zh` - Chinese
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-servicecatalog-launchroleconstraint-description"></a>
The description of the constraint.
*Required*: No
*Type*: String
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalRoleName`  <a name="cfn-servicecatalog-launchroleconstraint-localrolename"></a>
You are required to specify either the `RoleArn` or the `LocalRoleName` but can't use both.
If you specify the `LocalRoleName` property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.
The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortfolioId`  <a name="cfn-servicecatalog-launchroleconstraint-portfolioid"></a>
The portfolio identifier.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-]*`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProductId`  <a name="cfn-servicecatalog-launchroleconstraint-productid"></a>
The product identifier.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-]*`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-servicecatalog-launchroleconstraint-rolearn"></a>
The ARN of the launch role.
You are required to specify `RoleArn` or `LocalRoleName` but can't use both.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-cn|aws-us-gov):iam::[0-9]*:(role)\/.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-servicecatalog-launchroleconstraint-return-values"></a>

### Ref
<a name="aws-resource-servicecatalog-launchroleconstraint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns identifier of the constraint.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-servicecatalog-launchroleconstraint-return-values-fn--getatt"></a>

## See also
<a name="aws-resource-servicecatalog-launchroleconstraint--seealso"></a>
+ [CreateConstraint](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateConstraint.html) in the *AWS Service Catalog API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
