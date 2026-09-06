---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_RegistryAlias.html
---

# RegistryAlias
<a name="API_RegistryAlias"></a>

An object representing the aliases for a public registry. A public registry is given an alias when it's created. However, a custom alias can be set using the Amazon ECR console. For more information, see [Public registries](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registries.html) in the *Amazon Elastic Container Registry Public User Guide*.

## Contents
<a name="API_RegistryAlias_Contents"></a>

 ** defaultRegistryAlias **   <a name="ecrpublic-Type-RegistryAlias-defaultRegistryAlias"></a>
Indicates whether the registry alias is the default alias for the registry. When the first public repository is created, your public registry is assigned a default registry alias.
Type: Boolean
Required: Yes

 ** name **   <a name="ecrpublic-Type-RegistryAlias-name"></a>
The name of the registry alias.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

 ** primaryRegistryAlias **   <a name="ecrpublic-Type-RegistryAlias-primaryRegistryAlias"></a>
Indicates whether the registry alias is the primary alias for the registry. If true, the alias is the primary registry alias and is displayed in both the repository URL and the image URI used in the `docker pull` commands on the Amazon ECR Public Gallery.
A registry alias that isn't the primary registry alias can be used in the repository URI in a `docker pull` command.
Type: Boolean
Required: Yes

 ** status **   <a name="ecrpublic-Type-RegistryAlias-status"></a>
The status of the registry alias.
Type: String
Valid Values: `ACTIVE | PENDING | REJECTED`
Required: Yes

## See Also
<a name="API_RegistryAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/RegistryAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/RegistryAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/RegistryAlias)
