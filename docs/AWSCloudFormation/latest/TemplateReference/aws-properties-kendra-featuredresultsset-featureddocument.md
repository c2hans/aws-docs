---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-featuredresultsset-featureddocument.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::FeaturedResultsSet FeaturedDocument
<a name="aws-properties-kendra-featuredresultsset-featureddocument"></a>

A featured document. This document is displayed at the top of the search results page, placed above all other results for certain queries. If there's an exact match of a query, then the document is featured in the search results.

## Syntax
<a name="aws-properties-kendra-featuredresultsset-featureddocument-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-featuredresultsset-featureddocument-syntax.json"></a>

```
{
  "[Id](#cfn-kendra-featuredresultsset-featureddocument-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-kendra-featuredresultsset-featureddocument-syntax.yaml"></a>

```
  [Id](#cfn-kendra-featuredresultsset-featureddocument-id): {{String}}
```

## Properties
<a name="aws-properties-kendra-featuredresultsset-featureddocument-properties"></a>

`Id`  <a name="cfn-kendra-featuredresultsset-featureddocument-id"></a>
The identifier of the document to feature in the search results.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
