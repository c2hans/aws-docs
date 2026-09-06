---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ErrorDocument.html
---

# ErrorDocument
<a name="API_ErrorDocument"></a>

The error information.

## Contents
<a name="API_ErrorDocument_Contents"></a>

 ** Key **   <a name="AmazonS3-Type-ErrorDocument-Key"></a>
The object key name to use when a 4XX class error occurs.
Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [ XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_ErrorDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ErrorDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ErrorDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ErrorDocument)
