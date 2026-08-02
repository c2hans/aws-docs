---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_TagsError.html
---

# TagsError
<a name="API_TagsError"></a>

An object that contains details about an error related to retrieving tags.

## Contents
<a name="API_TagsError_Contents"></a>

 ** ErrorCode **   <a name="lambda-Type-TagsError-ErrorCode"></a>
The error code.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 21.
Pattern: `[A-Za-z]+Exception`
Required: Yes

 ** Message **   <a name="lambda-Type-TagsError-Message"></a>
The error message.
Type: String
Length Constraints: Minimum length of 84. Maximum length of 1000.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_TagsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/TagsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/TagsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/TagsError)
