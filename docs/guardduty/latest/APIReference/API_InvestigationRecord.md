---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationRecord.html
---

# InvestigationRecord
<a name="API_InvestigationRecord"></a>

Contains information about one step in the reasoning that GuardDuty followed during an investigation.

## Contents
<a name="API_InvestigationRecord_Contents"></a>

 ** createdAt **   <a name="guardduty-Type-InvestigationRecord-createdAt"></a>
The timestamp at which GuardDuty created the record.
Type: Timestamp
Required: Yes

 ** recordId **   <a name="guardduty-Type-InvestigationRecord-recordId"></a>
The unique identifier of the record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** title **   <a name="guardduty-Type-InvestigationRecord-title"></a>
A short title that describes the step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** type **   <a name="guardduty-Type-InvestigationRecord-type"></a>
The type of the record. Possible values:
+  `UPDATE` – A progress milestone, such as the request that started the investigation or a response from GuardDuty.
+  `FETCH` – Data that GuardDuty retrieved for the investigation, such as a finding, a detector configuration, or a list of your member accounts. The record includes what GuardDuty requested and what it received.
+  `OBSERVATION` – A fact that GuardDuty noted about your environment, such as the affected resource, the activity on that resource, or your detection coverage.
+  `ANALYSIS` – An assessment that GuardDuty derived from the data, such as a threat assessment, a comparison against normal behavior, or a process lineage.
+  `METADATA` – Operational details about the investigation itself, such as how long the investigation took.
Type: String
Valid Values: `OBSERVATION | ANALYSIS | UPDATE | FETCH | METADATA`
Required: Yes

 ** narrative **   <a name="guardduty-Type-InvestigationRecord-narrative"></a>
A plain-text explanation of the step. A narrative can span several paragraphs. Not every record includes a narrative.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** supportingData **   <a name="guardduty-Type-InvestigationRecord-supportingData"></a>
The structured details for the step. The member that is set matches the record type. `UPDATE` records never include supporting data, and records of other types don't always include it.
Type: [SupportingData](API_SupportingData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_InvestigationRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationRecord)
