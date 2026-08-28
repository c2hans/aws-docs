---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Signal.html
---

# Signal
<a name="API_Signal"></a>

 Contains information about the signals involved in an Amazon GuardDuty Extended Threat Detection attack sequence. An attack sequence is a type of threat detected by GuardDuty. GuardDuty generates an attack sequence finding when multiple events, or signals, align to a potentially suspicious activity. When GuardDuty and AWS Security Hub CSPM are integrated, GuardDuty sends attack sequence findings to Security Hub CSPM.

A signal can be an API activity or a finding that GuardDuty uses to detect an attack sequence finding.

## Contents
<a name="API_Signal_Contents"></a>

 ** ActorIds **   <a name="securityhub-Type-Signal-ActorIds"></a>
 The IDs of the threat actors involved in the signal.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Count **   <a name="securityhub-Type-Signal-Count"></a>
 The number of times this signal was observed.
Type: Integer
Required: No

 ** CreatedAt **   <a name="securityhub-Type-Signal-CreatedAt"></a>
 The timestamp when the first finding or activity related to this signal was observed.
Type: Long
Required: No

 ** EndpointIds **   <a name="securityhub-Type-Signal-EndpointIds"></a>
Information about the endpoint IDs associated with this signal.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** FirstSeenAt **   <a name="securityhub-Type-Signal-FirstSeenAt"></a>
 The timestamp when the first finding or activity related to this signal was observed.
Type: Long
Required: No

 ** Id **   <a name="securityhub-Type-Signal-Id"></a>
 The identifier of the signal.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastSeenAt **   <a name="securityhub-Type-Signal-LastSeenAt"></a>
 The timestamp when the last finding or activity related to this signal was observed.
Type: Long
Required: No

 ** Name **   <a name="securityhub-Type-Signal-Name"></a>
 The name of the GuardDuty signal. For example, when signal type is `FINDING`, the signal name is the name of the finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProductArn **   <a name="securityhub-Type-Signal-ProductArn"></a>
 The Amazon Resource Name (ARN) of the product that generated the signal.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceIds **   <a name="securityhub-Type-Signal-ResourceIds"></a>
 The ARN or ID of the AWS resource associated with the signal.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Severity **   <a name="securityhub-Type-Signal-Severity"></a>
The severity associated with the signal. For more information about severity, see [Severity levels for GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html) in the *Amazon GuardDuty User Guide*.
Type: Double
Required: No

 ** SignalIndicators **   <a name="securityhub-Type-Signal-SignalIndicators"></a>
 Contains information about the indicators associated with the signals in this attack sequence finding. The values for `SignalIndicators` are a subset of the values for [SequenceIndicators](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Sequence.html), but the values for these fields don't always match 1:1.
Type: Array of [Indicator](API_Indicator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Title **   <a name="securityhub-Type-Signal-Title"></a>
 The description of the GuardDuty finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-Signal-Type"></a>
 The type of the signal used to identify an attack sequence.
Signals can be GuardDuty findings or activities observed in data sources that GuardDuty monitors. For more information, see [GuardDuty foundational data sources](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html) in the *Amazon GuardDuty User Guide*.
A signal type can be one of the following values. Here are the related descriptions:
+  `FINDING` - Individually generated GuardDuty finding.
+  `CLOUD_TRAIL` - Activity observed from AWS CloudTrail logs
+  `S3_DATA_EVENTS` - Activity observed from CloudTrail data events for Amazon Simple Storage Service (S3). Activities associated with this type will show up only when you have enabled GuardDuty S3 Protection feature in your account. For more information about S3 Protection and the steps to enable it, see [S3 Protection](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html) in the *Amazon GuardDuty User Guide*.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-Signal-UpdatedAt"></a>
 The timestamp when this signal was last observed.
Type: Long
Required: No

## See Also
<a name="API_Signal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Signal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Signal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Signal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
