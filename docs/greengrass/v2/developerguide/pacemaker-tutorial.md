---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/pacemaker-tutorial.html
---

# Tutorial: Set up high availability for AWS IoT Greengrass V2 with Pacemaker
<a name="pacemaker-tutorial"></a>

This tutorial shows you how to set up AWS AWS IoT AWS IoT Greengrass V2 in a high availability (HA) configuration using [Pacemaker](https://clusterlabs.org/projects/pacemaker/), a high-availability cluster resource manager. You configure multiple Amazon EC2 instances as cluster instances, use [DRBD](https://linbit.com/drbd/) for block-level data replication, and manage AWS IoT Greengrass V2 and load balancer services as Pacemaker resources with automatic failover.

**Important**
This tutorial uses Amazon Elastic Compute Cloud instances to demonstrate the setup. You can deploy the AWS IoT Greengrass V2 and Pacemaker integration to achieve high availability on a cluster of any device type, as long as the devices can communicate with one another.

This tutorial includes the following setups:
+ **Active/Passive AWS IoT Greengrass V2 service** – Run AWS IoT Greengrass V2 as a systemd service managed by Pacemaker with DRBD-replicated storage. Only one instance runs AWS IoT Greengrass V2 at a time, and Pacemaker handles failover to a standby instance.
+ **Active/Passive load balancer** – Run HAProxy as a Pacemaker-managed resource with its configuration stored on DRBD-replicated storage. Pacemaker fails over the load balancer to a standby instance if the primary goes down.
+ **Active/Active AWS IoT Greengrass V2 component** – Monitor a AWS IoT Greengrass V2 component across all instances using a custom OCF (Open Cluster Framework) resource agent. Pacemaker detects component failures and triggers recovery without full instance failover.

Each setup is standalone and mutually exclusive. Each setup assumes a fresh start from the prerequisites, with the single DRBD resource repurposed for each setup's needs. Setup 3 (Active/Active) does not use DRBD — skip the DRBD prerequisite steps and install AWS IoT Greengrass V2 to a local path on each instance instead.

In Setups 1 and 2, you create a highly available cluster of AWS IoT Greengrass V2 devices. The cluster contains a *primary instance*, which is the instance that is currently active and running the managed services (such as AWS IoT Greengrass V2 or HAProxy), and one or more *standby instances*, which are idle and waiting to take over if the primary fails. Pacemaker automatically promotes one of the standby instances to primary during failover. In Setup 3 (Active/Active), all instances run the service simultaneously, and Pacemaker handles per-instance recovery rather than failover promotion.

**Topics**
+ [Prerequisites and cluster setup](pacemaker-tutorial-prerequisites.md)
+ [Active/passive AWS IoT Greengrass V2 service](pacemaker-tutorial-setup1.md)
+ [Active/passive load balancer](pacemaker-tutorial-setup2.md)
+ [Active/active AWS IoT Greengrass V2 component](pacemaker-tutorial-setup3.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
