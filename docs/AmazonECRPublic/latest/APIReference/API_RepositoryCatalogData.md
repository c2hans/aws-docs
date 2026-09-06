---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_RepositoryCatalogData.html
---

# RepositoryCatalogData
<a name="API_RepositoryCatalogData"></a>

The catalog data for a repository. This data is publicly visible in the Amazon ECR Public Gallery.

## Contents
<a name="API_RepositoryCatalogData_Contents"></a>

 ** aboutText **   <a name="ecrpublic-Type-RepositoryCatalogData-aboutText"></a>
The longform description of the contents of the repository. This text appears in the repository details on the Amazon ECR Public Gallery.
Type: String
Length Constraints: Maximum length of 25600.
Required: No

 ** architectures **   <a name="ecrpublic-Type-RepositoryCatalogData-architectures"></a>
The architecture tags that are associated with the repository.
Only supported operating system tags appear publicly in the Amazon ECR Public Gallery. For more information, see [RepositoryCatalogDataInput](API_RepositoryCatalogDataInput.md).
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** description **   <a name="ecrpublic-Type-RepositoryCatalogData-description"></a>
The short description of the repository.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** logoUrl **   <a name="ecrpublic-Type-RepositoryCatalogData-logoUrl"></a>
The URL that contains the logo that's associated with the repository.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** marketplaceCertified **   <a name="ecrpublic-Type-RepositoryCatalogData-marketplaceCertified"></a>
Indicates whether the repository is certified by AWS Marketplace.
Type: Boolean
Required: No

 ** operatingSystems **   <a name="ecrpublic-Type-RepositoryCatalogData-operatingSystems"></a>
The operating system tags that are associated with the repository.
Only supported operating system tags appear publicly in the Amazon ECR Public Gallery. For more information, see [RepositoryCatalogDataInput](API_RepositoryCatalogDataInput.md).
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** usageText **   <a name="ecrpublic-Type-RepositoryCatalogData-usageText"></a>
The longform usage details of the contents of the repository. The usage text provides context for users of the repository.
Type: String
Length Constraints: Maximum length of 25600.
Required: No

## See Also
<a name="API_RepositoryCatalogData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/RepositoryCatalogData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/RepositoryCatalogData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/RepositoryCatalogData)
