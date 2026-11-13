---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_SupportingData.html
---

# SupportingData
<a name="API_SupportingData"></a>

Contains the structured details for an investigation record. Only the member that matches the record type is set.

## Contents
<a name="API_SupportingData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** analysis **   <a name="guardduty-Type-SupportingData-analysis"></a>
Details about an assessment that GuardDuty derived from the data. Set for `ANALYSIS` records.
Type: [AnalysisRecord](API_AnalysisRecord.md) object
Required: No

 ** fetch **   <a name="guardduty-Type-SupportingData-fetch"></a>
Details about data that GuardDuty retrieved. Set for `FETCH` records.
Type: [FetchRecord](API_FetchRecord.md) object
Required: No

 ** metadata **   <a name="guardduty-Type-SupportingData-metadata"></a>
Operational details about the investigation. Set for `METADATA` records.
Type: [MetadataRecord](API_MetadataRecord.md) object
Required: No

 ** observation **   <a name="guardduty-Type-SupportingData-observation"></a>
Details about a fact that GuardDuty noted about your environment. Set for `OBSERVATION` records.
Type: [ObservationRecord](API_ObservationRecord.md) object
Required: No

## See Also
<a name="API_SupportingData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/SupportingData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/SupportingData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/SupportingData)
