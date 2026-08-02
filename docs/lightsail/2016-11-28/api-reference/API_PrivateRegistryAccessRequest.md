---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_PrivateRegistryAccessRequest.html
---

# PrivateRegistryAccessRequest
<a name="API_PrivateRegistryAccessRequest"></a>

Describes a request to configure an Amazon Lightsail container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.

For more information, see [Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access) in the *Amazon Lightsail Developer Guide*.

## Contents
<a name="API_PrivateRegistryAccessRequest_Contents"></a>

 ** ecrImagePullerRole **   <a name="Lightsail-Type-PrivateRegistryAccessRequest-ecrImagePullerRole"></a>
An object to describe a request to activate or deactivate the role that you can use to grant an Amazon Lightsail container service access to Amazon Elastic Container Registry (Amazon ECR) private repositories.
Type: [ContainerServiceECRImagePullerRoleRequest](API_ContainerServiceECRImagePullerRoleRequest.md) object
Required: No

## See Also
<a name="API_PrivateRegistryAccessRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/PrivateRegistryAccessRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/PrivateRegistryAccessRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/PrivateRegistryAccessRequest)
