---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ServiceCatalogProvisioningDetails.html
---

# ServiceCatalogProvisioningDetails
<a name="API_ServiceCatalogProvisioningDetails"></a>

Details that you specify to provision a service catalog product. For information about service catalog, see [What is AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).

## Contents
<a name="API_ServiceCatalogProvisioningDetails_Contents"></a>

 ** ProductId **   <a name="sagemaker-Type-ServiceCatalogProvisioningDetails-ProductId"></a>
The ID of the product to provision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_\-]*`
Required: Yes

 ** PathId **   <a name="sagemaker-Type-ServiceCatalogProvisioningDetails-PathId"></a>
The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisioningArtifactId **   <a name="sagemaker-Type-ServiceCatalogProvisioningDetails-ProvisioningArtifactId"></a>
The ID of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisioningParameters **   <a name="sagemaker-Type-ServiceCatalogProvisioningDetails-ProvisioningParameters"></a>
A list of key value pairs that you specify when you provision a product.
Type: Array of [ProvisioningParameter](API_ProvisioningParameter.md) objects
Required: No

## See Also
<a name="API_ServiceCatalogProvisioningDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ServiceCatalogProvisioningDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ServiceCatalogProvisioningDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ServiceCatalogProvisioningDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
