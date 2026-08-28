---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel07-bp02.html
---

# ADVREL07-BP02 Implement a backup strategy which would meet RTO and RPO objectives
<a name="advrel07-bp02"></a>

 Develop comprehensive backup strategies, focusing on data classification and meeting Recovery Time Objective (RTO) and Recovery Point Objective (RPO) requirements through appropriate service selection.

## Implementation guidance
<a name="implementation-guidance-32"></a>

 Review the data related to your workload and classify the data according to usage, retention, and availability needs. Example classifications might be user profile info, campaign data, reporting data. Consider how those different data classes are used within your workload and how the availability of that data can impact your workload's operation. Use those classifications to determine the RPO and RTO requirements for your workload. Identify the AWS services that can meet your requirements, and deploy resources to the Regions or Availability Zones that can achieve your RTO and RPO targets. Test the backup and restoration process to verify that your backup and recovery strategies will work during a disruptive event.

## Key AWS services
<a name="key-aws-services-18"></a>
+  [AWS Backup](https://aws.amazon.com/backup/)
+  [Amazon EBS](https://aws.amazon.com/ebs/)
+  [Amazon EC2](https://aws.amazon.com/ec2/)
+  [Amazon Relational Database Service](https://aws.amazon.com/rds/)
+  [Amazon Elastic File System](https://aws.amazon.com/efs/)

## Resources
<a name="resources-27"></a>
+  [Disaster Recovery (DR) Architecture on AWS, Part II: Backup and Restore with Rapid Recovery](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-ii-backup-and-restore-with-rapid-recovery/index.html)
+  Establishing RPO and RTO Targets for Cloud Applications

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
