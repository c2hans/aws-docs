---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BlobMetadata.html
---

# BlobMetadata
<a name="API_BlobMetadata"></a>

Returns information about a specific Git blob object.

## Contents
<a name="API_BlobMetadata_Contents"></a>

 ** blobId **   <a name="CodeCommit-Type-BlobMetadata-blobId"></a>
The full ID of the blob.
Type: String
Required: No

 ** mode **   <a name="CodeCommit-Type-BlobMetadata-mode"></a>
The file mode permissions of the blob. File mode permission codes include:
+  `100644` indicates read/write
+  `100755` indicates read/write/execute
+  `160000` indicates a submodule
+  `120000` indicates a symlink
Type: String
Required: No

 ** path **   <a name="CodeCommit-Type-BlobMetadata-path"></a>
The path to the blob and associated file name, if any.
Type: String
Required: No

## See Also
<a name="API_BlobMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/BlobMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/BlobMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/BlobMetadata)
