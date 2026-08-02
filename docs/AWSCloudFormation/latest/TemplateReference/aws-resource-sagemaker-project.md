---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-project.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Project
<a name="aws-resource-sagemaker-project"></a>

Creates a machine learning (ML) project that can contain one or more templates that set up an ML pipeline from training to deploying an approved model.

## Syntax
<a name="aws-resource-sagemaker-project-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-project-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Project",
  "Properties" : {
      "[ProjectDescription](#cfn-sagemaker-project-projectdescription)" : {{String}},
      "[ProjectName](#cfn-sagemaker-project-projectname)" : {{String}},
      "[ServiceCatalogProvisionedProductDetails](#cfn-sagemaker-project-servicecatalogprovisionedproductdetails)" : {{ServiceCatalogProvisionedProductDetails}},
      "[ServiceCatalogProvisioningDetails](#cfn-sagemaker-project-servicecatalogprovisioningdetails)" : {{ServiceCatalogProvisioningDetails}},
      "[Tags](#cfn-sagemaker-project-tags)" : {{[ Tag, ... ]}},
      "[TemplateProviderDetails](#cfn-sagemaker-project-templateproviderdetails)" : {{[ TemplateProviderDetail, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-project-syntax.yaml"></a>

```
Type: AWS::SageMaker::Project
Properties:
  [ProjectDescription](#cfn-sagemaker-project-projectdescription): {{String}}
  [ProjectName](#cfn-sagemaker-project-projectname): {{String}}
  [ServiceCatalogProvisionedProductDetails](#cfn-sagemaker-project-servicecatalogprovisionedproductdetails): {{
    ServiceCatalogProvisionedProductDetails}}
  [ServiceCatalogProvisioningDetails](#cfn-sagemaker-project-servicecatalogprovisioningdetails): {{
    ServiceCatalogProvisioningDetails}}
  [Tags](#cfn-sagemaker-project-tags): {{
    - Tag}}
  [TemplateProviderDetails](#cfn-sagemaker-project-templateproviderdetails): {{
    - TemplateProviderDetail}}
```

## Properties
<a name="aws-resource-sagemaker-project-properties"></a>

`ProjectDescription`  <a name="cfn-sagemaker-project-projectdescription"></a>
The description of the project.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectName`  <a name="cfn-sagemaker-project-projectname"></a>
The name of the project.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceCatalogProvisionedProductDetails`  <a name="cfn-sagemaker-project-servicecatalogprovisionedproductdetails"></a>
Details of a provisioned service catalog product. For information about service catalog, see [What is AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).
*Required*: No
*Type*: [ServiceCatalogProvisionedProductDetails](aws-properties-sagemaker-project-servicecatalogprovisionedproductdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceCatalogProvisioningDetails`  <a name="cfn-sagemaker-project-servicecatalogprovisioningdetails"></a>
The product ID and provisioning artifact ID to provision a service catalog. For information, see [What is AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).
*Required*: No
*Type*: [ServiceCatalogProvisioningDetails](aws-properties-sagemaker-project-servicecatalogprovisioningdetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-project-tags"></a>
A list of key-value pairs to apply to this resource.
For more information, see [Resource Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) and [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what) in the *AWS Billing and Cost Management User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-project-tag.md)
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TemplateProviderDetails`  <a name="cfn-sagemaker-project-templateproviderdetails"></a>
 An array of template providers associated with the project.
*Required*: No
*Type*: Array of [TemplateProviderDetail](aws-properties-sagemaker-project-templateproviderdetail.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-project-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-project-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the Project.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-project-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-project-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time that the project was created.

`ProjectArn`  <a name="ProjectArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the project.

`ProjectId`  <a name="ProjectId-fn::getatt"></a>
The ID of the project. This ID is prepended to all entities associated with this project.

`ProjectStatus`  <a name="ProjectStatus-fn::getatt"></a>
The status of the project.

## Examples
<a name="aws-resource-sagemaker-project--examples"></a>

### SageMaker Project Example
<a name="aws-resource-sagemaker-project--examples--SageMaker_Project_Example"></a>

The following example creates a SageMaker Project.

#### JSON
<a name="aws-resource-sagemaker-project--examples--SageMaker_Project_Example--json"></a>

```
{
   "Description": "AWS SageMaker Project basic template",
   "Resources": {
      "SampleProject": {
         "Type": "AWS::SageMaker::Project",
         "Properties": {
            "ProjectName": "project1",
            "ProjectDescription": "Project Description",
            "ServiceCatalogProvisioningDetails": {
               "ProductId": "prod-53ibyqbj2cgmo",
               "ProvisioningArtifactId": "pa-sm4pjfuzictpe"
            }
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-sagemaker-project--examples--SageMaker_Project_Example--yaml"></a>

```
---
Description: AWS SageMaker Project basic template

Resources:

  SampleProject:
    Type: AWS::SageMaker::Project
    Properties:
      ProjectName: "SampleProject"
      ProjectDescription: "Project Description"
      ServiceCatalogProvisioningDetails:
        ProductId: "prod-53ibyqbj2cgmo"
        ProvisioningArtifactId: "pa-sm4pjfuzictpe"
```
