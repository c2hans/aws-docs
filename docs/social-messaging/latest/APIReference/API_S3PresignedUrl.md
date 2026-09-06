---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_S3PresignedUrl.html
---

# S3PresignedUrl
<a name="API_S3PresignedUrl"></a>

You can use presigned URLs to grant time-limited access to objects in Amazon S3 without updating your bucket policy. For more information, see [Working with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) in the *Amazon S3 User Guide*.

## Contents
<a name="API_S3PresignedUrl_Contents"></a>

 ** headers **   <a name="Social-Type-S3PresignedUrl-headers"></a>
A map of headers and their values. You must specify the `Content-Type` header when using `PostWhatsAppMessageMedia`. For a list of common headers, see [Common Request Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonRequestHeaders.html) in the *Amazon S3 API Reference*
Type: String to string map
Required: Yes

 ** url **   <a name="Social-Type-S3PresignedUrl-url"></a>
The presign url to the object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `https://(.*)s3(.*).amazonaws.com/(.*)`
Required: Yes

## See Also
<a name="API_S3PresignedUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/S3PresignedUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/S3PresignedUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/S3PresignedUrl)
