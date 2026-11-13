---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FetchRecord.html
---

# FetchRecord
<a name="API_FetchRecord"></a>

Contains information about data that GuardDuty retrieved during an investigation, including what GuardDuty requested and what it received.

## Contents
<a name="API_FetchRecord_Contents"></a>

 ** fetchType **   <a name="guardduty-Type-FetchRecord-fetchType"></a>
The kind of data that GuardDuty retrieved. The value determines which members of `Query` and `Result` can be set. Possible values:
+  `FINDINGS` – GuardDuty findings.
+  `DETECTOR` – The configuration of a GuardDuty detector.
+  `REPUTATION` – Reputation information about a threat indicator, such as an IP address, a domain, or a file hash.
+  `FINDING_TYPE_DOCUMENTATION` – The documentation for a finding type.
+  `CLOUD_TRAIL_RAW_EVENTS` – AWS CloudTrail events.
+  `RUNTIME_SIGNALS` – Runtime signals.
+  `MEMBER_ACCOUNTS` – A list of member accounts.
Type: String
Valid Values: `FINDINGS | DETECTOR | REPUTATION | FINDING_TYPE_DOCUMENTATION | CLOUD_TRAIL_RAW_EVENTS | RUNTIME_SIGNALS | MEMBER_ACCOUNTS`
Required: Yes

 ** query **   <a name="guardduty-Type-FetchRecord-query"></a>
The request that GuardDuty made. Not every record includes a query.
Type: [FetchQuery](API_FetchQuery.md) object
Required: No

 ** result **   <a name="guardduty-Type-FetchRecord-result"></a>
The data that GuardDuty received in response to the request. Not every record includes a result.
Type: [FetchResult](API_FetchResult.md) object
Required: No

## See Also
<a name="API_FetchRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FetchRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FetchRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FetchRecord)
