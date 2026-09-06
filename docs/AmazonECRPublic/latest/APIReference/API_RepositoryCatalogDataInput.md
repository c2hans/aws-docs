---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_RepositoryCatalogDataInput.html
---

# RepositoryCatalogDataInput
<a name="API_RepositoryCatalogDataInput"></a>

An object that contains the catalog data for a repository. This data is publicly visible in the Amazon ECR Public Gallery.

## Contents
<a name="API_RepositoryCatalogDataInput_Contents"></a>

 ** aboutText **   <a name="ecrpublic-Type-RepositoryCatalogDataInput-aboutText"></a>
A detailed description of the contents of the repository. It's publicly visible in the Amazon ECR Public Gallery. The text must be in markdown format.
Type: String
Length Constraints: Maximum length of 25600.
Required: No

 ** architectures **   <a name="ecrpublic-Type-RepositoryCatalogDataInput-architectures"></a>
The system architecture that the images in the repository are compatible with. On the Amazon ECR Public Gallery, the following supported architectures appear as badges on the repository and are used as search filters.
If an unsupported tag is added to your repository catalog data, it's associated with the repository and can be retrieved using the API but isn't discoverable in the Amazon ECR Public Gallery.
+  `ARM`
+  `ARM 64`
+  `x86`
+  `x86-64`
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** description **   <a name="ecrpublic-Type-RepositoryCatalogDataInput-description"></a>
A short description of the contents of the repository. This text appears in both the image details and also when searching for repositories on the Amazon ECR Public Gallery.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** logoImageBlob **   <a name="ecrpublic-Type-RepositoryCatalogDataInput-logoImageBlob"></a>
The base64-encoded repository logo payload.
The repository logo is only publicly visible in the Amazon ECR Public Gallery for verified accounts.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 512000.
Required: No

 ** operatingSystems **   <a name="ecrpublic-Type-RepositoryCatalogDataInput-operatingSystems"></a>
The operating systems that the images in the repository are compatible with. On the Amazon ECR Public Gallery, the following supported operating systems appear as badges on the repository and are used as search filters.
If an unsupported tag is added to your repository catalog data, it's associated with the repository and can be retrieved using the API but isn't discoverable in the Amazon ECR Public Gallery.
+  `Linux`
+  `Windows`
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** usageText **   <a name="ecrpublic-Type-RepositoryCatalogDataInput-usageText"></a>
Detailed information about how to use the contents of the repository. It's publicly visible in the Amazon ECR Public Gallery. The usage text provides context, support information, and additional usage details for users of the repository. The text must be in markdown format.
Type: String
Length Constraints: Maximum length of 25600.
Required: No

## See Also
<a name="API_RepositoryCatalogDataInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/RepositoryCatalogDataInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/RepositoryCatalogDataInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/RepositoryCatalogDataInput)
