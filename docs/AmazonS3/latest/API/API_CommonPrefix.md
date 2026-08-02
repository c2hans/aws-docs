---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_CommonPrefix.html
---

# CommonPrefix
<a name="API_CommonPrefix"></a>

Container for all (if there are any) keys between Prefix and the next occurrence of the string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

## Contents
<a name="API_CommonPrefix_Contents"></a>

 ** Prefix **   <a name="AmazonS3-Type-CommonPrefix-Prefix"></a>
Container for the specified common prefix.
Type: String
Required: No

## See Also
<a name="API_CommonPrefix_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CommonPrefix)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CommonPrefix)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CommonPrefix)
