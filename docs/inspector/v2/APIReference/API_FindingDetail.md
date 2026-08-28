---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FindingDetail.html
---

# FindingDetail
<a name="API_FindingDetail"></a>

Details of the vulnerability identified in a finding.

## Contents
<a name="API_FindingDetail_Contents"></a>

 ** cisaData **   <a name="inspector2-Type-FindingDetail-cisaData"></a>
The Cybersecurity and Infrastructure Security Agency (CISA) details for a specific vulnerability.
Type: [CisaData](API_CisaData.md) object
Required: No

 ** cwes **   <a name="inspector2-Type-FindingDetail-cwes"></a>
The Common Weakness Enumerations (CWEs) associated with the vulnerability.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 0.
Required: No

 ** epssScore **   <a name="inspector2-Type-FindingDetail-epssScore"></a>
The Exploit Prediction Scoring System (EPSS) score of the vulnerability.
Type: Double
Required: No

 ** evidences **   <a name="inspector2-Type-FindingDetail-evidences"></a>
Information on the evidence of the vulnerability.
Type: Array of [Evidence](API_Evidence.md) objects
Required: No

 ** exploitObserved **   <a name="inspector2-Type-FindingDetail-exploitObserved"></a>
Contains information on when this exploit was observed.
Type: [ExploitObserved](API_ExploitObserved.md) object
Required: No

 ** findingArn **   <a name="inspector2-Type-FindingDetail-findingArn"></a>
The finding ARN that the vulnerability details are associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:finding/[a-f0-9]{32}`
Required: No

 ** referenceUrls **   <a name="inspector2-Type-FindingDetail-referenceUrls"></a>
The reference URLs for the vulnerability data.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0.
Required: No

 ** riskScore **   <a name="inspector2-Type-FindingDetail-riskScore"></a>
The risk score of the vulnerability.
Type: Integer
Required: No

 ** tools **   <a name="inspector2-Type-FindingDetail-tools"></a>
The known malware tools or kits that can exploit the vulnerability.
Type: Array of strings
Length Constraints: Minimum length of 0.
Required: No

 ** ttps **   <a name="inspector2-Type-FindingDetail-ttps"></a>
The MITRE adversary tactics, techniques, or procedures (TTPs) associated with the vulnerability.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 0. Maximum length of 30.
Required: No

## See Also
<a name="API_FindingDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FindingDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FindingDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FindingDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
