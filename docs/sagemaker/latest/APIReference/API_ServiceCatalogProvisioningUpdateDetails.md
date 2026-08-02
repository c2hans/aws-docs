---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ServiceCatalogProvisioningUpdateDetails.html
---

# ServiceCatalogProvisioningUpdateDetails
<a name="API_ServiceCatalogProvisioningUpdateDetails"></a>

Details that you specify to provision a service catalog product. For information about service catalog, see [What is AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).

## Contents
<a name="API_ServiceCatalogProvisioningUpdateDetails_Contents"></a>

 ** ProvisioningArtifactId **   <a name="sagemaker-Type-ServiceCatalogProvisioningUpdateDetails-ProvisioningArtifactId"></a>
The ID of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisioningParameters **   <a name="sagemaker-Type-ServiceCatalogProvisioningUpdateDetails-ProvisioningParameters"></a>
A list of key value pairs that you specify when you provision a product.
Type: Array of [ProvisioningParameter](API_ProvisioningParameter.md) objects
Required: No

## See Also
<a name="API_ServiceCatalogProvisioningUpdateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ServiceCatalogProvisioningUpdateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ServiceCatalogProvisioningUpdateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ServiceCatalogProvisioningUpdateDetails)
