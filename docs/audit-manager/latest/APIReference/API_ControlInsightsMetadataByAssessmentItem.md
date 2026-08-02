---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ControlInsightsMetadataByAssessmentItem.html
---

# ControlInsightsMetadataByAssessmentItem
<a name="API_ControlInsightsMetadataByAssessmentItem"></a>

A summary of the latest analytics data for a specific control in a specific active assessment.

Control insights are grouped by control domain, and ranked by the highest total count of non-compliant evidence.

## Contents
<a name="API_ControlInsightsMetadataByAssessmentItem_Contents"></a>

 ** controlSetName **   <a name="auditmanager-Type-ControlInsightsMetadataByAssessmentItem-controlSetName"></a>
The name of the control set that the assessment control belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** evidenceInsights **   <a name="auditmanager-Type-ControlInsightsMetadataByAssessmentItem-evidenceInsights"></a>
A breakdown of the compliance check status for the evidence that’s associated with the assessment control.
Type: [EvidenceInsights](API_EvidenceInsights.md) object
Required: No

 ** id **   <a name="auditmanager-Type-ControlInsightsMetadataByAssessmentItem-id"></a>
The unique identifier for the assessment control.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 2048.
Pattern: `^arn:.*:controlcatalog:.*:.*:domain/.*|UNCATEGORIZED|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdated **   <a name="auditmanager-Type-ControlInsightsMetadataByAssessmentItem-lastUpdated"></a>
The time when the assessment control insights were last updated.
Type: Timestamp
Required: No

 ** name **   <a name="auditmanager-Type-ControlInsightsMetadataByAssessmentItem-name"></a>
The name of the assessment control.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

## See Also
<a name="API_ControlInsightsMetadataByAssessmentItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ControlInsightsMetadataByAssessmentItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ControlInsightsMetadataByAssessmentItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ControlInsightsMetadataByAssessmentItem)
