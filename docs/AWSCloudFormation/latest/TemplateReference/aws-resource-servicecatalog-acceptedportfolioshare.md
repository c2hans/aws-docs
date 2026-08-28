---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicecatalog-acceptedportfolioshare.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::AcceptedPortfolioShare
<a name="aws-resource-servicecatalog-acceptedportfolioshare"></a>

Accepts an offer to share the specified portfolio.

## Syntax
<a name="aws-resource-servicecatalog-acceptedportfolioshare-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-servicecatalog-acceptedportfolioshare-syntax.json"></a>

```
{
  "Type" : "AWS::ServiceCatalog::AcceptedPortfolioShare",
  "Properties" : {
      "[AcceptLanguage](#cfn-servicecatalog-acceptedportfolioshare-acceptlanguage)" : {{String}},
      "[PortfolioId](#cfn-servicecatalog-acceptedportfolioshare-portfolioid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-servicecatalog-acceptedportfolioshare-syntax.yaml"></a>

```
Type: AWS::ServiceCatalog::AcceptedPortfolioShare
Properties:
  [AcceptLanguage](#cfn-servicecatalog-acceptedportfolioshare-acceptlanguage): {{String}}
  [PortfolioId](#cfn-servicecatalog-acceptedportfolioshare-portfolioid): {{String}}
```

## Properties
<a name="aws-resource-servicecatalog-acceptedportfolioshare-properties"></a>

`AcceptLanguage`  <a name="cfn-servicecatalog-acceptedportfolioshare-acceptlanguage"></a>
The language code.
+ `jp` - Japanese
+ `zh` - Chinese
*Required*: No
*Type*: String
*Pattern*: `^(en|jp|zh)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PortfolioId`  <a name="cfn-servicecatalog-acceptedportfolioshare-portfolioid"></a>
The portfolio identifier.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-servicecatalog-acceptedportfolioshare-return-values"></a>

### Ref
<a name="aws-resource-servicecatalog-acceptedportfolioshare-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a unique identifier.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also
<a name="aws-resource-servicecatalog-acceptedportfolioshare--seealso"></a>
+ [AcceptPortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AcceptPortfolioShare.html) in the *AWS Service Catalog API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
