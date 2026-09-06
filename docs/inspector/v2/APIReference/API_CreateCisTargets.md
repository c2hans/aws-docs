---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCisTargets.html
---

# CreateCisTargets
<a name="API_CreateCisTargets"></a>

Creates CIS targets.

## Contents
<a name="API_CreateCisTargets_Contents"></a>

 ** accountIds **   <a name="inspector2-Type-CreateCisTargets-accountIds"></a>
The CIS target account ids.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Pattern: `\d{12}|ALL_ACCOUNTS|SELF`
Required: Yes

 ** targetResourceTags **   <a name="inspector2-Type-CreateCisTargets-targetResourceTags"></a>
The CIS target resource tags.
Type: String to array of strings map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{Z}\p{N}_.:/=\-@]*`
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_CreateCisTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CreateCisTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CreateCisTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CreateCisTargets)
