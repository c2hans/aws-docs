---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_AccountEntity.html
---

# AccountEntity

An entity representing an affected account, including its account ID and associated tags.

## Contents
<a name="API_AccountEntity_Contents"></a>

 ** accountId **   <a name="AWSHealth-Type-AccountEntity-accountId"></a>
The 12-digit AWS account numbers that contains the affected entities.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\S+$`
Required: No

 ** accountTags **   <a name="AWSHealth-Type-AccountEntity-accountTags"></a>
A map of tag key-value pairs attached to the affected account.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 127.
Key Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{1,127}`
Value Length Constraints: Minimum length of 0. Maximum length of 255.
Value Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{0,255}`
Required: No

## See Also
<a name="API_AccountEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/AccountEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/AccountEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/AccountEntity)
