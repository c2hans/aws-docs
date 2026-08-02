---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ControlInsightsMetadataItem.html
---

# ControlInsightsMetadataItem
<a name="API_ControlInsightsMetadataItem"></a>

A summary of the latest analytics data for a specific control.

This data reflects the total counts for the specified control across all active assessments. Control insights are grouped by control domain, and ranked by the highest total count of non-compliant evidence.

## Contents
<a name="API_ControlInsightsMetadataItem_Contents"></a>

 ** evidenceInsights **   <a name="auditmanager-Type-ControlInsightsMetadataItem-evidenceInsights"></a>
A breakdown of the compliance check status for the evidence that’s associated with the control.
Type: [EvidenceInsights](API_EvidenceInsights.md) object
Required: No

 ** id **   <a name="auditmanager-Type-ControlInsightsMetadataItem-id"></a>
The unique identifier for the control.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 2048.
Pattern: `^arn:.*:controlcatalog:.*:.*:domain/.*|UNCATEGORIZED|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdated **   <a name="auditmanager-Type-ControlInsightsMetadataItem-lastUpdated"></a>
The time when the control insights were last updated.
Type: Timestamp
Required: No

 ** name **   <a name="auditmanager-Type-ControlInsightsMetadataItem-name"></a>
The name of the control.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

## See Also
<a name="API_ControlInsightsMetadataItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ControlInsightsMetadataItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ControlInsightsMetadataItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ControlInsightsMetadataItem)
