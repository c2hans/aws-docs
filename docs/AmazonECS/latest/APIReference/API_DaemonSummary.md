---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonSummary.html
---

# DaemonSummary
<a name="API_DaemonSummary"></a>

A summary of a daemon.

## Contents
<a name="API_DaemonSummary_Contents"></a>

 ** createdAt **   <a name="ECS-Type-DaemonSummary-createdAt"></a>
The Unix timestamp for the time when the daemon was created.
Type: Timestamp
Required: No

 ** daemonArn **   <a name="ECS-Type-DaemonSummary-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon.
Type: String
Required: No

 ** status **   <a name="ECS-Type-DaemonSummary-status"></a>
The status of the daemon.
Type: String
Valid Values: `ACTIVE | DELETE_IN_PROGRESS`
Required: No

 ** updatedAt **   <a name="ECS-Type-DaemonSummary-updatedAt"></a>
The Unix timestamp for the time when the daemon was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DaemonSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
