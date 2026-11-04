---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::CloudFormationProduct ProvisioningArtifactProperties
<a name="aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties"></a>

Information about a provisioning artifact (also known as a version) for a product.

## Syntax
<a name="aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties-syntax.json"></a>

```
{
  "[Description](#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-description)" : {{String}},
  "[DisableTemplateValidation](#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-disabletemplatevalidation)" : {{Boolean}},
  "[Info](#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-info)" : {{Info}},
  "[Name](#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-name)" : {{String}},
  "[Type](#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties-syntax.yaml"></a>

```
  [Description](#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-description): {{String}}
  [DisableTemplateValidation](#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-disabletemplatevalidation): {{Boolean}}
  [Info](#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-info): {{
    Info}}
  [Name](#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-name): {{String}}
  [Type](#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-type): {{String}}
```

## Properties
<a name="aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties-properties"></a>

`Description`  <a name="cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-description"></a>
The description of the provisioning artifact, including how it differs from the previous provisioning artifact.
*Required*: No
*Type*: String
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisableTemplateValidation`  <a name="cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-disabletemplatevalidation"></a>
If set to true, AWS Service Catalog stops validating the specified provisioning artifact even if it is invalid.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Info`  <a name="cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-info"></a>
The template source of the provisioning artifact. `Info` is an object that has one of the following keys, but not both. Each value is a string.
+ `LoadTemplateFromURL` - The URL of the AWS CloudFormation template in Amazon S3, for example `https://s3.amazonaws.com/amzn-s3-demo-bucket/sample-template.json`.
+ `ImportFromPhysicalId` - The Amazon Resource Name (ARN) of the CloudFormation stack that contains the template, for example `arn:aws:cloudformation:us-east-1:111122223333:stack/MyStack/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. AWS Service Catalog supports only CloudFormation stack ARNs.
*Required*: Yes
*Type*: [Info](aws-properties-servicecatalog-cloudformationproduct-info.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-name"></a>
The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.
When `ReplaceProvisioningArtifacts` is `false` (the default), CloudFormation matches the provisioning artifacts in your template to the product's existing provisioning artifacts by name and template URL. If you change the name or the template URL of a provisioning artifact, CloudFormation creates a provisioning artifact with a new ID and deletes the old one. The product itself isn't replaced. If the update fails partway, the product can have the old provisioning artifact, the new one, or both. For details, see the `ReplaceProvisioningArtifacts` property of the `AWS::ServiceCatalog::CloudFormationProduct` resource.
*Required*: No
*Type*: String
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-type"></a>
The type of provisioning artifact.
+ `CLOUD_FORMATION_TEMPLATE` - AWS CloudFormation template
+ `TERRAFORM_OPEN_SOURCE` - Terraform Open Source configuration file
+ `TERRAFORM_CLOUD` - Terraform Cloud configuration file
+ `EXTERNAL` - External configuration file
*Required*: No
*Type*: String
*Allowed values*: `CLOUD_FORMATION_TEMPLATE | MARKETPLACE_AMI | MARKETPLACE_CAR | TERRAFORM_OPEN_SOURCE | TERRAFORM_CLOUD | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties--examples"></a>

### Example - Specify the template of a provisioning artifact
<a name="aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties--examples--Example_-_Specify_the_template_of_a_provisioning_artifact"></a>

`Info` is an object, not a string. The following example specifies a provisioning artifact whose template is loaded from Amazon S3.

#### JSON
<a name="aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties--examples--Example_-_Specify_the_template_of_a_provisioning_artifact--json"></a>

```
{
    "Name": "v2",
    "Description": "Adds an output for the bucket name",
    "Type": "CLOUD_FORMATION_TEMPLATE",
    "Info": {
        "LoadTemplateFromURL": "https://s3.amazonaws.com/amzn-s3-demo-bucket/sample-template-v2.json"
    }
}
```

#### YAML
<a name="aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties--examples--Example_-_Specify_the_template_of_a_provisioning_artifact--yaml"></a>

```
Name: v2
Description: Adds an output for the bucket name
Type: CLOUD_FORMATION_TEMPLATE
Info:
  LoadTemplateFromURL: https://s3.amazonaws.com/amzn-s3-demo-bucket/sample-template-v2.json
```

## See also
<a name="aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties--seealso"></a>
+ [ProvisioningArtifactProperties](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifactProperties.html) in the *AWS Service Catalog API Reference*
