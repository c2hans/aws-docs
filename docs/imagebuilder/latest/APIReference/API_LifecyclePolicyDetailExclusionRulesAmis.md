---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicyDetailExclusionRulesAmis.html
---

# LifecyclePolicyDetailExclusionRulesAmis
<a name="API_LifecyclePolicyDetailExclusionRulesAmis"></a>

Defines criteria for AMIs that are excluded from lifecycle actions.

## Contents
<a name="API_LifecyclePolicyDetailExclusionRulesAmis_Contents"></a>

 ** isPublic **   <a name="imagebuilder-Type-LifecyclePolicyDetailExclusionRulesAmis-isPublic"></a>
Configures whether public AMIs are excluded from the lifecycle action.
Type: Boolean
Required: No

 ** lastLaunched **   <a name="imagebuilder-Type-LifecyclePolicyDetailExclusionRulesAmis-lastLaunched"></a>
Configures Image Builder to exclude AMIs that were launched within the specified time period from lifecycle actions. AMIs with no recorded last-launched time aren't excluded by this rule.
Type: [LifecyclePolicyDetailExclusionRulesAmisLastLaunched](API_LifecyclePolicyDetailExclusionRulesAmisLastLaunched.md) object
Required: No

 ** regions **   <a name="imagebuilder-Type-LifecyclePolicyDetailExclusionRulesAmis-regions"></a>
Configures AWS Regions that are excluded from the lifecycle action.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** sharedAccounts **   <a name="imagebuilder-Type-LifecyclePolicyDetailExclusionRulesAmis-sharedAccounts"></a>
The lifecycle action doesn't apply to AMIs that are shared with any of the specified AWS accounts.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1536 items.
Pattern: `^[0-9]{12}$`
Required: No

 ** tagMap **   <a name="imagebuilder-Type-LifecyclePolicyDetailExclusionRulesAmis-tagMap"></a>
Lifecycle actions don't apply to AMIs that have any of these tags. Both the key and the value must match.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_LifecyclePolicyDetailExclusionRulesAmis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicyDetailExclusionRulesAmis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicyDetailExclusionRulesAmis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicyDetailExclusionRulesAmis)
