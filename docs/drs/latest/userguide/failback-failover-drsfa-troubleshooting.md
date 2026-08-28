---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/failback-failover-drsfa-troubleshooting.html
---

# Troubleshooting the DRSFA Client
<a name="failback-failover-drsfa-troubleshooting"></a>

The following table describes common issues and resolutions when using the DRSFA client.

| Issue | Possible cause | Resolution |
| --- | --- | --- |
| Cannot connect to vCenter | vCenter host is unreachable from the DRSFA client host, or the specified port is blocked. | Verify network connectivity between the DRSFA client host and vCenter. Confirm that the VCENTER\_PORT (usually 443) is open. |
| Replication fails to start | TCP port 1500 is blocked on the Recovery instance. | Verify that inbound TCP port 1500 is open on the Recovery instance security group in AWS. |
| Permission errors on vCenter operations | The vCenter credentials lack required permissions. | Confirm that the vCenter user has all required permissions listed in the prerequisites (Virtual machine and Datastore permissions). |
| AWS API permission errors | The IAM credentials lack the required policy. | Verify that the IAM role or user includes the AWSElasticDisasterRecoveryFailbackInstallationPolicy policy. |
| CD-ROM attachment failures | The VM does not have two available IDE CD-ROM slots, or the datastore path is incorrect. | Verify that the VM has available IDE controller slots. Confirm that VCENTER\_FAILBACK\_CLIENT\_PATH and VCENTER\_SEED\_ISO\_PATH are correct. |
| Replication stalls or fails | Network connectivity issues between the source server and the Recovery instance. | Verify that the source server can reach the Recovery instance on TCP port 1500. Check the failback.log on the source VM for details. |

## Log locations
<a name="failback-failover-drsfa-log-locations"></a>
+ **DRSFA client log**: `drs_failback_automation_client/drs_failback_automation.log` on the host where the client runs.
+ **Per-server failback log**: `failback.log` on the individual source VM being failed back.
+ **CloudWatch**: If configured, logs are sent to the `DRS_Mass_Failback_Automation` log group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
