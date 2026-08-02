---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Signal.html
---

# Signal
<a name="API_Signal"></a>

Contains information about the signals involved in the attack sequence.

## Contents
<a name="API_Signal_Contents"></a>

 ** count **   <a name="guardduty-Type-Signal-count"></a>
The number of times this signal was observed.
Type: Integer
Required: Yes

 ** createdAt **   <a name="guardduty-Type-Signal-createdAt"></a>
The timestamp when the first finding or activity related to this signal was observed.
Type: Timestamp
Required: Yes

 ** firstSeenAt **   <a name="guardduty-Type-Signal-firstSeenAt"></a>
The timestamp when the first finding or activity related to this signal was observed.
Type: Timestamp
Required: Yes

 ** lastSeenAt **   <a name="guardduty-Type-Signal-lastSeenAt"></a>
The timestamp when the last finding or activity related to this signal was observed.
Type: Timestamp
Required: Yes

 ** name **   <a name="guardduty-Type-Signal-name"></a>
The name of the signal. For example, when signal type is `FINDING`, the signal name is the name of the finding.
Type: String
Required: Yes

 ** type **   <a name="guardduty-Type-Signal-type"></a>
The type of the signal used to identify an attack sequence.
Signals can be GuardDuty findings or activities observed in data sources that GuardDuty monitors. For more information, see [Foundational data sources](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html) in the *Amazon GuardDuty User Guide*.
A signal type can be one of the valid values listed in this API. Here are the related descriptions:
+  `FINDING` - Individually generated GuardDuty finding.
+  `CLOUD_TRAIL` - Activity observed from CloudTrail logs
+  `S3_DATA_EVENTS` - Activity observed from CloudTrail data events for S3. Activities associated with this type will show up only when you have enabled GuardDuty S3 Protection feature in your account. For more information about S3 Protection and steps to enable it, see [S3 Protection](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html) in the *Amazon GuardDuty User Guide*.
Type: String
Valid Values: `FINDING | CLOUD_TRAIL | S3_DATA_EVENTS | EKS_AUDIT_LOGS | FLOW_LOGS | DNS_LOGS | RUNTIME_MONITORING`
Required: Yes

 ** uid **   <a name="guardduty-Type-Signal-uid"></a>
The unique identifier of the signal.
Type: String
Required: Yes

 ** updatedAt **   <a name="guardduty-Type-Signal-updatedAt"></a>
The timestamp when this signal was last observed.
Type: Timestamp
Required: Yes

 ** actorIds **   <a name="guardduty-Type-Signal-actorIds"></a>
Information about the IDs of the threat actors involved in the signal.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Required: No

 ** description **   <a name="guardduty-Type-Signal-description"></a>
The description of the signal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** endpointIds **   <a name="guardduty-Type-Signal-endpointIds"></a>
Information about the endpoint IDs associated with this signal.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Required: No

 ** resourceUids **   <a name="guardduty-Type-Signal-resourceUids"></a>
Information about the unique identifiers of the resources involved in the signal.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Required: No

 ** severity **   <a name="guardduty-Type-Signal-severity"></a>
The severity associated with the signal. For more information about severity, see [Findings severity levels](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html) in the *Amazon GuardDuty User Guide*.
Type: Double
Required: No

 ** signalIndicators **   <a name="guardduty-Type-Signal-signalIndicators"></a>
Contains information about the indicators associated with the signals.
Type: Array of [Indicator](API_Indicator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Required: No

## See Also
<a name="API_Signal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Signal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Signal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Signal)
