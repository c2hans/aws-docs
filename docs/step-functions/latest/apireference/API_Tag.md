---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Tags are key-value pairs that can be associated with Step Functions state machines and activities.

An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the * AWS Billing and Cost Management User Guide*, and [Controlling Access Using IAM Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html).

Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + - @`.

## Contents
<a name="API_Tag_Contents"></a>

 ** key **   <a name="StepFunctions-Type-Tag-key"></a>
The key of a tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** value **   <a name="StepFunctions-Type-Tag-value"></a>
The value of a tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/Tag)
