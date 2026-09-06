---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_ActionSet.html
---

# ActionSet
<a name="API_ActionSet"></a>

The set of actions authorized by a permit. Specify either all actions or a list of specific actions.

## Contents
<a name="API_ActionSet_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** actions **   <a name="supportauthorization-Type-ActionSet-actions"></a>
A list of specific support actions to authorize. Maximum of 10 actions.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-z][a-z0-9-]*:[A-Za-z0-9_.-]+`
Required: No

 ** allActions **   <a name="supportauthorization-Type-ActionSet-allActions"></a>
Authorizes all available support actions.
Type: Structure
Required: No

## See Also
<a name="API_ActionSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/ActionSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/ActionSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/ActionSet)
