---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CoverageEcsClusterDetails.html
---

# CoverageEcsClusterDetails
<a name="API_CoverageEcsClusterDetails"></a>

Contains information about Amazon ECS cluster runtime coverage details.

## Contents
<a name="API_CoverageEcsClusterDetails_Contents"></a>

 ** clusterName **   <a name="guardduty-Type-CoverageEcsClusterDetails-clusterName"></a>
The name of the Amazon ECS cluster.
Type: String
Required: No

 ** containerInstanceDetails **   <a name="guardduty-Type-CoverageEcsClusterDetails-containerInstanceDetails"></a>
Information about the Amazon ECS container running on Amazon EC2 instance.
Type: [ContainerInstanceDetails](API_ContainerInstanceDetails.md) object
Required: No

 ** fargateDetails **   <a name="guardduty-Type-CoverageEcsClusterDetails-fargateDetails"></a>
Information about the Fargate details associated with the Amazon ECS cluster.
Type: [FargateDetails](API_FargateDetails.md) object
Required: No

## See Also
<a name="API_CoverageEcsClusterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CoverageEcsClusterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CoverageEcsClusterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CoverageEcsClusterDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
