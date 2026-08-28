---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ECSTaskSet.html
---

# ECSTaskSet
<a name="API_ECSTaskSet"></a>

 Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic. An AWS CodeDeploy application that uses the Amazon ECS compute platform deploys a containerized application in an Amazon ECS service as a task set.

## Contents
<a name="API_ECSTaskSet_Contents"></a>

 ** desiredCount **   <a name="CodeDeploy-Type-ECSTaskSet-desiredCount"></a>
 The number of tasks in a task set. During a deployment that uses the Amazon ECS compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses this value to determine how many tasks to create. After the updated task set is created, CodeDeploy shifts traffic to the new task set.
Type: Long
Required: No

 ** identifer **   <a name="CodeDeploy-Type-ECSTaskSet-identifer"></a>
 A unique ID of an `ECSTaskSet`.
Type: String
Required: No

 ** pendingCount **   <a name="CodeDeploy-Type-ECSTaskSet-pendingCount"></a>
 The number of tasks in the task set that are in the `PENDING` status during an Amazon ECS deployment. A task in the `PENDING` state is preparing to enter the `RUNNING` state. A task set enters the `PENDING` status when it launches for the first time, or when it is restarted after being in the `STOPPED` state.
Type: Long
Required: No

 ** runningCount **   <a name="CodeDeploy-Type-ECSTaskSet-runningCount"></a>
 The number of tasks in the task set that are in the `RUNNING` status during an Amazon ECS deployment. A task in the `RUNNING` state is running and ready for use.
Type: Long
Required: No

 ** status **   <a name="CodeDeploy-Type-ECSTaskSet-status"></a>
 The status of the task set. There are three valid task set statuses:
+  `PRIMARY`: Indicates the task set is serving production traffic.
+  `ACTIVE`: Indicates the task set is not serving production traffic.
+  `DRAINING`: Indicates the tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.
Type: String
Required: No

 ** targetGroup **   <a name="CodeDeploy-Type-ECSTaskSet-targetGroup"></a>
 The target group associated with the task set. The target group is used by AWS CodeDeploy to manage traffic to a task set.
Type: [TargetGroupInfo](API_TargetGroupInfo.md) object
Required: No

 ** taskSetLabel **   <a name="CodeDeploy-Type-ECSTaskSet-taskSetLabel"></a>
 A label that identifies whether the ECS task set is an original target (`BLUE`) or a replacement target (`GREEN`).
Type: String
Valid Values: `Blue | Green`
Required: No

 ** trafficWeight **   <a name="CodeDeploy-Type-ECSTaskSet-trafficWeight"></a>
 The percentage of traffic served by this task set.
Type: Double
Required: No

## See Also
<a name="API_ECSTaskSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ECSTaskSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ECSTaskSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ECSTaskSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
