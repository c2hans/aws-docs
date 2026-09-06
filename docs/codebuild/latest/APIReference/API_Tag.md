---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A tag, consisting of a key and a value.

This tag is available for use by AWS services that support tags in AWS CodeBuild.

## Contents
<a name="API_Tag_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** key **   <a name="CodeBuild-Type-Tag-key"></a>
The tag's key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=@+\-]*)$`
Required: No

 ** value **   <a name="CodeBuild-Type-Tag-value"></a>
The tag's value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=@+\-]*)$`
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/Tag)
