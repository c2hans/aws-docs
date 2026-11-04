---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-servicecatalog-cloudformationproduct-info.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::CloudFormationProduct Info
<a name="aws-properties-servicecatalog-cloudformationproduct-info"></a>

The template source of a provisioning artifact. Specify one of the following keys, but not both.

## Syntax
<a name="aws-properties-servicecatalog-cloudformationproduct-info-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-servicecatalog-cloudformationproduct-info-syntax.json"></a>

```
{
  "[ImportFromPhysicalId](#cfn-servicecatalog-cloudformationproduct-info-importfromphysicalid)" : {{String}},
  "[LoadTemplateFromURL](#cfn-servicecatalog-cloudformationproduct-info-loadtemplatefromurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-servicecatalog-cloudformationproduct-info-syntax.yaml"></a>

```
  [ImportFromPhysicalId](#cfn-servicecatalog-cloudformationproduct-info-importfromphysicalid): {{String}}
  [LoadTemplateFromURL](#cfn-servicecatalog-cloudformationproduct-info-loadtemplatefromurl): {{String}}
```

## Properties
<a name="aws-properties-servicecatalog-cloudformationproduct-info-properties"></a>

`ImportFromPhysicalId`  <a name="cfn-servicecatalog-cloudformationproduct-info-importfromphysicalid"></a>
The Amazon Resource Name (ARN) of the CloudFormation stack that contains the template, for example `arn:aws:cloudformation:us-east-1:111122223333:stack/MyStack/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. AWS Service Catalog supports only CloudFormation stack ARNs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoadTemplateFromURL`  <a name="cfn-servicecatalog-cloudformationproduct-info-loadtemplatefromurl"></a>
The URL of the AWS CloudFormation template in Amazon S3, for example `https://s3.amazonaws.com/amzn-s3-demo-bucket/sample-template.json`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
