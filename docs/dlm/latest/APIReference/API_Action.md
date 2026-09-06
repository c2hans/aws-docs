---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_Action.html
---

# Action
<a name="API_Action"></a>

 **[Event-based policies only]** Specifies an action for an event-based policy.

## Contents
<a name="API_Action_Contents"></a>

 ** CrossRegionCopy **   <a name="dlm-Type-Action-CrossRegionCopy"></a>
The rule for copying shared snapshots across Regions.
Type: Array of [CrossRegionCopyAction](API_CrossRegionCopyAction.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: Yes

 ** Name **   <a name="dlm-Type-Action-Name"></a>
A descriptive name for the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 120.
Pattern: `[0-9A-Za-z _-]+`
Required: Yes

## See Also
<a name="API_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/Action)
