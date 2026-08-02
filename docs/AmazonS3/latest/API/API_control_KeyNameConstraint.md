---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_KeyNameConstraint.html
---

# KeyNameConstraint
<a name="API_control_KeyNameConstraint"></a>

If provided, the generated manifest includes only source bucket objects whose object keys match the string constraints specified for `MatchAnyPrefix`, `MatchAnySuffix`, and `MatchAnySubstring`.

## Contents
<a name="API_control_KeyNameConstraint_Contents"></a>

 ** MatchAnyPrefix **   <a name="AmazonS3-Type-control_KeyNameConstraint-MatchAnyPrefix"></a>
If provided, the generated manifest includes objects where the specified string appears at the start of the object key string. Each KeyNameConstraint filter accepts an array of strings with a length of 1 string.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** MatchAnySubstring **   <a name="AmazonS3-Type-control_KeyNameConstraint-MatchAnySubstring"></a>
If provided, the generated manifest includes objects where the specified string appears anywhere within the object key string. Each KeyNameConstraint filter accepts an array of strings with a length of 1 string.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** MatchAnySuffix **   <a name="AmazonS3-Type-control_KeyNameConstraint-MatchAnySuffix"></a>
If provided, the generated manifest includes objects where the specified string appears at the end of the object key string. Each KeyNameConstraint filter accepts an array of strings with a length of 1 string.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_control_KeyNameConstraint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/KeyNameConstraint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/KeyNameConstraint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/KeyNameConstraint)
