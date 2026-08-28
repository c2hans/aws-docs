---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-analytics-well-architected-framework/operational-excellence-pillar.html
---

# Operational excellence pillar
<a name="operational-excellence-pillar"></a>

The [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/operational-excellence.html) of the AWS Well-Architected Framework focuses on running and monitoring systems, and continually improving processes and procedures. It includes the ability to support development and run workloads effectively, gain insight into their operation, and continuously improve supporting processes and procedures to deliver business value. You can reduce operational complexity through self-healing workloads, which detect and remediate most issues without human intervention. You can work toward this goal by following the best practices described in this section, and use Amazon Neptune Analytics metrics, APIs, and mechanisms to properly respond when your workload deviates from expected behavior.

This discussion of the operational excellence pillar focuses on the following key areas:
+ Infrastructure as code (IaC)
+ Change management
+ Resiliency strategies
+ Incident management
+ Audit reporting for compliance
+ Logging and monitoring

## Automate deployment using an IaC approach
<a name="iac"></a>

Best practices for automating deployment on Neptune by using IaC include the following:
+ Apply IaC to deploy Neptune Analytics graphs and related resources. For consistent environment configuration, use the [support for Neptune Analytics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NeptuneGraph.html) provided by [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) to provision graphs and private endpoints.
+ Use CloudFormation to [provision Neptune notebook instances on Amazon SageMaker AI.](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/create-notebook-cfn.html) You can use notebooks to query and visualize data in a Neptune Analytics graph.
+ When you create a Neptune Analytics graph from an existing source, such as a Neptune database cluster or snapshot, or data files staged in Amazon Simple Storage Service (Amazon S3), monitor the [bulk import task](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-checking-details.html).
+ Automate Neptune Analytics operational procedures, such as [resizing the graph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UpdateGraph.html), deleting and snapshotting the graph, restoring the graph from a snapshot, and resetting and reloading the graph. Use the [Neptune Analytics API](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/Welcome.html), which is available through the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/) or [SDK](https://aws.amazon.com/developer/tools/)s.
+ Assess the required uptime of your graph. Analytics is often ephemeral; the graph is required only for the time you need to run algorithms. If this is the case, use the AWS CLI or SDKs to [snapshot and delete](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing.html#managing-deleting) the graph when it is no longer required. You can then [restore it from a snapshot](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/graph-snapshots.html#graph-snapshots-restoring) later, if necessary.
+ Store connection strings externally from your client. You can store connection strings in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), or any location where they can be changed dynamically.
+ [Use tags to add metadata](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-tagging.html) to your Neptune Analytics resources, and track usage based on tags. Tags help organize your resources. For example, you can apply a common tag to resources in a specific environment or application. You can also use tags to analyze billing of resource usage; for more information, see [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*. Additionally, you can use conditions in your AWS Identity and Access Management (IAM) policies to control access to AWS resources based on the tags used on that resource. You can do this by using the global `aws:ResourceTag/tag-key` condition key. For more information, see [Controlling access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-resources) in the *IAM User Guide*.

## Design for operations
<a name="design-ops"></a>

Adopt approaches to improve how you operate Neptune Analytics graphs:
+ Maintain separate Neptune Analytics graphs for development, test, and production use. These graphs might have different datasets, users, and operational controls.
+ Maintain separate Neptune Analytics graphs for different uses. For example, if two groups of analytical users require separate graphs with different timelines, models, performance and availability SLAs, and usage patterns, maintain separate graphs for each group.
+ Prepare users and operational staff for Neptune Analytics [maintenance updates](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-maintaining.html).

## Make frequent, small, reversible changes
<a name="frequent-changes"></a>

The following recommendations focus on small, reversible changes you can make to minimize complexity and reduce the likelihood of workload disruption:
+ Store IaC templates and scripts in a source control service such as GitHub or GitLab.
**Important**
Do not store AWS credentials in source control.
+ Require IaC deployments to use a continuous integration and continuous delivery (CI/CD) service such as [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) or [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html). Compile, test, and deploy code in a non-production Neptune Analytics environment before promoting it to a production graph.

## Implement observability for actionable insights
<a name="observability"></a>

Gain a comprehensive understanding of workload behavior, performance, reliability, cost, and health. The following recommendations help you gain that level of understanding in Neptune Analytics:
+ Monitor Amazon CloudWatch metrics for Neptune Analytics. From these metrics, you can determine the size of a graph (number of nodes, edges, and vectors, plus total byte size), CPU utilization, and query request and error rates.
+ Create CloudWatch dashboards and alarms for key metrics such as `NumQueuedRequestsPerSec`, `NumOpenCypherRequestsPerSec`, `GraphStorageUsagePercent`, `GraphSizeBytes`, and `CPUUtilization` as well as Neptune client responses found in your application logs.
+ Set notifications to monitor the health of the Neptune Analytics graph such as when graph size, request rate, or CPU utilization exceeds your threshold. For example, if `GraphStorageUsagePercent` has climbed to 90 percent on a graph you intend to grow significantly, decide whether to increase memory-optimized Neptune Capacity Unit (m-NCU) capacity. If current m-NCU is 128, increasing it to 256 will reduce storage by about 45 percent. If `NumQueuedRequestsPerSec` is often greater than zero, consider increasing m-NCU capacity to provide more compute capacity. Alternatively, you can reduce client-side concurrency.

## Learn from all operational failures
<a name="op-failure"></a>

A self-healing infrastructure is a long-term effort that develops in iterations as rare problems occur or responses are not as effective as desired. Adopting the following practices drives focus toward that goal:
+ Drive improvement by learning from all failures.
+ Share what is learned across teams and the organization. If multiple teams within your organization use Neptune, create a common chatroom or user group to share learnings and best practices.

## Use logging capabilities to monitor for unauthorized or anomalous activity
<a name="logging"></a>

Use logging to observe anomalous performance and activity patterns. Consider the following best practices:
+ Neptune Analytics supports logging of control plane actions by using AWS CloudTrail. For more information, see [Logging Neptune Analytics API calls using AWS CloudTrail](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/monitoring.html#monitoring-cloudtrail). Through this capability, you can track the creation, update, and deletion of Neptune Analytics resources. For robust monitoring and alerting, you can also integrate CloudTrail events with [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html). To enhance your analysis of Neptune Analytics service activity and identify changes in activities for an AWS account, you can [query CloudTrail logs by using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html). For example, you can use queries to identify trends and further isolate activity by attributes such as source IP address or user.
+ You can also use CloudTrail to [enable logging of Neptune Analytics data plane activities](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) such as query executions. You can view which queries are being run, their frequency, and their source. By default, CloudTrail doesn't log data events. Additional charges apply for data events. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/).
+ You can also log your application calls to Neptune Analytics in either the control plane or the data plane. For example, if you use the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to make queries, you can [enable debug-level logging](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/boto3.html) to obtain a trace of queries to the console or file. This is useful during development. We also recommend that you catch and log exceptions from your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
