---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Finding.html
---

# Finding
<a name="API_Finding"></a>

Details about an Amazon Inspector finding.

## Contents
<a name="API_Finding_Contents"></a>

 ** awsAccountId **   <a name="inspector2-Type-Finding-awsAccountId"></a>
The AWS account ID associated with the finding.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** description **   <a name="inspector2-Type-Finding-description"></a>
The description of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** findingArn **   <a name="inspector2-Type-Finding-findingArn"></a>
The Amazon Resource Number (ARN) of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:finding/[a-f0-9]{32}`
Required: Yes

 ** firstObservedAt **   <a name="inspector2-Type-Finding-firstObservedAt"></a>
The date and time that the finding was first observed.
Type: Timestamp
Required: Yes

 ** lastObservedAt **   <a name="inspector2-Type-Finding-lastObservedAt"></a>
 The date and time the finding was last observed. This timestamp for this field remains unchanged until a finding is updated.
Type: Timestamp
Required: Yes

 ** remediation **   <a name="inspector2-Type-Finding-remediation"></a>
An object that contains the details about how to remediate a finding.
Type: [Remediation](API_Remediation.md) object
Required: Yes

 ** resources **   <a name="inspector2-Type-Finding-resources"></a>
Contains information on the resources involved in a finding. The `resource` value determines the valid values for `type` in your request. For more information, see [Finding types](https://docs.aws.amazon.com/inspector/latest/user/findings-types.html) in the Amazon Inspector user guide.
Type: Array of [Resource](API_Resource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** severity **   <a name="inspector2-Type-Finding-severity"></a>
The severity of the finding. `UNTRIAGED` applies to `PACKAGE_VULNERABILITY` type findings that the vendor has not assigned a severity yet. For more information, see [Severity levels for findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html) in the Amazon Inspector user guide.
Type: String
Valid Values: `INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL | UNTRIAGED`
Required: Yes

 ** status **   <a name="inspector2-Type-Finding-status"></a>
The status of the finding.
Type: String
Valid Values: `ACTIVE | SUPPRESSED | CLOSED`
Required: Yes

 ** type **   <a name="inspector2-Type-Finding-type"></a>
The type of the finding. The `type` value determines the valid values for `resource` in your request. For more information, see [Finding types](https://docs.aws.amazon.com/inspector/latest/user/findings-types.html) in the Amazon Inspector user guide.
Type: String
Valid Values: `NETWORK_REACHABILITY | PACKAGE_VULNERABILITY | CODE_VULNERABILITY`
Required: Yes

 ** codeVulnerabilityDetails **   <a name="inspector2-Type-Finding-codeVulnerabilityDetails"></a>
Details about the code vulnerability identified in a Lambda function used to filter findings.
Type: [CodeVulnerabilityDetails](API_CodeVulnerabilityDetails.md) object
Required: No

 ** epss **   <a name="inspector2-Type-Finding-epss"></a>
The finding's EPSS score.
Type: [EpssDetails](API_EpssDetails.md) object
Required: No

 ** exploitabilityDetails **   <a name="inspector2-Type-Finding-exploitabilityDetails"></a>
The details of an exploit available for a finding discovered in your environment.
Type: [ExploitabilityDetails](API_ExploitabilityDetails.md) object
Required: No

 ** exploitAvailable **   <a name="inspector2-Type-Finding-exploitAvailable"></a>
If a finding discovered in your environment has an exploit available.
Type: String
Valid Values: `YES | NO`
Required: No

 ** fixAvailable **   <a name="inspector2-Type-Finding-fixAvailable"></a>
Details on whether a fix is available through a version update. This value can be `YES`, `NO`, or `PARTIAL`. A `PARTIAL` fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.
Type: String
Valid Values: `YES | NO | PARTIAL`
Required: No

 ** inspectorScore **   <a name="inspector2-Type-Finding-inspectorScore"></a>
The Amazon Inspector score given to the finding.
Type: Double
Required: No

 ** inspectorScoreDetails **   <a name="inspector2-Type-Finding-inspectorScoreDetails"></a>
An object that contains details of the Amazon Inspector score.
Type: [InspectorScoreDetails](API_InspectorScoreDetails.md) object
Required: No

 ** networkReachabilityDetails **   <a name="inspector2-Type-Finding-networkReachabilityDetails"></a>
An object that contains the details of a network reachability finding.
Type: [NetworkReachabilityDetails](API_NetworkReachabilityDetails.md) object
Required: No

 ** packageVulnerabilityDetails **   <a name="inspector2-Type-Finding-packageVulnerabilityDetails"></a>
An object that contains the details of a package vulnerability finding.
Type: [PackageVulnerabilityDetails](API_PackageVulnerabilityDetails.md) object
Required: No

 ** title **   <a name="inspector2-Type-Finding-title"></a>
The title of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** updatedAt **   <a name="inspector2-Type-Finding-updatedAt"></a>
The date and time the finding was last updated at.
Type: Timestamp
Required: No

## See Also
<a name="API_Finding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Finding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Finding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Finding)
