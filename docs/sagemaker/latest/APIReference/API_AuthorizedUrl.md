---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AuthorizedUrl.html
---

# AuthorizedUrl
<a name="API_AuthorizedUrl"></a>

Contains a presigned URL and its associated local file path for downloading hub content artifacts.

## Contents
<a name="API_AuthorizedUrl_Contents"></a>

 ** LocalPath **   <a name="sagemaker-Type-AuthorizedUrl-LocalPath"></a>
The recommended local file path where the downloaded file should be stored to maintain proper directory structure and file organization.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\/.*`
Required: No

 ** Url **   <a name="sagemaker-Type-AuthorizedUrl-Url"></a>
The presigned S3 URL that provides temporary, secure access to download the file. URLs expire within 15 minutes for security purposes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_AuthorizedUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AuthorizedUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AuthorizedUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AuthorizedUrl)
