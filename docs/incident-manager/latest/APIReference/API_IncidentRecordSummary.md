---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_IncidentRecordSummary.html
---

# IncidentRecordSummary
<a name="API_IncidentRecordSummary"></a>

Details describing an incident record.

## Contents
<a name="API_IncidentRecordSummary_Contents"></a>

 ** arn **   <a name="IncidentManager-Type-IncidentRecordSummary-arn"></a>
The Amazon Resource Name (ARN) of the incident.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** creationTime **   <a name="IncidentManager-Type-IncidentRecordSummary-creationTime"></a>
The timestamp for when the incident was created.
Type: Timestamp
Required: Yes

 ** impact **   <a name="IncidentManager-Type-IncidentRecordSummary-impact"></a>
Defines the impact to customers and applications.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: Yes

 ** incidentRecordSource **   <a name="IncidentManager-Type-IncidentRecordSummary-incidentRecordSource"></a>
What caused Incident Manager to create the incident.
Type: [IncidentRecordSource](API_IncidentRecordSource.md) object
Required: Yes

 ** status **   <a name="IncidentManager-Type-IncidentRecordSummary-status"></a>
The current status of the incident.
Type: String
Valid Values: `OPEN | RESOLVED`
Required: Yes

 ** title **   <a name="IncidentManager-Type-IncidentRecordSummary-title"></a>
The title of the incident. This value is either provided by the response plan or overwritten on creation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** resolvedTime **   <a name="IncidentManager-Type-IncidentRecordSummary-resolvedTime"></a>
The timestamp for when the incident was resolved.
Type: Timestamp
Required: No

## See Also
<a name="API_IncidentRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/IncidentRecordSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/IncidentRecordSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/IncidentRecordSummary)
