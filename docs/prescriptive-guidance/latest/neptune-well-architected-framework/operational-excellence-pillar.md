---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-well-architected-framework/operational-excellence-pillar.html
---

# Operational excellence pillar
<a name="operational-excellence-pillar"></a>

The [operational excellence](https://docs.aws.amazon.com/wellarchitected/latest/framework/operational-excellence.html) pillar of the AWS Well-Architected Framework focuses on running and monitoring systems, and continually improving processes and procedures. It includes the ability to support development and run workloads effectively, gain insight into their operation, and continuously improve supporting processes and procedures to deliver business value. You can reduce operational complexity through self-healing workloads, which detect and remediate most issues without human intervention. You can work toward this goal by following the best practices described in this section. Use Amazon Neptune metrics, APIs, and mechanisms to properly respond when your workload deviates from expected behavior.

This discussion of the operational excellence pillar focuses on the following key areas:
+ Infrastructure as code (IaC)
+ Change management
+ Resiliency strategies
+ Incident management
+ Audit reporting for compliance
+ Logging and monitoring

## Automate deployment using an IaC approach
<a name="iac"></a>

Best practices for automating deployment on Neptune using IaC include the following:
+ Apply infrastructure as- code (IaC) to deploy Neptune clusters whenever possible. For consistent environment configuration, use an [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) template, [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html), or [HashiCorp Terraform](https://aws.amazon.com/blogs/apn/terraform-beyond-the-basics-with-aws/) to create all the required resources for your cluster.
+ Automate Neptune operational procedures, such as resizing instances, adding or removing read replicas, or doing manual failovers on global tables, whenever possible.
+ Store connection strings externally from your client. Use extract, transform, and load (ETL) processes to facilitate blue/green deployment strategies, disaster recovery (DR), and near-zero downtime migrations to new clusters. Connection strings can be stored in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), or any location where they can be changed dynamically.
+ Use tags to add metadata to your Neptune resources, and track usage based on tags. For more information, see [Tagging Amazon Neptune Resources](https://docs.aws.amazon.com/neptune/latest/userguide/tagging.html).

## Make frequent, small, reversible changes
<a name="changes"></a>

The following recommendations focus on small, reversible changes to minimize complexity and reduce the likelihood of workload disruption:
+ Store IaC templates and scripts in a source control service, such as GitHub or GitLab.
**Important**
Do not store AWS credentials in source control.
+ Require IaC deployments to use a continuous integration and continuous delivery (CI/CD) service, such as [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) or [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html). These services compile, test, and deploy code in a non-production environment containing an ephemeral Neptune cluster before impacting [your production Amazon Neptune cluster](https://aws.amazon.com/blogs/database/automated-testing-of-amazon-neptune-data-access-with-apache-tinkerpop-gremlin/).
+ Test infrastructure and application queries in a lower environment before you deploy them to production. This will minimize the likelihood of a disruption and help ensure they perform well with your workload and scale.

## Anticipate failure
<a name="anticipate-failure"></a>

A self-healing infrastructure exemplifies operational excellence by anticipating failure and attempting to resolve any issues without intervention. The following recommendations help you achieve that maturity with Neptune:
+ Create a monitoring plan that uses Amazon CloudWatch metrics to monitor your DB instance's CPU and memory usage, and understand the usage patterns. Create CloudWatch dashboards and alarms for key metrics and the Neptune client responses found in your application logs. For more information about indicators of high or low CPU utilization, see [Using CloudWatch to monitor DB instance performance in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-monitoring-instances.html) in the Neptune documentation.

  If you frequently get out-of-memory exceptions on your queries, consider reducing the total number of nodes your query traverses or try using an instance from the `X2` family, which has a higher RAM-to-CPU ratio.
+ Set notifications to monitor the health of the Neptune cluster. For example, `BufferCacheHitRatio` should be constantly high (greater than 99.9 percent), whereas `MainRequestQueuePendingRequests` should be constantly low (ideally 0 but dependent on your requirements and latency tolerance).
+ Consider using read replicas to achieve high availability within Neptune. You should have at least two read replicas in different Availability Zones from the writer instance to ensure an instance is always available to serve read queries during a failover event.
+ Automatically scale read replicas based on utilization metrics. For more information, see [Auto-scaling the number of replicas in an Amazon Neptune DB cluster](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-autoscaling.html).
+ Test failover for your DB instance to understand how long the process takes for your use case.
+ If your application requires surviving a complete AWS Region outage, consider using [global databases](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-disaster-recovery.html) as part of your DR plans.

## Learn from all operational failures
<a name="learn"></a>

A self-healing infrastructure is a long-term effort that develops in iterations as rare problems occur or responses are not as effective as desired. Adopting the following practices drives focus toward that goal:
+ Drive improvement by learning from all failures.
+ Share what is learned across teams and the organization. If multiple teams within an organization use Neptune, create a common chatroom or user group to share learnings and best practices.

## Use logging capabilities to monitor for unauthorized or anomalous activity
<a name="logging"></a>

To observe anomalous performance and activity patterns, store logs in Amazon CloudWatch Logs. Consider the following best practices:
+ Enable [slow-query logging](https://docs.aws.amazon.com/neptune/latest/userguide/slow-query-logs.html). Regularly review the log and diagnose why certain queries are slow. Use the Neptune explain and profile endpoints for [Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html), [SPARQL](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-explain.html), or [openCypher ](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-explain.html)to gain insights into why these queries are slow.
+ [Enable Neptune audit logs](https://docs.aws.amazon.com/neptune/latest/userguide/auditing.html#auditing-enable), and regularly review the logs for unauthorized access or anomalies.
+ If you are using slow-query logging or audit logging, enable publishing to CloudWatch Logs. This will help you to avoid running out of disk space on instances. Neptune instances have limited log storage capacity and will overwrite older log files when log space is exceeded. CloudWatch Logs supports long-term retention of logs. The enhanced monitoring capabilities in CloudWatch Logs will improve your ability to query logs and diagnose issues.
+ To facilitate better analysis tools for your audit logs, you can configure a Neptune DB cluster to publish audit log data to a log group in CloudWatch Logs. With CloudWatch Logs, you can perform real-time analysis of the log data, use CloudWatch to create alarms and view metrics, and use CloudWatch Logs to store your log records in highly durable storage. For more information, see [Publishing Neptune logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html).
+ Neptune supports logging of control plane actions using AWS CloudTrail. For more information, see [Logging Amazon Neptune API Calls with AWS CloudTrail](https://docs.aws.amazon.com/neptune/latest/userguide/cloudtrail.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
