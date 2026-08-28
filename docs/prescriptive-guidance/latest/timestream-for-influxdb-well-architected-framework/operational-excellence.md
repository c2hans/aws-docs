---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/timestream-for-influxdb-well-architected-framework/operational-excellence.html
---

# Operational excellence pillar
<a name="operational-excellence"></a>

The [operational excellence](https://docs.aws.amazon.com/wellarchitected/latest/framework/operational-excellence.html) pillar of the AWS Well-Architected Framework focuses on running and monitoring systems, and continually improving processes and procedures to deliver business value. The operational excellence pillar includes the ability to support development and run workloads effectively, and to gain insight into their operation.

You can reduce operational complexity through self-healing workloads, which detect and remediate most issues without human intervention. To work toward this goal, follow the best practices described in this section. Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) metrics for Amazon Timestream for InfluxDB, the InfluxDB native metrics endpoint, APIs, and mechanisms to respond when your workload deviates from expected behavior.

This discussion of the operational excellence pillar focuses on the following key areas:
+ Infrastructure as code (IaC)
+ Change management
+ Resiliency strategies
+ Incident management
+ Logging and monitoring for auditing purposes

## Automate deployment by using an IaC approach
<a name="iac"></a>

Best practices for automating deployment on Timestream for InfluxDB by using IaC include the following:
+ Apply IaC to deploy Timestream for InfluxDB whenever possible. For consistent environment configuration, use an [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) template, [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html), or [HashiCorp Terraform](https://aws.amazon.com/blogs/apn/terraform-beyond-the-basics-with-aws/) to create all the required resources for your instance.
+ Automate Timestream for InfluxDB operational procedures, such as resizing instances.
+ Use tags to add metadata to your Timestream for InfluxDB resources, and track usage based on tags. For more information, see [Tagging Amazon Timestream for InfluxDB](https://docs.aws.amazon.com/timestream/latest/developerguide/tagging-keyspaces-influxdb.html).

## Make frequent, small, reversible changes
<a name="change-management"></a>

The following recommendations focus on small, reversible changes to minimize complexity and reduce the likelihood of workload disruption:
+ Store IaC templates and scripts in a source-control service, such as GitHub or GitLab. Do not store AWS credentials in source control.
+ Require IaC deployments to use a continuous integration and continuous delivery (CI/CD) service, such as [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) or [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html). These services compile, test, and deploy code in a non-production environment that contains an ephemeral InfluxDB instance before affecting your production InfluxDB instance.
+ Test infrastructure and application queries in a lower environment before you deploy them to production. This minimizes the likelihood of a disruption and helps ensure that they perform well with your workload and scale.

## Anticipate failure
<a name="resilience"></a>

A self-healing infrastructure exemplifies operational excellence by anticipating failure and attempting to resolve any issues without intervention. The following recommendations help you achieve that maturity with Timestream for InfluxDB:
+ Use metrics to monitor your memory, CPU, and storage usage. You can set up CloudWatch to notify you when usage patterns change or when you approach the capacity of your deployment. This way, you can maintain system performance and availability.
+ Scale up your DB instance when you are approaching the resource limit. You should have some buffer in storage and memory to accommodate unforeseen increases in demand from your applications.
+ If your database workload requires more I/O than you have provisioned, recovery after a failover or database failure will be slow. To increase the I/O capacity of a DB instance, migrate to a different DB instance that has higher I/O capacity.
+ If your client application is caching the DNS data of your DB instances, set a time-to-live (TTL) value of less than 30 seconds. The underlying IP address of a DB instance can change after a failover. Caching the DNS data for an extended time can lead to connection failures. Your application might try to connect to an IP address that's no longer in service.
+ If your application requires surviving a complete AWS Region outage, consider setting up replication or write to a different Region as part of your disaster recovery (DR) plans. Understand the limitations while setting up replication. For more information about replication, see the [InfluxDB documentation](https://docs.influxdata.com/influxdb/cloud/write-data/replication/replicate-data/).

## Learn from all operational failures
<a name="incident-management"></a>

A self-healing infrastructure is a long-term effort that you develop in iterations when rare problems occur or responses are not as effective as you want. To focus on achieving a self-healing infrastructure, adopt the following practices:
+ Drive improvement by learning from all failures.
+ Share what is learned across teams and the organization. If multiple teams within an organization use Timestream for InfluxDB, create a common chatroom or user group to share lessons learned and best practices.

## Use logging capabilities to monitor for unauthorized or anomalous activity
<a name="logging-monitoring"></a>

To observe anomalous performance and activity patterns, consider the following practices:
+ Enable [log delivery](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influx-managing-view-influx-logs.html) to store InfluxDB logs in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). InfluxDB logs record information that can help to check the following:
  + [Data plane API events](https://docs.influxdata.com/influxdb/v2/reference/api/)
  + Response times
  + Compaction details
  + Any critical errors or warnings encountered by the system

  Review the logs for unauthorized access or anomalies. Overall, logging provides diagnostic information for troubleshooting.
+ Timestream for InfluxDB supports logging control plane actions by using AWS CloudTrail. For more information, see [Logging Timestream for InfluxDB API calls with AWS CloudTrail](https://docs.aws.amazon.com/timestream/latest/developerguide/logging-using-cloudtrail-influxdb.html).
+ You can monitor `CPUUtilization`, `MemoryUtilization`, and `DiskUtilization` metrics from **Timestream/InfluxDB >** <**Namespace**> in CloudWatch.

For more information, see the [Timestream for InfluxDB documentation](https://docs.aws.amazon.com/timestream/latest/developerguide/monitoring-influxdb.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
