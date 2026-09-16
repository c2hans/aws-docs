---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kendra-featuredresultsset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::FeaturedResultsSet
<a name="aws-resource-kendra-featuredresultsset"></a>

Creates a set of featured results to display at the top of the search results page. Featured results are placed above all other results for certain queries. You map specific queries to specific documents for featuring in the results. If a query contains an exact match, then one or more specific documents are featured in the search results.

## Syntax
<a name="aws-resource-kendra-featuredresultsset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kendra-featuredresultsset-syntax.json"></a>

```
{
  "Type" : "AWS::Kendra::FeaturedResultsSet",
  "Properties" : {
      "[Description](#cfn-kendra-featuredresultsset-description)" : {{String}},
      "[FeaturedDocuments](#cfn-kendra-featuredresultsset-featureddocuments)" : {{[ FeaturedDocument, ... ]}},
      "[FeaturedResultsSetName](#cfn-kendra-featuredresultsset-featuredresultssetname)" : {{String}},
      "[IndexId](#cfn-kendra-featuredresultsset-indexid)" : {{String}},
      "[QueryTexts](#cfn-kendra-featuredresultsset-querytexts)" : {{[ String, ... ]}},
      "[Status](#cfn-kendra-featuredresultsset-status)" : {{String}},
      "[Tags](#cfn-kendra-featuredresultsset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kendra-featuredresultsset-syntax.yaml"></a>

```
Type: AWS::Kendra::FeaturedResultsSet
Properties:
  [Description](#cfn-kendra-featuredresultsset-description): {{String}}
  [FeaturedDocuments](#cfn-kendra-featuredresultsset-featureddocuments): {{
    - FeaturedDocument}}
  [FeaturedResultsSetName](#cfn-kendra-featuredresultsset-featuredresultssetname): {{String}}
  [IndexId](#cfn-kendra-featuredresultsset-indexid): {{String}}
  [QueryTexts](#cfn-kendra-featuredresultsset-querytexts): {{
    - String}}
  [Status](#cfn-kendra-featuredresultsset-status): {{String}}
  [Tags](#cfn-kendra-featuredresultsset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kendra-featuredresultsset-properties"></a>

`Description`  <a name="cfn-kendra-featuredresultsset-description"></a>
A description for the set of featured results.
*Required*: No
*Type*: String
*Pattern*: `^\P{C}*$`
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FeaturedDocuments`  <a name="cfn-kendra-featuredresultsset-featureddocuments"></a>
A list of document IDs for the documents you want to feature at the top of the search results page.
*Required*: No
*Type*: Array of [FeaturedDocument](aws-properties-kendra-featuredresultsset-featureddocument.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FeaturedResultsSetName`  <a name="cfn-kendra-featuredresultsset-featuredresultssetname"></a>
A name for the set of featured results.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][ a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexId`  <a name="cfn-kendra-featuredresultsset-indexid"></a>
The identifier of the index that you want to use for featuring results.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]*$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueryTexts`  <a name="cfn-kendra-featuredresultsset-querytexts"></a>
A list of queries for featuring results.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `49`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-kendra-featuredresultsset-status"></a>
The current status of the set of featured results. When the value is `ACTIVE`, featured results are ready for use. You can still configure your settings before setting the status to `ACTIVE`. The queries you specify for featured results must be unique per featured results set for each index, whether the status is `ACTIVE` or `INACTIVE`.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | INACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-kendra-featuredresultsset-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-kendra-featuredresultsset-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kendra-featuredresultsset-return-values"></a>

### Ref
<a name="aws-resource-kendra-featuredresultsset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the features results set ID. For example:

 `{"Ref": "featured-results-set-id"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-kendra-featuredresultsset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-kendra-featuredresultsset-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`FeaturedResultsSetId`  <a name="FeaturedResultsSetId-fn::getatt"></a>
The identifier of the set of featured results.
