---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RelatedFindings.html
---

# RelatedFindings
<a name="API_RelatedFindings"></a>

Contains information about findings that are related to the investigated activity.

## Contents
<a name="API_RelatedFindings_Contents"></a>

 ** correlated **   <a name="guardduty-Type-RelatedFindings-correlated"></a>
The findings that GuardDuty correlated with the investigated activity, grouped by finding type.
Type: Array of [CorrelatedFinding](API_CorrelatedFinding.md) objects
Array Members: Minimum number of 0 items. Maximum number of 8 items.
Required: No

 ** observed **   <a name="guardduty-Type-RelatedFindings-observed"></a>
Other finding types that GuardDuty observed, with counts. These entries don't include finding IDs.
Type: Array of [ObservedFindingType](API_ObservedFindingType.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_RelatedFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RelatedFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RelatedFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RelatedFindings)
