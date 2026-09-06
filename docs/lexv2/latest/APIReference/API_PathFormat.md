---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PathFormat.html
---

# PathFormat
<a name="API_PathFormat"></a>

The object that contains a path format that will be applied when Amazon Lex reads the transcript file in the bucket you provide. Specify this object if you only want Lex to read a subset of files in your Amazon S3 bucket.

## Contents
<a name="API_PathFormat_Contents"></a>

 ** objectPrefixes **   <a name="lexv2-Type-PathFormat-objectPrefixes"></a>
A list of Amazon S3 prefixes that points to sub-folders in the Amazon S3 bucket. Specify this list if you only want Lex to read the files under this set of sub-folders.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Length Constraints: Minimum length of 1.
Pattern: `^[\/]?+[a-zA-Z0-9!_.*'()-]+(\/[a-zA-Z0-9!_.*'()-]+)*$`
Required: No

## See Also
<a name="API_PathFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/PathFormat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/PathFormat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/PathFormat)
