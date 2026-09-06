---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/testing-disaster-recovery.html
---

# Testing disaster recovery
<a name="testing-disaster-recovery"></a>

 Test disaster recovery implementation to validate the implementation and regularly test failover to your workload’s DR Region to ensure that RTO and RPO are met.

 A pattern to avoid is developing recovery paths that are rarely executed. For example, you might have a secondary data store that is used for read-only queries. When you write to a data store and the primary fails, you might want to fail over to the secondary data store. If you don’t frequently test this failover, you might find that your assumptions about the capabilities of the secondary data store are incorrect. The capacity of the secondary, which might have been sufficient when you last tested, might no longer be able to tolerate the load under this scenario, or service quotas in the secondary Region might not be sufficient.

 Our experience has shown that the only error recovery that works is the path you test frequently. This is the reason why having a small number of recovery paths is best.

 You can establish recovery patterns and regularly test them. If you have a complex or critical recovery path, you still need to regularly execute that failure in production to validate that the recovery path works.

 Manage configuration drift at the DR Region. Ensure that your infrastructure, data, and configuration are as needed at the DR Region. For example, check that AMIs and service quotas are up-to-date.

 You can utilize [AWS Config](https://aws.amazon.com/config/) to continuously monitor and record your AWS resource configurations. AWS Config can detect drift and trigger [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to fix drift and raise alarms. [AWS CloudFormation](https://aws.amazon.com/cloudformation/) can additionally detect drift in stacks you have deployed.
