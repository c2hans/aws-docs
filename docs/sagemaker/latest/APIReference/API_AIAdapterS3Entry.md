---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIAdapterS3Entry.html
---

# AIAdapterS3Entry
<a name="API_AIAdapterS3Entry"></a>

A LoRA adapter entry identified by an Amazon S3 URI.

## Contents
<a name="API_AIAdapterS3Entry_Contents"></a>

 ** AdapterId **   <a name="sagemaker-Type-AIAdapterS3Entry-AdapterId"></a>
A unique identifier for the adapter. This ID is used as the inference component name when the adapter is deployed. The ID must start and end with an alphanumeric character, can contain hyphens between alphanumeric characters, and can be up to 63 characters long.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-AIAdapterS3Entry-S3Uri"></a>
The Amazon S3 URI of the directory that contains the LoRA adapter artifacts in PEFT format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

## See Also
<a name="API_AIAdapterS3Entry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIAdapterS3Entry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIAdapterS3Entry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIAdapterS3Entry)
