---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CoverageResource.html
---

# CoverageResource
<a name="API_CoverageResource"></a>

Information about the resource of the GuardDuty account.

## Contents
<a name="API_CoverageResource_Contents"></a>

 ** accountId **   <a name="guardduty-Type-CoverageResource-accountId"></a>
The unique ID of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** coverageStatus **   <a name="guardduty-Type-CoverageResource-coverageStatus"></a>
Represents the status of the EKS cluster coverage.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

 ** detectorId **   <a name="guardduty-Type-CoverageResource-detectorId"></a>
The unique ID of the GuardDuty detector associated with the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** issue **   <a name="guardduty-Type-CoverageResource-issue"></a>
Represents the reason why a coverage status was `UNHEALTHY` for the EKS cluster.
Type: String
Required: No

 ** resourceDetails **   <a name="guardduty-Type-CoverageResource-resourceDetails"></a>
Information about the resource for which the coverage statistics are retrieved.
Type: [CoverageResourceDetails](API_CoverageResourceDetails.md) object
Required: No

 ** resourceId **   <a name="guardduty-Type-CoverageResource-resourceId"></a>
The unique ID of the resource.
Type: String
Required: No

 ** updatedAt **   <a name="guardduty-Type-CoverageResource-updatedAt"></a>
The timestamp at which the coverage details for the resource were last updated. This is in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_CoverageResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CoverageResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CoverageResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CoverageResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
