---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RegexPatternSetSummary.html
---

# RegexPatternSetSummary
<a name="API_RegexPatternSetSummary"></a>

High-level information about a [RegexPatternSet](API_RegexPatternSet.md), returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage a `RegexPatternSet`, and the ARN, that you provide to the [RegexPatternSetReferenceStatement](API_RegexPatternSetReferenceStatement.md) to use the pattern set in a [Rule](API_Rule.md).

## Contents
<a name="API_RegexPatternSetSummary_Contents"></a>

 ** ARN **   <a name="WAF-Type-RegexPatternSetSummary-ARN"></a>
The Amazon Resource Name (ARN) of the entity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="WAF-Type-RegexPatternSetSummary-Description"></a>
A description of the set that helps with identification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`
Required: No

 ** Id **   <a name="WAF-Type-RegexPatternSetSummary-Id"></a>
A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: No

 ** LockToken **   <a name="WAF-Type-RegexPatternSetSummary-LockToken"></a>
A token used for optimistic locking. AWS WAF returns a token to your `get` and `list` requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like `update` and `delete`. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a `WAFOptimisticLockException`. If this happens, perform another `get`, and use the new token returned by that operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: No

 ** Name **   <a name="WAF-Type-RegexPatternSetSummary-Name"></a>
The name of the data type instance. You cannot change the name after you create the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: No

## See Also
<a name="API_RegexPatternSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RegexPatternSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RegexPatternSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RegexPatternSetSummary)
