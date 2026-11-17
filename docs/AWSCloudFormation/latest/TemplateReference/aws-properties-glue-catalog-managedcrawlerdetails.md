---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-managedcrawlerdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog ManagedCrawlerDetails
<a name="aws-properties-glue-catalog-managedcrawlerdetails"></a>

<a name="aws-properties-glue-catalog-managedcrawlerdetails-description"></a>The `ManagedCrawlerDetails` property type specifies Property description not available. for an [AWS::Glue::Catalog](aws-resource-glue-catalog.md).

## Syntax
<a name="aws-properties-glue-catalog-managedcrawlerdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-managedcrawlerdetails-syntax.json"></a>

```
{
  "[CrawlerArn](#cfn-glue-catalog-managedcrawlerdetails-crawlerarn)" : {{String}},
  "[Error](#cfn-glue-catalog-managedcrawlerdetails-error)" : {{ErrorDetail}},
  "[Status](#cfn-glue-catalog-managedcrawlerdetails-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-catalog-managedcrawlerdetails-syntax.yaml"></a>

```
  [CrawlerArn](#cfn-glue-catalog-managedcrawlerdetails-crawlerarn): {{String}}
  [Error](#cfn-glue-catalog-managedcrawlerdetails-error): {{
    ErrorDetail}}
  [Status](#cfn-glue-catalog-managedcrawlerdetails-status): {{String}}
```

## Properties
<a name="aws-properties-glue-catalog-managedcrawlerdetails-properties"></a>

`CrawlerArn`  <a name="cfn-glue-catalog-managedcrawlerdetails-crawlerarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Error`  <a name="cfn-glue-catalog-managedcrawlerdetails-error"></a>
Property description not available.
*Required*: No
*Type*: [ErrorDetail](aws-properties-glue-catalog-errordetail.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-glue-catalog-managedcrawlerdetails-status"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `PROVISIONING | PROVISIONED | FAILED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
