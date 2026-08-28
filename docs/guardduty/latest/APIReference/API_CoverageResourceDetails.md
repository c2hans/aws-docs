---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CoverageResourceDetails.html
---

# CoverageResourceDetails
<a name="API_CoverageResourceDetails"></a>

Information about the resource for each individual EKS cluster.

## Contents
<a name="API_CoverageResourceDetails_Contents"></a>

 ** ec2InstanceDetails **   <a name="guardduty-Type-CoverageResourceDetails-ec2InstanceDetails"></a>
Information about the Amazon EC2 instance assessed for runtime coverage.
Type: [CoverageEc2InstanceDetails](API_CoverageEc2InstanceDetails.md) object
Required: No

 ** ecsClusterDetails **   <a name="guardduty-Type-CoverageResourceDetails-ecsClusterDetails"></a>
Information about the Amazon ECS cluster that is assessed for runtime coverage.
Type: [CoverageEcsClusterDetails](API_CoverageEcsClusterDetails.md) object
Required: No

 ** eksClusterDetails **   <a name="guardduty-Type-CoverageResourceDetails-eksClusterDetails"></a>
EKS cluster details involved in the coverage statistics.
Type: [CoverageEksClusterDetails](API_CoverageEksClusterDetails.md) object
Required: No

 ** resourceType **   <a name="guardduty-Type-CoverageResourceDetails-resourceType"></a>
The type of AWS resource.
Type: String
Valid Values: `EKS | ECS | EC2`
Required: No

## See Also
<a name="API_CoverageResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CoverageResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CoverageResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CoverageResourceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
