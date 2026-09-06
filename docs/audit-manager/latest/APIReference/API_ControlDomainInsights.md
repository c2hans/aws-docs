---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ControlDomainInsights.html
---

# ControlDomainInsights
<a name="API_ControlDomainInsights"></a>

A summary of the latest analytics data for a specific control domain.

Control domain insights are grouped by control domain, and ranked by the highest total count of non-compliant evidence.

## Contents
<a name="API_ControlDomainInsights_Contents"></a>

 ** controlsCountByNoncompliantEvidence **   <a name="auditmanager-Type-ControlDomainInsights-controlsCountByNoncompliantEvidence"></a>
The number of controls in the control domain that collected non-compliant evidence on the `lastUpdated` date.
Type: Integer
Required: No

 ** evidenceInsights **   <a name="auditmanager-Type-ControlDomainInsights-evidenceInsights"></a>
A breakdown of the compliance check status for the evidence that’s associated with the control domain.
Type: [EvidenceInsights](API_EvidenceInsights.md) object
Required: No

 ** id **   <a name="auditmanager-Type-ControlDomainInsights-id"></a>
The unique identifier for the control domain. Audit Manager supports the control domains that are provided by AWS Control Catalog. For information about how to find a list of available control domains, see [`ListDomains`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html) in the AWS Control Catalog API Reference.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 2048.
Pattern: `^arn:.*:controlcatalog:.*:.*:domain/.*|UNCATEGORIZED|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdated **   <a name="auditmanager-Type-ControlDomainInsights-lastUpdated"></a>
The time when the control domain insights were last updated.
Type: Timestamp
Required: No

 ** name **   <a name="auditmanager-Type-ControlDomainInsights-name"></a>
The name of the control domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** totalControlsCount **   <a name="auditmanager-Type-ControlDomainInsights-totalControlsCount"></a>
The total number of controls in the control domain.
Type: Integer
Required: No

## See Also
<a name="API_ControlDomainInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ControlDomainInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ControlDomainInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ControlDomainInsights)
