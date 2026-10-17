---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_RegistryMapping.html
---

# RegistryMapping
<a name="API_RegistryMapping"></a>

Maps an upstream container registry to a repository prefix in your Amazon Elastic Container Registry (Amazon ECR) private registry. For registries that Amazon ECR pull through cache supports, you create a pull through cache rule that synchronizes the upstream repositories with your private repositories. You can also use some registries that pull through cache doesn't support. For these registries, specify `credentialArn`, and AWS HealthOmics copies each image into a private Amazon ECR repository the first time a task needs it.

## Contents
<a name="API_RegistryMapping_Contents"></a>

 ** ecrRepositoryPrefix **   <a name="omics-Type-RegistryMapping-ecrRepositoryPrefix"></a>
The repository prefix to use in the ECR private repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** upstreamRegistryUrl **   <a name="omics-Type-RegistryMapping-upstreamRegistryUrl"></a>
The URI of the upstream registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** credentialArn **   <a name="omics-Type-RegistryMapping-credentialArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that holds the credentials for the upstream registry. You must specify this value when Amazon Elastic Container Registry (Amazon ECR) doesn't support pull through cache for the upstream registry. HealthOmics supports only some of these registries. The workflow role must have permission to call the `secretsmanager:GetSecretValue` operation on the secret. For more information about the supported registries, see [Container images](https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html) in the * AWS HealthOmics User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-\w+)*:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9\/_+=.@-]+`
Required: No

 ** ecrAccountId **   <a name="omics-Type-RegistryMapping-ecrAccountId"></a>
Account ID of the account that owns the upstream container image.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** upstreamRepositoryPrefix **   <a name="omics-Type-RegistryMapping-upstreamRepositoryPrefix"></a>
The repository prefix of the corresponding repository in the upstream registry.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_RegistryMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/RegistryMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/RegistryMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/RegistryMapping)
