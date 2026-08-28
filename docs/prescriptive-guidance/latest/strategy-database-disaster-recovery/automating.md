---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/automating.html
---

# Automating your disaster recovery strategy
<a name="automating"></a>

You can optionally choose to implement full or partial automation to gain better control of disaster recovery. If you're using the backup and restore DR option, you can automate your backups by using [AWS Backup](https://aws.amazon.com/backup/), which supports all Amazon RDS databases as well as DynamoDB, Amazon DocumentDB, and Amazon Neptune tables.

## Disaster event detection
<a name="detection"></a>

To shorten the recovery time, you can consider automating the detection of a Regionwide event, which can then initiate failover to the DR Region. To implement automated detection to achieve an aggressive RTO, you can build a solution based on [health checks](https://aws.amazon.com/builders-library/implementing-health-checks/). These health checks do not stop at heartbeats (which check whether the control plane and data plane modules within a network can communicate with one another), but go deeper to evaluate the interrelated nature of application components to achieve an accurate prediction. However, an automated solution can carry the risk of false alarms, which can lead to unnecessary failovers. You should exercise caution in this case, because unnecessary failovers introduce availability issues for your business. You also can build manual overrides in the workflow to confirm that the failover has been carried out. You can subscribe to the [Service Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/aws-health-dashboard-status.html) RSS feed to stay informed of service-level disruptions. Additionally, you can use the [AWS Health Dashboard ](https://aws.amazon.com/health/home)(requires an AWS account) within your primary Region and account to stay aware of events that can affect your account. These can help you make an informed decision to fail over in the case of a Region-wide event.

## Failover
<a name="failover"></a>

Regardless of which DR strategy you choose, you can build custom DR automation solutions to perform the failover to the DR Region. This automation can minimize the need for manual intervention and provide greater control in testing your DR solution. You can choose from the [AWS service APIs](https://aws.amazon.com/tools/), which AWS provides in multiple languages such as JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js and C\+\+, based on your organization's preference. To build automation that uses these AWS service APIs, you should first focus on turning the database infrastructure to code in the form of AWS CloudFormation or Terraform templates. These templates can help you automate the failover of several databases and also maintain the order in which application and database components are brought back up in the DR Region.

For DR purposes, we recommend that you focus on these two goals:
+ Existing [CloudFormation stacks should export](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html) pertinent information about your databases, including instance names and endpoints. Your automation processes can refer to these export values within a Region and perform operations that will help with your DR operations.
+ If you have resources that are in production but don't have an associated CloudFormation stack, you should focus on creating stacks for those resources. Also ensure that these stacks cover the right export values, as mentioned in the previous point.

When you have met these two goals, you can build automation solutions in the language of your organization's choice to take advantage of CloudFormation exports and automatically perform the cutover actions required in the event of a disaster. For example, if you have an ElastiCache (Redis OSS) global datastore that is deployed as a CloudFormation template, the automation code has access to the CloudFormation exports that provide details about the global datastore. In the event of a disaster, the code can automatically promote the secondary datastore to the primary datastore without any manual intervention by using the ElastiCache (Redis OSS) service APIs.

In a typical scenario, automation should be scalable for multiple databases within your organization. You can scale your automation solutions for several databases by using [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) or [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
