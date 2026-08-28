---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/testing.html
---

# Testing to achieve confidence
<a name="testing"></a>

The best DR solution for databases is one that is tested frequently and passes the following checks:
+ Proper data recovery that meets the RPO expectations for each database
+ Complete restoration of a functioning database within the expected RTO time frame, which allows applications to connect to the database and resume full functionality

DR testing should be part of your business strategy so that backups work when they are most needed. DR testing should also address cases where:
+ The size of a database grew significantly, and your current DR strategy no longer meets the service-level agreement (SLA) for the business.
+ A backup file is corrupted, which could cause problems during recovery.

## What to consider when testing your DR strategy
<a name="considerations"></a>
+ Have clear business continuity goals regarding RPO and RTO, and make sure that test results align with your goals.
+ Create a detailed DR test plan that takes financial and human resource requirements for testing into account.
+ Assign resources to document potential issues and learnings.
+ Update your DR strategy based on learnings, and find the solution that supports the optimal processes and automation that works for your organization.

## Testing frequency for DR solutions
<a name="frequency"></a>

There are no set recommendations for the DR test cycles, unless they are explicitly prescribed by regulations. For example, the Payment Card Industry Data Security Standards (PCI DSS) compliance audit requires organizations to test their DR plan at least once a year. (See [PCI DSS Disaster Recovery Requirements](https://www.pcidssguide.com/pci-dss-disaster-recovery-requirements/) on the PCI DSS website.)

Application teams can also perform continuous testing of their individual DR solutions when their application or infrastructure changes.

## Drift detection
<a name="drift-detection"></a>

Your DR solution should also manage [drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html). This will ensure that the primary Region and DR Region are at the right level of synchronization and will ensure smooth progress during testing. [AWS Config](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization.html) provides configuration management and history tracking of configurations in your infrastructure, and can help you manage drift effectively.

## Observability
<a name="observability"></a>

Improving observability positively impacts your preparation for testing. All DR solutions move data in the primary Region to the secondary (DR) Region. You can set up alerts for replication lag and backups, or put a process in place to perform daily checks that ensure that your data was copied to the DR Region successfully.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
