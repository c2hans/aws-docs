---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_AccountTag.html
---

# AccountTag

A tag key-value pair associated with a resource in an account.

## Contents
<a name="API_AccountTag_Contents"></a>

 ** key **   <a name="AWSHealth-Type-AccountTag-key"></a>
The tag key.
Type: String
Length Constraints: Maximum length of 127.
Pattern: `.{0,127}`
Required: No

 ** type **   <a name="AWSHealth-Type-AccountTag-type"></a>
The type of tag (resource tag or account tag).
Type: String
Valid Values: `ACCOUNT_RESOURCE_TAG`
Required: No

 ** value **   <a name="AWSHealth-Type-AccountTag-value"></a>
The tag value.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `.{0,255}`
Required: No

## See Also
<a name="API_AccountTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/AccountTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/AccountTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/AccountTag)
