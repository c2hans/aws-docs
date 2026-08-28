---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/start-stop-aurora-cluster.html
---

# `AWS-StartStopAuroraCluster`
<a name="start-stop-aurora-cluster"></a>

**Description**

This runbook starts or stops an Amazon Aurora cluster.

**Note**
To start a cluster it must be in a `stopped` status. To stop a cluster it must be in an `available` status. This runbook can't be used to start or stop a cluster that is an Aurora Serverless v1 cluster, an Aurora multi-master cluster, part of an Aurora global database, or a cluster that uses Aurora parallel query. The runbook can be used to stop and start an Aurora Serverless v2 cluster.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-StartStopAuroraCluster)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ ClusterName

  Type: String

  Description: (Required) The name of the Aurora cluster you want to stop or start.
+ Action

  Type: String

  Valid values: Start \| Stop

  Default: Start

  Description: (Required) The name of the Aurora cluster you want to stop or start.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBClusters`
+ `rds:StartDBCluster`
+ `rds:StopDBCluster`

**Document Steps**
+ `aws:executeScript` - Starts or stops the cluster based on the values you specify for the.

**Outputs**

StartStopAuroraCluster.ClusterName - The name of the Aurora cluster

StartStopAuroraCluster.CurrentStatus - The current status of the Aurora cluster

StartStopAuroraCluster.Message - Details of the automation

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
