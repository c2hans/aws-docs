---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FetchQuery.html
---

# FetchQuery
<a name="API_FetchQuery"></a>

Contains the parameters of a request that GuardDuty made to retrieve data during an investigation. The members that are set depend on the `FetchType` of the record.

## Contents
<a name="API_FetchQuery_Contents"></a>

 ** accountId **   <a name="guardduty-Type-FetchQuery-accountId"></a>
The AWS account ID that the request was made for.
Type: String
Required: No

 ** criteria **   <a name="guardduty-Type-FetchQuery-criteria"></a>
The filter criteria that GuardDuty applied to the request.
Type: Array of [FetchCriterion](API_FetchCriterion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** findingId **   <a name="guardduty-Type-FetchQuery-findingId"></a>
The ID of the finding that GuardDuty retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** findingType **   <a name="guardduty-Type-FetchQuery-findingType"></a>
The finding type whose documentation GuardDuty retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** indicator **   <a name="guardduty-Type-FetchQuery-indicator"></a>
The threat indicator that GuardDuty looked up, such as an IP address, a domain, or a file hash.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** indicatorType **   <a name="guardduty-Type-FetchQuery-indicatorType"></a>
The type of the threat indicator. Possible values are `IP`, `DOMAIN`, and `FILE`.
Type: String
Valid Values: `IP | DOMAIN | FILE`
Required: No

 ** rowLimit **   <a name="guardduty-Type-FetchQuery-rowLimit"></a>
The maximum number of rows that GuardDuty requested. Valid values are 1 to 1,000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** timeWindow **   <a name="guardduty-Type-FetchQuery-timeWindow"></a>
The time range of the data that GuardDuty requested.
Type: [FetchTimeWindow](API_FetchTimeWindow.md) object
Required: No

## See Also
<a name="API_FetchQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FetchQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FetchQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FetchQuery)
