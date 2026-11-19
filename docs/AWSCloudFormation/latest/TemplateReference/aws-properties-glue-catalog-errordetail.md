---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-errordetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog ErrorDetail

Contains details about an error.

## Syntax
<a name="aws-properties-glue-catalog-errordetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-errordetail-syntax.json"></a>

```
{
  "[ErrorCode](#cfn-glue-catalog-errordetail-errorcode)" : {{String}},
  "[ErrorMessage](#cfn-glue-catalog-errordetail-errormessage)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-catalog-errordetail-syntax.yaml"></a>

```
  [ErrorCode](#cfn-glue-catalog-errordetail-errorcode): {{String}}
  [ErrorMessage](#cfn-glue-catalog-errordetail-errormessage): {{String}}
```

## Properties
<a name="aws-properties-glue-catalog-errordetail-properties"></a>

`ErrorCode`  <a name="cfn-glue-catalog-errordetail-errorcode"></a>
The code associated with this error.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ErrorMessage`  <a name="cfn-glue-catalog-errordetail-errormessage"></a>
A message describing the error.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
