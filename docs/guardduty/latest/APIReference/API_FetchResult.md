---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FetchResult.html
---

# FetchResult
<a name="API_FetchResult"></a>

Contains the data that GuardDuty received in response to a request during an investigation. The members that are set depend on the `FetchType` of the record.

## Contents
<a name="API_FetchResult_Contents"></a>

 ** documentation **   <a name="guardduty-Type-FetchResult-documentation"></a>
The documentation for the finding type that GuardDuty retrieved.
Type: [FindingTypeDocumentation](API_FindingTypeDocumentation.md) object
Required: No

 ** features **   <a name="guardduty-Type-FetchResult-features"></a>
The configuration of the detector features that GuardDuty retrieved.
Type: Array of [InvestigationDetectorFeatureConfiguration](API_InvestigationDetectorFeatureConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** itemIds **   <a name="guardduty-Type-FetchResult-itemIds"></a>
The identifiers of the items that were returned, such as finding IDs, event IDs, signal IDs, or account IDs, depending on `FetchType`. The list contains at most 50 identifiers; `TotalCount` can be larger.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** totalCount **   <a name="guardduty-Type-FetchResult-totalCount"></a>
The total number of items that were returned. This value can be greater than the number of identifiers in `ItemIds`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** verdict **   <a name="guardduty-Type-FetchResult-verdict"></a>
The reputation verdict for the threat indicator. Possible values are `THREAT`, `BENIGN`, and `NEUTRAL`. If the lookup returned more than one result, the verdict describes the first result.
Type: String
Valid Values: `THREAT | BENIGN | NEUTRAL`
Required: No

## See Also
<a name="API_FetchResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FetchResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FetchResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FetchResult)
