---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicecatalog-portfolio.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::Portfolio
<a name="aws-resource-servicecatalog-portfolio"></a>

Specifies a portfolio.

## Syntax
<a name="aws-resource-servicecatalog-portfolio-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-servicecatalog-portfolio-syntax.json"></a>

```
{
  "Type" : "AWS::ServiceCatalog::Portfolio",
  "Properties" : {
      "[AcceptLanguage](#cfn-servicecatalog-portfolio-acceptlanguage)" : {{String}},
      "[Description](#cfn-servicecatalog-portfolio-description)" : {{String}},
      "[DisplayName](#cfn-servicecatalog-portfolio-displayname)" : {{String}},
      "[ProviderName](#cfn-servicecatalog-portfolio-providername)" : {{String}},
      "[Tags](#cfn-servicecatalog-portfolio-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-servicecatalog-portfolio-syntax.yaml"></a>

```
Type: AWS::ServiceCatalog::Portfolio
Properties:
  [AcceptLanguage](#cfn-servicecatalog-portfolio-acceptlanguage): {{String}}
  [Description](#cfn-servicecatalog-portfolio-description): {{String}}
  [DisplayName](#cfn-servicecatalog-portfolio-displayname): {{String}}
  [ProviderName](#cfn-servicecatalog-portfolio-providername): {{String}}
  [Tags](#cfn-servicecatalog-portfolio-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-servicecatalog-portfolio-properties"></a>

`AcceptLanguage`  <a name="cfn-servicecatalog-portfolio-acceptlanguage"></a>
The language code.
+ `jp` - Japanese
+ `zh` - Chinese
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-servicecatalog-portfolio-description"></a>
The description of the portfolio.
*Required*: No
*Type*: String
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-servicecatalog-portfolio-displayname"></a>
The name to use for display purposes.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderName`  <a name="cfn-servicecatalog-portfolio-providername"></a>
The name of the portfolio provider.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-servicecatalog-portfolio-tags"></a>
One or more tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-servicecatalog-portfolio-tag.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-servicecatalog-portfolio-return-values"></a>

### Ref
<a name="aws-resource-servicecatalog-portfolio-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the portfolio identifier.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-servicecatalog-portfolio-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-servicecatalog-portfolio-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The portfolio identifier.

`PortfolioName`  <a name="PortfolioName-fn::getatt"></a>
The name of the portfolio.

## See also
<a name="aws-resource-servicecatalog-portfolio--seealso"></a>
+ [CreatePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreatePortfolio.html) in the *AWS Service Catalog API Reference*
