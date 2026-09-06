---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This guidance uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this guidance.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this guidance using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ Logs and metrics from all Druid components are gathered and stored in CloudWatch.
+ A comprehensive CloudWatch dashboard is provided to monitor the operational status of underlying services.
+ Alarms are set up within CloudWatch to provide timely notifications for issues or anomalies.
+ Server access logging is enabled to provide detail records for the requests that are made to an Amazon S3 bucket.
+  [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) [flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) are enabled to monitor IP traffic both incoming and outgoing through network interfaces in your VPC Security.

## Security
<a name="security"></a>

This section describes how we architected this guidance using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ Multiple authentication schemas are supported including basic authentication, OIDC authentication, and LDAP authentication.
+ All inter service communications use [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles. Communications between EC2 instances hosting the Druid process and Aurora Postgres uses basic authentication and does not use IAM.
+ All IAM roles used by the guidance follow the least privilege access principle. They only contain the minimum permissions required so that the service can function properly.
+ AWS WAF is associated with AWS ALB to protect the Druid cluster from common application-layer exploits. AWS WAF is only provisioned and associated with the Application Load Balancer (ALB) when it is configured to be internet-facing and in the public mode.
+ All data stored in Amazon Aurora, [AWS Backup](https://aws.amazon.com/backup/), and Amazon S3 buckets have encryption at REST with customer managed keys.
+ All communication between Apache Druid and AWS service endpoints is covered by TLS.
+ TLS connectivity is implemented within the Druid cluster, as well as from the Druid cluster to the rest of the supported AWS services.
+ VPC endpoints are introduced to privately connect to supported AWS services.

## Reliability
<a name="reliability"></a>

This section describes how we architected this guidance using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ Amazon EC2 Auto Scaling is used to distribute instances across Availability Zones, and replace the failed instances automatically.
+ The database-first migration strategy allows for cluster restoration using existing backups of the metadata store and deep storage.
+ The guidance stores data in Amazon S3 so it persists in multiple Availability Zones by default.
+ AWS Backup is used to regularly backup the metadata store at defined intervals.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this guidance using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ The guidance supports AWS Fargate for serverless compute and Aurora PostgreSQL Serverless.
+ You can deploy the guidance in any AWS Region that supports the required AWS services.
+ The guidance provides versatile Automatic scaling policies, including CPU utilization, request per second, and scheduled scaling.
+ Developed using AWS CDK and managed through AWS CloudFormation stacks, it follows a complete Infrastructure-as-Code (IAC) approach, simplifying upgrades and resource management.
+ The guidance maximizes the utilization of AWS Managed Services. For more details, refer to the [AWS services used in this guidance](aws-services-in-this-solution.md) section.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this guidance using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ The guidance offers support for various EC2 instance types, including Graviton-based EC2 instances.
+ It supports a full serverless architecture by leveraging AWS Fargate and Aurora PostgreSQL Serverless.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this guidance using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ Support for Graviton-based EC2 instances aids in minimizing your carbon footprint and aligning with sustainability objectives.
+ Amazon EC2 Auto Scaling is used to scale your workloads dynamically. The predicative auto scaling is used to proactively scale as you anticipate predicted and planned changes in demand.
