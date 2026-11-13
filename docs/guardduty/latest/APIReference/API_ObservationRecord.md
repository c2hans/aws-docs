---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ObservationRecord.html
---

# ObservationRecord
<a name="API_ObservationRecord"></a>

Contains a fact that GuardDuty noted about your environment during an investigation, such as the affected resource, the activity on that resource, or your detection coverage. The record contains at most one of the payload members, the one that matches `ObservationType`. `Indicators` can accompany any observation type.

## Contents
<a name="API_ObservationRecord_Contents"></a>

 ** observationType **   <a name="guardduty-Type-ObservationRecord-observationType"></a>
The kind of observation. The value identifies the payload member that can be set: `FINDING_DETAIL` (`FindingDetail`), `RESOURCE` (`Resource`), `NETWORK_ACTIVITY` (`NetworkActivity`), `RDS_LOGIN_ACTIVITY` (`RdsLoginActivity`), `S3_ACTIVITY` (`S3Activity`), `KUBERNETES_ACTIVITY` (`KubernetesActivity`), `MALWARE_SCAN` (`MalwareScan`), `RELATED_FINDINGS` (`RelatedFindings`), `DETECTION_COVERAGE` (`DetectionCoverage`), `ACCOUNT_OVERVIEW` (`AccountOverview`), `RECOMMENDATION` (`Recommendations`), `RUNTIME_SIGNALS` (`RuntimeSignals`), `DISTRIBUTION` (`Distribution`), and `REPRESENTATIVE_RESOURCE` (`RepresentativeResources`).
Type: String
Valid Values: `FINDING_DETAIL | RESOURCE | NETWORK_ACTIVITY | RDS_LOGIN_ACTIVITY | S3_ACTIVITY | KUBERNETES_ACTIVITY | MALWARE_SCAN | RELATED_FINDINGS | DETECTION_COVERAGE | ACCOUNT_OVERVIEW | RECOMMENDATION | RUNTIME_SIGNALS | DISTRIBUTION | REPRESENTATIVE_RESOURCE`
Required: Yes

 ** accountOverview **   <a name="guardduty-Type-ObservationRecord-accountOverview"></a>
Overview information about an account. Set when `ObservationType` is `ACCOUNT_OVERVIEW`.
Type: [AccountOverview](API_AccountOverview.md) object
Required: No

 ** detectionCoverage **   <a name="guardduty-Type-ObservationRecord-detectionCoverage"></a>
Details about your detection coverage. Set when `ObservationType` is `DETECTION_COVERAGE`.
Type: [DetectionCoverage](API_DetectionCoverage.md) object
Required: No

 ** distribution **   <a name="guardduty-Type-ObservationRecord-distribution"></a>
A breakdown of findings along one dimension. Set when `ObservationType` is `DISTRIBUTION`.
Type: [Distribution](API_Distribution.md) object
Required: No

 ** findingDetail **   <a name="guardduty-Type-ObservationRecord-findingDetail"></a>
Details about a GuardDuty finding. Set when `ObservationType` is `FINDING_DETAIL`.
Type: [FindingDetail](API_FindingDetail.md) object
Required: No

 ** indicators **   <a name="guardduty-Type-ObservationRecord-indicators"></a>
The threat indicators associated with the observation, such as an IP address, a domain, or a file hash.
Type: Array of [InvestigationIndicator](API_InvestigationIndicator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** kubernetesActivity **   <a name="guardduty-Type-ObservationRecord-kubernetesActivity"></a>
Details about Kubernetes activity. Set when `ObservationType` is `KUBERNETES_ACTIVITY`.
Type: [KubernetesActivity](API_KubernetesActivity.md) object
Required: No

 ** malwareScan **   <a name="guardduty-Type-ObservationRecord-malwareScan"></a>
Details about a malware scan. Set when `ObservationType` is `MALWARE_SCAN`.
Type: [InvestigationMalwareScan](API_InvestigationMalwareScan.md) object
Required: No

 ** networkActivity **   <a name="guardduty-Type-ObservationRecord-networkActivity"></a>
Details about network activity. Set when `ObservationType` is `NETWORK_ACTIVITY`.
Type: [NetworkActivity](API_NetworkActivity.md) object
Required: No

 ** rdsLoginActivity **   <a name="guardduty-Type-ObservationRecord-rdsLoginActivity"></a>
Details about login activity on an Amazon RDS database. Set when `ObservationType` is `RDS_LOGIN_ACTIVITY`.
Type: [RdsLoginActivity](API_RdsLoginActivity.md) object
Required: No

 ** recommendations **   <a name="guardduty-Type-ObservationRecord-recommendations"></a>
Recommended actions. Set when `ObservationType` is `RECOMMENDATION`.
Type: Array of [Recommendation](API_Recommendation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** relatedFindings **   <a name="guardduty-Type-ObservationRecord-relatedFindings"></a>
Details about findings that are related to the investigated activity. Set when `ObservationType` is `RELATED_FINDINGS`.
Type: [RelatedFindings](API_RelatedFindings.md) object
Required: No

 ** representativeResources **   <a name="guardduty-Type-ObservationRecord-representativeResources"></a>
Representative findings for the affected resources, one finding for each resource. Set when `ObservationType` is `REPRESENTATIVE_RESOURCE`.
Type: Array of [RepresentativeFinding](API_RepresentativeFinding.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** resource **   <a name="guardduty-Type-ObservationRecord-resource"></a>
Details about an affected resource. Set when `ObservationType` is `RESOURCE`.
Type: [InvestigationResource](API_InvestigationResource.md) object
Required: No

 ** runtimeSignals **   <a name="guardduty-Type-ObservationRecord-runtimeSignals"></a>
A summary of runtime signals. Set when `ObservationType` is `RUNTIME_SIGNALS`.
Type: [RuntimeSignals](API_RuntimeSignals.md) object
Required: No

 ** s3Activity **   <a name="guardduty-Type-ObservationRecord-s3Activity"></a>
Details about Amazon S3 activity. Set when `ObservationType` is `S3_ACTIVITY`.
Type: [S3Activity](API_S3Activity.md) object
Required: No

## See Also
<a name="API_ObservationRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ObservationRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ObservationRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ObservationRecord)
