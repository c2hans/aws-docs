---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Tags are key/value pairs defined by a user and associated with a pipeline to control access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see [Controlling User Access to Pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html) in the *AWS Data Pipeline Developer Guide*.

## Contents
<a name="API_Tag_Contents"></a>

 ** key **   <a name="DP-Type-Tag-key"></a>
The key name of a tag defined by a user. For more information, see [Controlling User Access to Pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html) in the *AWS Data Pipeline Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** value **   <a name="DP-Type-Tag-value"></a>
The optional value portion of a tag defined by a user. For more information, see [Controlling User Access to Pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html) in the *AWS Data Pipeline Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/Tag)
