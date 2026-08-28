---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Service.html
---

# Service
<a name="API_Service"></a>

Contains additional information about the generated finding.

## Contents
<a name="API_Service_Contents"></a>

 ** action **   <a name="guardduty-Type-Service-action"></a>
Information about the activity that is described in a finding.
Type: [Action](API_Action.md) object
Required: No

 ** additionalInfo **   <a name="guardduty-Type-Service-additionalInfo"></a>
Contains additional information about the generated finding.
Type: [ServiceAdditionalInfo](API_ServiceAdditionalInfo.md) object
Required: No

 ** archived **   <a name="guardduty-Type-Service-archived"></a>
Indicates whether this finding is archived.
Type: Boolean
Required: No

 ** count **   <a name="guardduty-Type-Service-count"></a>
The total count of the occurrences of this finding type.
Type: Integer
Required: No

 ** detection **   <a name="guardduty-Type-Service-detection"></a>
Contains information about the detected unusual behavior.
Type: [Detection](API_Detection.md) object
Required: No

 ** detectorId **   <a name="guardduty-Type-Service-detectorId"></a>
The detector ID for the GuardDuty service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** ebsVolumeScanDetails **   <a name="guardduty-Type-Service-ebsVolumeScanDetails"></a>
Returns details from the malware scan that created a finding.
Type: [EbsVolumeScanDetails](API_EbsVolumeScanDetails.md) object
Required: No

 ** eventFirstSeen **   <a name="guardduty-Type-Service-eventFirstSeen"></a>
The first-seen timestamp of the activity that prompted GuardDuty to generate this finding.
Type: String
Required: No

 ** eventLastSeen **   <a name="guardduty-Type-Service-eventLastSeen"></a>
The last-seen timestamp of the activity that prompted GuardDuty to generate this finding.
Type: String
Required: No

 ** evidence **   <a name="guardduty-Type-Service-evidence"></a>
An evidence object associated with the service.
Type: [Evidence](API_Evidence.md) object
Required: No

 ** featureName **   <a name="guardduty-Type-Service-featureName"></a>
The name of the feature that generated a finding.
Type: String
Required: No

 ** malwareScanDetails **   <a name="guardduty-Type-Service-malwareScanDetails"></a>
Returns details from the malware scan that generated a GuardDuty finding.
Type: [MalwareScanDetails](API_MalwareScanDetails.md) object
Required: No

 ** resourceRole **   <a name="guardduty-Type-Service-resourceRole"></a>
The resource role information for this finding.
Type: String
Required: No

 ** runtimeDetails **   <a name="guardduty-Type-Service-runtimeDetails"></a>
Information about the process and any required context values for a specific finding
Type: [RuntimeDetails](API_RuntimeDetails.md) object
Required: No

 ** serviceName **   <a name="guardduty-Type-Service-serviceName"></a>
The name of the AWS service (GuardDuty) that generated a finding.
Type: String
Required: No

 ** userFeedback **   <a name="guardduty-Type-Service-userFeedback"></a>
Feedback that was submitted about the finding.
Type: String
Required: No

## See Also
<a name="API_Service_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Service)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Service)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Service)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
