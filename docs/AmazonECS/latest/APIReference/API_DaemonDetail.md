---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonDetail.html
---

# DaemonDetail
<a name="API_DaemonDetail"></a>

The detailed information about a daemon.

## Contents
<a name="API_DaemonDetail_Contents"></a>

 ** clusterArn **   <a name="ECS-Type-DaemonDetail-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster that the daemon is running in.
Type: String
Required: No

 ** createdAt **   <a name="ECS-Type-DaemonDetail-createdAt"></a>
The Unix timestamp for the time when the daemon was created.
Type: Timestamp
Required: No

 ** currentRevisions **   <a name="ECS-Type-DaemonDetail-currentRevisions"></a>
The current daemon revision details, including the running task counts per capacity provider.
Type: Array of [DaemonRevisionDetail](API_DaemonRevisionDetail.md) objects
Required: No

 ** daemonArn **   <a name="ECS-Type-DaemonDetail-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon.
Type: String
Required: No

 ** deploymentArn **   <a name="ECS-Type-DaemonDetail-deploymentArn"></a>
The Amazon Resource Name (ARN) of the most recent daemon deployment.
Type: String
Required: No

 ** status **   <a name="ECS-Type-DaemonDetail-status"></a>
The status of the daemon.
Type: String
Valid Values: `ACTIVE | DELETE_IN_PROGRESS`
Required: No

 ** updatedAt **   <a name="ECS-Type-DaemonDetail-updatedAt"></a>
The Unix timestamp for the time when the daemon was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DaemonDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
