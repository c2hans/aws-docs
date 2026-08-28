---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicecatalog-portfolioprincipalassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::PortfolioPrincipalAssociation
<a name="aws-resource-servicecatalog-portfolioprincipalassociation"></a>

Associates the specified principal ARN with the specified portfolio.

## Syntax
<a name="aws-resource-servicecatalog-portfolioprincipalassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-servicecatalog-portfolioprincipalassociation-syntax.json"></a>

```
{
  "Type" : "AWS::ServiceCatalog::PortfolioPrincipalAssociation",
  "Properties" : {
      "[AcceptLanguage](#cfn-servicecatalog-portfolioprincipalassociation-acceptlanguage)" : {{String}},
      "[PortfolioId](#cfn-servicecatalog-portfolioprincipalassociation-portfolioid)" : {{String}},
      "[PrincipalARN](#cfn-servicecatalog-portfolioprincipalassociation-principalarn)" : {{String}},
      "[PrincipalType](#cfn-servicecatalog-portfolioprincipalassociation-principaltype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-servicecatalog-portfolioprincipalassociation-syntax.yaml"></a>

```
Type: AWS::ServiceCatalog::PortfolioPrincipalAssociation
Properties:
  [AcceptLanguage](#cfn-servicecatalog-portfolioprincipalassociation-acceptlanguage): {{String}}
  [PortfolioId](#cfn-servicecatalog-portfolioprincipalassociation-portfolioid): {{String}}
  [PrincipalARN](#cfn-servicecatalog-portfolioprincipalassociation-principalarn): {{String}}
  [PrincipalType](#cfn-servicecatalog-portfolioprincipalassociation-principaltype): {{String}}
```

## Properties
<a name="aws-resource-servicecatalog-portfolioprincipalassociation-properties"></a>

`AcceptLanguage`  <a name="cfn-servicecatalog-portfolioprincipalassociation-acceptlanguage"></a>
The language code.
+ `jp` - Japanese
+ `zh` - Chinese
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PortfolioId`  <a name="cfn-servicecatalog-portfolioprincipalassociation-portfolioid"></a>
The portfolio identifier.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-]*`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrincipalARN`  <a name="cfn-servicecatalog-portfolioprincipalassociation-principalarn"></a>
The ARN of the principal (IAM user, role, or group).
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-cn|aws-us-gov):iam::[0-9]*:(role|user|group)\/.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrincipalType`  <a name="cfn-servicecatalog-portfolioprincipalassociation-principaltype"></a>
The principal type. The supported values are `IAM` and `IAM_PATTERN`.
*Required*: Yes
*Type*: String
*Allowed values*: `IAM | IAM_PATTERN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-servicecatalog-portfolioprincipalassociation-return-values"></a>

### Ref
<a name="aws-resource-servicecatalog-portfolioprincipalassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a unique identifier for the association.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also
<a name="aws-resource-servicecatalog-portfolioprincipalassociation--seealso"></a>
+ [AssociatePrincipalWithPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociatePrincipalWithPortfolio.html) in the *AWS Service Catalog API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
