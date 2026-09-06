---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompletedMultipartUpload.html
---

# CompletedMultipartUpload
<a name="API_CompletedMultipartUpload"></a>

The container for the completed multipart upload details.

## Contents
<a name="API_CompletedMultipartUpload_Contents"></a>

 ** Parts **   <a name="AmazonS3-Type-CompletedMultipartUpload-Parts"></a>
Array of CompletedPart data types.
If you do not supply a valid `Part` with your request, the service sends back an HTTP 400 response.
Type: Array of [CompletedPart](API_CompletedPart.md) data types
Required: No

## See Also
<a name="API_CompletedMultipartUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CompletedMultipartUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CompletedMultipartUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CompletedMultipartUpload)
