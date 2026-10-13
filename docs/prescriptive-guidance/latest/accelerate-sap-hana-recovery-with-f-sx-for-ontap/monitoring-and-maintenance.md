---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/monitoring-and-maintenance.html
---

# Monitoring and maintenance
<a name="monitoring-and-maintenance"></a>

Backup architecture success requires ongoing operational oversight. This section establishes the monitoring, maintenance, and validation procedures that you require. These maintain production backup SLAs and ensure recovery capability remains valid throughout the system's lifecycle.

## Ongoing monitoring
<a name="ongoing-monitoring.e8a8c349-3b0a-54d9-9197-76b9825198ea"></a>

Implement continuous monitoring. This ensures backup operations meet service level agreements:
+ **Backup success rate:** Monitor backup job success percentage. Target a success rate greater than 99% for scheduled backups. Exclude environmental failures.
+ **Snapshot creation time:** Track snapshot creation duration. Alert when snapshot creation exceeds 10 minutes. Also alert when it increases by more than 50% from baseline.
+ **Replication lag:** Monitor lag between snapshot creation and replication completion. Alert when replication lag exceeds 30 minutes. Also alert when it increases by more than 100% from baseline.
+ **Storage utilization:** Track snapshot storage consumption. Monitor for unexpected growth.
+ **Backup catalog consistency:** Verify the HANA backup catalog matches Commvault records.
+ **Network bandwidth utilization:** Monitor replication bandwidth consumption patterns.

## Regular maintenance tasks
<a name="regular-maintenance-tasks.34c35cc3-91b7-5d93-b38c-bd95a6c620e7"></a>

Establish a regular maintenance cadence. This upholds operational continuity of the backup solution:
+ **Monthly recovery testing: **Test recovery from snapshots to verify that your recovery capability continues to function correctly.
+ **Quarterly disaster recovery drill:** Test recovery in the Backup account. This validates the multi-account architecture.
+ **Policy review:** Review backup policies quarterly. Confirm they continue to meet the defined RPO/RTO targets. Also confirm they meet any updated business and regulatory requirements.
+ **Capacity planning:** Track Amazon FSx for NetApp ONTAP volume utilization. Initiate capacity expansion when consumed storage exceeds 70% of provisioned capacity. This prevents backup failures from insufficient storage headroom.
+ **Security audits:** Review access logs. Verify only authorized users access backup resources.
+ **Commvault updates:** Apply Commvault patches and updates. Follow vendor recommendations.
+ **Amazon FSx for NetApp ONTAP firmware updates:** Apply NetApp firmware updates. AWS applies updates during these windows with minimal impact.
