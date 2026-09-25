---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ScopedActions.html
---

# ScopedActions
<a name="API_ScopedActions"></a>

A group of actions within an access grant, together with the resource scopes and context conditions that apply to exactly those actions.

## Contents
<a name="API_ScopedActions_Contents"></a>

 ** actions **   <a name="cloudwatchomni-Type-ScopedActions-actions"></a>
The actions this group applies to.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-z0-9][a-z0-9-]*:[A-Za-z][A-Za-z0-9]*`
Required: Yes

 ** contextConditions **   <a name="cloudwatchomni-Type-ScopedActions-contextConditions"></a>
Optional context conditions for fine-grained access control on these actions.
Type: String to array of strings map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** resources **   <a name="cloudwatchomni-Type-ScopedActions-resources"></a>
Optional resource scopes constraining these actions to specific resources.
Type: Array of [ResourceScope](API_ResourceScope.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_ScopedActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ScopedActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ScopedActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ScopedActions)
