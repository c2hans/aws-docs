---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_LFTag.html
---

# LFTag
<a name="API_LFTag"></a>

A structure that allows an admin to grant user permissions on certain conditions. For example, granting a role access to all columns that do not have the LF-tag 'PII' in tables that have the LF-tag 'Prod'.

## Contents
<a name="API_LFTag_Contents"></a>

 ** TagKey **   <a name="lakeformation-Type-LFTag-TagKey"></a>
The key-name for the LF-tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@%]*)$`
Required: Yes

 ** TagValues **   <a name="lakeformation-Type-LFTag-TagValues"></a>
A list of possible values an attribute can take.
The maximum number of values that can be defined for a LF-Tag is 1000. A single API call supports 50 values. You can use multiple API calls to add more values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\*\/=+\-@%]*)$`
Required: Yes

## See Also
<a name="API_LFTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/LFTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/LFTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/LFTag)
