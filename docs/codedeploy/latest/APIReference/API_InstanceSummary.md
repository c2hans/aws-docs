---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_InstanceSummary.html
---

# InstanceSummary
<a name="API_InstanceSummary"></a>

 *This data type has been deprecated.*

Information about an instance in a deployment.

## Contents
<a name="API_InstanceSummary_Contents"></a>

 ** deploymentId **   <a name="CodeDeploy-Type-InstanceSummary-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: No

 ** instanceId **   <a name="CodeDeploy-Type-InstanceSummary-instanceId"></a>
The instance ID.
Type: String
Required: No

 ** instanceType **   <a name="CodeDeploy-Type-InstanceSummary-instanceType"></a>
Information about which environment an instance belongs to in a blue/green deployment.
+ BLUE: The instance is part of the original environment.
+ GREEN: The instance is part of the replacement environment.
Type: String
Valid Values: `Blue | Green`
Required: No

 ** lastUpdatedAt **   <a name="CodeDeploy-Type-InstanceSummary-lastUpdatedAt"></a>
A timestamp that indicates when the instance information was last updated.
Type: Timestamp
Required: No

 ** lifecycleEvents **   <a name="CodeDeploy-Type-InstanceSummary-lifecycleEvents"></a>
A list of lifecycle events for this instance.
Type: Array of [LifecycleEvent](API_LifecycleEvent.md) objects
Required: No

 ** status **   <a name="CodeDeploy-Type-InstanceSummary-status"></a>
 *This member has been deprecated.*
The deployment status for this instance:
+  `Pending`: The deployment is pending for this instance.
+  `In Progress`: The deployment is in progress for this instance.
+  `Succeeded`: The deployment has succeeded for this instance.
+  `Failed`: The deployment has failed for this instance.
+  `Skipped`: The deployment has been skipped for this instance.
+  `Unknown`: The deployment status is unknown for this instance.
Type: String
Valid Values: `Pending | InProgress | Succeeded | Failed | Skipped | Unknown | Ready`
Required: No

## See Also
<a name="API_InstanceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/InstanceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/InstanceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/InstanceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
