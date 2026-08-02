---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ContainerRegistryMap.html
---

# ContainerRegistryMap
<a name="API_ContainerRegistryMap"></a>

Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see [Container images](https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html) in the * AWS HealthOmics User Guide*.

## Contents
<a name="API_ContainerRegistryMap_Contents"></a>

 ** imageMappings **   <a name="omics-Type-ContainerRegistryMap-imageMappings"></a>
Image mappings specify path mappings between the ECR private repository and their corresponding external repositories.
Type: Array of [ImageMapping](API_ImageMapping.md) objects
Required: No

 ** registryMappings **   <a name="omics-Type-ContainerRegistryMap-registryMappings"></a>
Mapping that provides the ECR repository path where upstream container images are pulled and synchronized.
Type: Array of [RegistryMapping](API_RegistryMapping.md) objects
Required: No

## See Also
<a name="API_ContainerRegistryMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ContainerRegistryMap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ContainerRegistryMap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ContainerRegistryMap)
