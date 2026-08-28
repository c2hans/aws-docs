---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EcsCluster.html
---

# EcsCluster
<a name="API_EcsCluster"></a>

Contains information about the Amazon ECS cluster involved in a GuardDuty finding, including cluster identification and status.

## Contents
<a name="API_EcsCluster_Contents"></a>

 ** ec2InstanceUids **   <a name="guardduty-Type-EcsCluster-ec2InstanceUids"></a>
A list of unique identifiers for the Amazon EC2 instances that serve as container instances in the Amazon ECS cluster.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** status **   <a name="guardduty-Type-EcsCluster-status"></a>
The current status of the Amazon ECS cluster.
Type: String
Valid Values: `ACTIVE | PROVISIONING | DEPROVISIONING | FAILED | INACTIVE`
Required: No

## See Also
<a name="API_EcsCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/EcsCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/EcsCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/EcsCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
