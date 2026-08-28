---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EcsClusterDetails.html
---

# EcsClusterDetails
<a name="API_EcsClusterDetails"></a>

Contains information about the details of the ECS Cluster.

## Contents
<a name="API_EcsClusterDetails_Contents"></a>

 ** activeServicesCount **   <a name="guardduty-Type-EcsClusterDetails-activeServicesCount"></a>
The number of services that are running on the cluster in an ACTIVE state.
Type: Integer
Required: No

 ** arn **   <a name="guardduty-Type-EcsClusterDetails-arn"></a>
The Amazon Resource Name (ARN) that identifies the cluster.
Type: String
Required: No

 ** name **   <a name="guardduty-Type-EcsClusterDetails-name"></a>
The name of the ECS Cluster.
Type: String
Required: No

 ** registeredContainerInstancesCount **   <a name="guardduty-Type-EcsClusterDetails-registeredContainerInstancesCount"></a>
The number of container instances registered into the cluster.
Type: Integer
Required: No

 ** runningTasksCount **   <a name="guardduty-Type-EcsClusterDetails-runningTasksCount"></a>
The number of tasks in the cluster that are in the RUNNING state.
Type: Integer
Required: No

 ** status **   <a name="guardduty-Type-EcsClusterDetails-status"></a>
The status of the ECS cluster.
Type: String
Required: No

 ** tags **   <a name="guardduty-Type-EcsClusterDetails-tags"></a>
The tags of the ECS Cluster.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** taskDetails **   <a name="guardduty-Type-EcsClusterDetails-taskDetails"></a>
Contains information about the details of the ECS Task.
Type: [EcsTaskDetails](API_EcsTaskDetails.md) object
Required: No

## See Also
<a name="API_EcsClusterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/EcsClusterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/EcsClusterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/EcsClusterDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
