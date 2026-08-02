---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_AzureBlobSasConfiguration.html
---

# AzureBlobSasConfiguration
<a name="API_AzureBlobSasConfiguration"></a>

The shared access signature (SAS) configuration that allows AWS DataSync to access your Microsoft Azure Blob Storage.

For more information, see [SAS tokens](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-sas-tokens) for accessing your Azure Blob Storage.

## Contents
<a name="API_AzureBlobSasConfiguration_Contents"></a>

 ** Token **   <a name="DataSync-Type-AzureBlobSasConfiguration-Token"></a>
Specifies a SAS token that provides permissions to access your Azure Blob Storage.
The token is part of the SAS URI string that comes after the storage resource URI and a question mark. A token looks something like this:
 `sp=r&st=2023-12-20T14:54:52Z&se=2023-12-20T22:54:52Z&spr=https&sv=2021-06-08&sr=c&sig=aBBKDWQvyuVcTPH9EBp%2FXTI9E%2F%2Fmq171%2BZU178wcwqU%3D`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.+$`
Required: Yes

## See Also
<a name="API_AzureBlobSasConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/AzureBlobSasConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/AzureBlobSasConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/AzureBlobSasConfiguration)
