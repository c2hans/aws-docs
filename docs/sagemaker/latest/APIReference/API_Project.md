---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Project.html
---

# Project
<a name="API_Project"></a>

The properties of a project as returned by the Search API.

## Contents
<a name="API_Project_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-Project-CreatedBy"></a>
Who created the project.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-Project-CreationTime"></a>
A timestamp specifying when the project was created.
Type: Timestamp
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-Project-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-Project-LastModifiedTime"></a>
A timestamp container for when the project was last modified.
Type: Timestamp
Required: No

 ** ProjectArn **   <a name="sagemaker-Type-Project-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:project/[\S]{1,2048}`
Required: No

 ** ProjectDescription **   <a name="sagemaker-Type-Project-ProjectDescription"></a>
The description of the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** ProjectId **   <a name="sagemaker-Type-Project-ProjectId"></a>
The ID of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** ProjectName **   <a name="sagemaker-Type-Project-ProjectName"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: No

 ** ProjectStatus **   <a name="sagemaker-Type-Project-ProjectStatus"></a>
The status of the project.
Type: String
Valid Values: `Pending | CreateInProgress | CreateCompleted | CreateFailed | DeleteInProgress | DeleteFailed | DeleteCompleted | UpdateInProgress | UpdateCompleted | UpdateFailed`
Required: No

 ** ServiceCatalogProvisionedProductDetails **   <a name="sagemaker-Type-Project-ServiceCatalogProvisionedProductDetails"></a>
Details of a provisioned service catalog product. For information about service catalog, see [What is AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).
Type: [ServiceCatalogProvisionedProductDetails](API_ServiceCatalogProvisionedProductDetails.md) object
Required: No

 ** ServiceCatalogProvisioningDetails **   <a name="sagemaker-Type-Project-ServiceCatalogProvisioningDetails"></a>
Details that you specify to provision a service catalog product. For information about service catalog, see [What is AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).
Type: [ServiceCatalogProvisioningDetails](API_ServiceCatalogProvisioningDetails.md) object
Required: No

 ** Tags **   <a name="sagemaker-Type-Project-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** TemplateProviderDetails **   <a name="sagemaker-Type-Project-TemplateProviderDetails"></a>
 An array of template providers associated with the project.
Type: Array of [TemplateProviderDetail](API_TemplateProviderDetail.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_Project_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Project)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Project)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Project)
