---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_LicenseEndpointSummary.html
---

# LicenseEndpointSummary
<a name="API_LicenseEndpointSummary"></a>

The details for a license endpoint.

## Contents
<a name="API_LicenseEndpointSummary_Contents"></a>

 ** licenseEndpointId **   <a name="deadlinecloud-Type-LicenseEndpointSummary-licenseEndpointId"></a>
The license endpoint ID.
Type: String
Pattern: `le-[0-9a-f]{32}`
Required: No

 ** status **   <a name="deadlinecloud-Type-LicenseEndpointSummary-status"></a>
The status of the license endpoint.
Type: String
Valid Values: `CREATE_IN_PROGRESS | DELETE_IN_PROGRESS | READY | NOT_READY`
Required: No

 ** statusMessage **   <a name="deadlinecloud-Type-LicenseEndpointSummary-statusMessage"></a>
The status message of the license endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** vpcId **   <a name="deadlinecloud-Type-LicenseEndpointSummary-vpcId"></a>
The VPC (virtual private cloud) ID associated with the license endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `vpc-[\w]{1,120}`
Required: No

## See Also
<a name="API_LicenseEndpointSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/LicenseEndpointSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/LicenseEndpointSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/LicenseEndpointSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
