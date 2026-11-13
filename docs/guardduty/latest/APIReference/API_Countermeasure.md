---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Countermeasure.html
---

# Countermeasure
<a name="API_Countermeasure"></a>

Contains the actions that you can take for one defensive tactic.

## Contents
<a name="API_Countermeasure_Contents"></a>

 ** actions **   <a name="guardduty-Type-Countermeasure-actions"></a>
The actions for the defensive tactic.
Type: Array of [CountermeasureAction](API_CountermeasureAction.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** defenseTactic **   <a name="guardduty-Type-Countermeasure-defenseTactic"></a>
The defensive tactic. Possible values are `Isolate`, `Evict`, `Restore`, `Harden`, and `Detect`.
Type: String
Valid Values: `Isolate | Evict | Restore | Harden | Detect`
Required: No

 ** description **   <a name="guardduty-Type-Countermeasure-description"></a>
A description of the countermeasure.
Type: String
Required: No

## See Also
<a name="API_Countermeasure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Countermeasure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Countermeasure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Countermeasure)
