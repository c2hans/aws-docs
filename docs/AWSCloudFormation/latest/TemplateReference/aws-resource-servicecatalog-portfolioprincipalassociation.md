---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicecatalog-portfolioprincipalassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::PortfolioPrincipalAssociation
<a name="aws-resource-servicecatalog-portfolioprincipalassociation"></a>

Associates the Amazon Resource Name (ARN) of the specified principal with the specified portfolio.

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
The ARN of the principal (IAM user, role, or group). The ARN format depends on the value of `PrincipalType`, as follows:
+ `IAM` - A full ARN, in the format `arn:partition:iam::account-id:resource-type/resource-id`, for example `arn:aws:iam::444455556666:role/Admin`.
+ `IAM_PATTERN` - An ARN without the account ID, in the format `arn:partition:iam:::resource-type/resource-id`, for example `arn:aws:iam:::role/Admin`.
With `IAM_PATTERN`, the path and name in the resource ID can contain the wildcard characters `*`, which matches any number of characters, and `?`, which matches zero or one character, for example `arn:aws:iam:::role/MyTeam-*`. Wildcards can't replace the resource type (`user`, `group`, or `role`). You can associate an `IAM_PATTERN` ARN even if no principal with that name exists.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-cn|aws-us-gov):iam::[0-9]*:(role|user|group)\/.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrincipalType`  <a name="cfn-servicecatalog-portfolioprincipalassociation-principaltype"></a>
The principal type. Specify `IAM` to associate a principal by its full ARN, or `IAM_PATTERN` to associate principals by an ARN that has no account ID and can contain wildcard characters. You can associate up to 10 principals of type `IAM_PATTERN` with a portfolio. For the ARN formats, see `PrincipalARN`.
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

## Examples
<a name="aws-resource-servicecatalog-portfolioprincipalassociation--examples"></a>

**Topics**
+ [Example - Associate an IAM role with a portfolio](#aws-resource-servicecatalog-portfolioprincipalassociation--examples--Example_-_Associate_an_IAM_role_with_a_portfolio)
+ [Example - Associate IAM roles by name pattern](#aws-resource-servicecatalog-portfolioprincipalassociation--examples--Example_-_Associate_IAM_roles_by_name_pattern)

### Example - Associate an IAM role with a portfolio
<a name="aws-resource-servicecatalog-portfolioprincipalassociation--examples--Example_-_Associate_an_IAM_role_with_a_portfolio"></a>

The following example gives the IAM role `MyRole` in the current account access to the portfolio `MyPortfolio`, which is declared elsewhere in the same template.

#### JSON
<a name="aws-resource-servicecatalog-portfolioprincipalassociation--examples--Example_-_Associate_an_IAM_role_with_a_portfolio--json"></a>

```
{
    "MyPrincipalAssociation": {
        "Type": "AWS::ServiceCatalog::PortfolioPrincipalAssociation",
        "Properties": {
            "PortfolioId": { "Ref": "MyPortfolio" },
            "PrincipalType": "IAM",
            "PrincipalARN": { "Fn::Sub": "arn:${AWS::Partition}:iam::${AWS::AccountId}:role/MyRole" }
        }
    }
}
```

#### YAML
<a name="aws-resource-servicecatalog-portfolioprincipalassociation--examples--Example_-_Associate_an_IAM_role_with_a_portfolio--yaml"></a>

```
MyPrincipalAssociation:
  Type: AWS::ServiceCatalog::PortfolioPrincipalAssociation
  Properties:
    PortfolioId: !Ref MyPortfolio
    PrincipalType: IAM
    PrincipalARN: !Sub arn:${AWS::Partition}:iam::${AWS::AccountId}:role/MyRole
```

### Example - Associate IAM roles by name pattern
<a name="aws-resource-servicecatalog-portfolioprincipalassociation--examples--Example_-_Associate_IAM_roles_by_name_pattern"></a>

The following example gives the IAM roles that have the default path (`/`) and whose names start with `MyTeam-` access to the portfolio. With `IAM_PATTERN`, the ARN has no account ID and can contain wildcard characters. AWS Service Catalog matches the pattern against both the path and the name of a role. For example, this pattern doesn't match a role named `MyTeam-Dev` that has the path `/teams/`. To include roles under other paths, also associate a pattern such as `arn:aws:iam:::role/*/MyTeam-*`.

#### JSON
<a name="aws-resource-servicecatalog-portfolioprincipalassociation--examples--Example_-_Associate_IAM_roles_by_name_pattern--json"></a>

```
{
    "MyPatternAssociation": {
        "Type": "AWS::ServiceCatalog::PortfolioPrincipalAssociation",
        "Properties": {
            "PortfolioId": { "Ref": "MyPortfolio" },
            "PrincipalType": "IAM_PATTERN",
            "PrincipalARN": { "Fn::Sub": "arn:${AWS::Partition}:iam:::role/MyTeam-*" }
        }
    }
}
```

#### YAML
<a name="aws-resource-servicecatalog-portfolioprincipalassociation--examples--Example_-_Associate_IAM_roles_by_name_pattern--yaml"></a>

```
MyPatternAssociation:
  Type: AWS::ServiceCatalog::PortfolioPrincipalAssociation
  Properties:
    PortfolioId: !Ref MyPortfolio
    PrincipalType: IAM_PATTERN
    PrincipalARN: !Sub arn:${AWS::Partition}:iam:::role/MyTeam-*
```

## See also
<a name="aws-resource-servicecatalog-portfolioprincipalassociation--seealso"></a>
+ [AssociatePrincipalWithPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociatePrincipalWithPortfolio.html) in the *AWS Service Catalog API Reference*
