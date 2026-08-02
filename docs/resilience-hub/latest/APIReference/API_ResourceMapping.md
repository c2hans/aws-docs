---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ResourceMapping.html
---

# ResourceMapping
<a name="API_ResourceMapping"></a>

Defines a resource mapping.

## Contents
<a name="API_ResourceMapping_Contents"></a>

 ** mappingType **   <a name="resiliencehub-Type-ResourceMapping-mappingType"></a>
Specifies the type of resource mapping.
Type: String
Valid Values: `CfnStack | Resource | AppRegistryApp | ResourceGroup | Terraform | EKS`
Required: Yes

 ** physicalResourceId **   <a name="resiliencehub-Type-ResourceMapping-physicalResourceId"></a>
Identifier of the physical resource.
Type: [PhysicalResourceId](API_PhysicalResourceId.md) object
Required: Yes

 ** appRegistryAppName **   <a name="resiliencehub-Type-ResourceMapping-appRegistryAppName"></a>
Name of the application this resource is mapped to when the `mappingType` is `AppRegistryApp`.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** eksSourceName **   <a name="resiliencehub-Type-ResourceMapping-eksSourceName"></a>
Name of the Amazon Elastic Kubernetes Service cluster and namespace that this resource is mapped to when the `mappingType` is `EKS`.
This parameter accepts values in "eks-cluster/namespace" format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** logicalStackName **   <a name="resiliencehub-Type-ResourceMapping-logicalStackName"></a>
Name of the CloudFormation stack this resource is mapped to when the `mappingType` is `CfnStack`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** resourceGroupName **   <a name="resiliencehub-Type-ResourceMapping-resourceGroupName"></a>
Name of the AWS Resource Groups that this resource is mapped to when the `mappingType` is `ResourceGroup`.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** resourceName **   <a name="resiliencehub-Type-ResourceMapping-resourceName"></a>
Name of the resource that this resource is mapped to when the `mappingType` is `Resource`.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** terraformSourceName **   <a name="resiliencehub-Type-ResourceMapping-terraformSourceName"></a>
Name of the Terraform source that this resource is mapped to when the `mappingType` is `Terraform`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ResourceMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ResourceMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ResourceMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ResourceMapping)
