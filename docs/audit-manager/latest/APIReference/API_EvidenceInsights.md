---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_EvidenceInsights.html
---

# EvidenceInsights
<a name="API_EvidenceInsights"></a>

A breakdown of the latest compliance check status for the evidence in your Audit Manager assessments.

## Contents
<a name="API_EvidenceInsights_Contents"></a>

 ** compliantEvidenceCount **   <a name="auditmanager-Type-EvidenceInsights-compliantEvidenceCount"></a>
The number of compliance check evidence that Audit Manager classified as compliant. This includes evidence that was collected from AWS Security Hub CSPM with a *Pass* ruling, or collected from AWS Config with a *Compliant* ruling.
Type: Integer
Required: No

 ** inconclusiveEvidenceCount **   <a name="auditmanager-Type-EvidenceInsights-inconclusiveEvidenceCount"></a>
The number of evidence that a compliance check ruling isn't available for. Evidence is inconclusive when the associated control uses AWS Security Hub CSPM or AWS Config as a data source but you didn't enable those services. This is also the case when a control uses a data source that doesn’t support compliance checks (for example, manual evidence, API calls, or AWS CloudTrail).
If evidence has a compliance check status of *not applicable* in the console, it's classified as *inconclusive* in `EvidenceInsights` data.
Type: Integer
Required: No

 ** noncompliantEvidenceCount **   <a name="auditmanager-Type-EvidenceInsights-noncompliantEvidenceCount"></a>
The number of compliance check evidence that Audit Manager classified as non-compliant. This includes evidence that was collected from AWS Security Hub CSPM with a *Fail* ruling, or collected from AWS Config with a *Non-compliant* ruling.
Type: Integer
Required: No

## See Also
<a name="API_EvidenceInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/EvidenceInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/EvidenceInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/EvidenceInsights)
