---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/upgrade-sap-pacemaker-clusters-from-ensa1-to-ensa2.html
---

# Upgrade SAP Pacemaker clusters from ENSA1 to ENSA2
<a name="upgrade-sap-pacemaker-clusters-from-ensa1-to-ensa2"></a>

*Gergely Cserdi and Balazs Sandor Skublics, Amazon Web Services*

## Summary
<a name="upgrade-sap-pacemaker-clusters-from-ensa1-to-ensa2-summary"></a>

This pattern explains the steps and considerations for upgrading an SAP Pacemaker cluster that is based on Standalone Enqueue Server (ENSA1) to ENSA2. The information in this pattern applies to both SUSE Linux Enterprise Server (SLES) and Red Hat Enterprise Linux (RHEL) operating systems.

Pacemaker clusters on SAP NetWeaver 7.52 or S/4HANA 1709 and earlier versions run on an ENSA1 architecture and are configured specifically for ENSA1. If you run your SAP workloads on Amazon Web Services (AWS) and you’re interested in moving to ENSA2, you might find that the SAP, SUSE, and RHEL documentation doesn’t provide comprehensive information. This pattern describes the technical steps required to reconfigure SAP parameters and Pacemaker clusters to upgrade from ENSA1 to ENSA2. It provides examples of SUSE systems, but the concept is the same for RHEL clusters.

**Note**
ENSA1 and ENSA2 are concepts that pertain to SAP applications only, so the information in this pattern doesn’t apply to SAP HANA or other types of clusters.

**Note**
Technically, ENSA2 can be used with or without Enqueue Replicator 2. However, high availability (HA) and failover automation (through a  cluster solution) require Enqueue Replicator 2. This pattern uses the term *ENSA2 clusters* to refer to clusters with Standalone Enqueue Server 2 and Enqueue Replicator 2.

## Prerequisites and limitations
<a name="upgrade-sap-pacemaker-clusters-from-ensa1-to-ensa2-prereqs"></a>

**Prerequisites **
+ A working ENSA1-based cluster that uses Pacemaker and Corosync on SLES or RHEL.
+ At least two Amazon Elastic Compute Cloud (Amazon EC2) instances where the (ABAP) SAP Central Services (ASCS/SCS) and Enqueue Replication Server (ERS) instances are running.
+ Knowledge of managing SAP applications and clusters.
+ Access to the Linux environment as root user.

**Limitations **
+ ENSA1-based clusters support a two-node architecture only.
+ ENSA2-based clusters cannot be deployed to SAP NetWeaver versions before 7.52.
+ EC2 instances in clusters should be in different AWS Availability Zones.

**Product versions**
+ SAP NetWeaver version 7.52 or later
+ Starting with S/4HANA 2020, only ENSA2 clusters are supported
+ Kernel 7.53 or later, which supports ENSA2 and Enqueue Replicator 2
+ SLES for SAP Applications version 12 or later
+ RHEL for SAP with High Availability (HA) version 7.9 or later

## Architecture
<a name="upgrade-sap-pacemaker-clusters-from-ensa1-to-ensa2-architecture"></a>

**Source technology stack **
+ SAP NetWeaver 7.52 with SAP Kernel 7.53 or later
+ SLES or RHEL operating system

**Target technology stack **
+ SAP NetWeaver 7.52 with SAP Kernel 7.53 or later, including S/4HANA 2020 with ABAP platform
+ SLES or RHEL operating system

**Target architecture **

The following diagram shows an HA configuration of ASCS/SCS and ERS instances based on an ENSA2 cluster.

![HA architecture for ASCS/SCS and ERS instances on an ENSA2 cluster](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c32560de-901f-4796-a6b3-c08c109b22c8/images/19501713-0ddf-4242-9ea3-90478200a19e.png)

**Comparison of ENSA1 and ENSA2 clusters**

SAP introduced ENSA2 as the successor to ENSA1. An ENSA1-based cluster supports a two-node architecture where the ASCS/SCS instance fails over to ERS when an error occurs. This limitation stems from how the ASCS/SCS instance regains the lock table information from the shared memory of the ERS node after failover. ENSA2-based clusters with Enqueue Replicator 2 eliminate this limitation, because the ASCS/SCS instance can collect the lock information from the ERS instance over the network. ENSA2-based clusters can have more than two nodes, because the ASCS/SCS instance is no longer required to fail over to the ERS node. (However, in a two-node ENSA2 cluster environment, the ASCS/SCS instance will still fail over to the ERS node because there are no other nodes in the cluster to fail over to.) ENSA2 is supported starting with SAP Kernel 7.50 with some limitations. For HA setup that supports Enqueue Replicator 2, the minimum requirement is NetWeaver 7.52 (see [SAP OSS Note 2630416](https://launchpad.support.sap.com/#/notes/2630416)). S/4HANA 1809 comes with ENSA2 architecture recommended by default, whereas S/4HANA supports only ENSA2 starting with version 2020.

**Automation and scale**

The HA cluster in the target architecture makes ASCS fail over to other nodes automatically.

**Scenarios for moving to ENSA2-based clusters**

There are two main scenarios for upgrading to ENSA2-based clusters:
+ Scenario 1: You choose to upgrade to ENSA2 without an accompanying SAP upgrade or S/4HANA conversion, assuming that your SAP release and Kernel version support ENSA2.
+ Scenario 2: You move to ENSA2 as part of an upgrade or conversion (for example, to S/4HANA 1809 or later) by using SUM.

The [Epics](#upgrade-sap-pacemaker-clusters-from-ensa1-to-ensa2-epics) section covers the steps for these two scenarios. The first scenario requires you to manually set up SAP-related parameters before you change the cluster configuration for ENSA2. In the second scenario, the binaries and SAP-related parameters are deployed by SUM, and your only remaining task is to update the cluster configuration for HA. We still recommend that you validate SAP parameters after you use SUM. In most cases, S/4HANA conversion is the main reason for a cluster upgrade.

## Tools
<a name="upgrade-sap-pacemaker-clusters-from-ensa1-to-ensa2-tools"></a>
+ For OS package managers, we recommend the Zypper (for SLES) or YUM (for RHEL) tools.
+ For cluster management, we recommend **crm** (for SLES) or **pcs** (for RHEL) shells.
+ SAP instance management tools such as SAPControl.
+ (Optional) SUM tool for S/4HANA conversion upgrade.

## Best practices
<a name="upgrade-sap-pacemaker-clusters-from-ensa1-to-ensa2-best-practices"></a>
+ For best practices for using SAP workloads on AWS, see the [SAP Lens](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/sap-lens.html) for the AWS Well-Architected Framework.
+ Consider the number of cluster nodes (odd or even) in your ENSA2 multi-node architecture.
+ Set up the ENSA2 cluster for SLES 15 in alignment with the SAP S/4-HA-CLU 1.0 certification standard.
+ Always save or back up your existing cluster and application state before upgrading to ENSA2.

## Epics
<a name="upgrade-sap-pacemaker-clusters-from-ensa1-to-ensa2-epics"></a>

### Configure SAP parameters manually for ENSA2 (scenario 1 only)
<a name="configure-sap-parameters-manually-for-ensa2-scenario-1-only"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the parameters in the default profile. | If you want to upgrade to ENSA2 while staying on the same SAP release or if your target release defaults to ENSA1, set the parameters in the default profile (DEFAULT.PFL file) to the following values.<pre>enq/enable=TRUE<br />enq/serverhost=sapascsvirt<br />enq/serverinst=10        (instance number of ASCS/SCS instance)<br />enque/process_location=REMOTESA<br />enq/replicatorhost=sapersvirt<br />enq/replicatorinst=11    (instance number of ERS instance)<br />  </pre><br />where `sapascsvirt` is the virtual hostname for the ASCS instances, and `sapersvirt` is the virtual hostname for the ERS instances. You can change these to fit your target environment.To use this upgrade option, your SAP release and Kernel version must support ENSA2 and Enqueue Replicator 2. | SAP |
| Configure the ASCS/SCS instance profile. | If you want to upgrade to ENSA2 while staying on the same SAP release or if your target release defaults to ENSA1, set the following parameters in the ASCS/SCS instance profile. <br />The section of the profile where ENSA1 is defined looks something like the following.<pre>#--------------------------------------------------------------<br />Start SAP enqueue server<br />#-------------------------------------------------------------- <br />_EN = en.sap$(SAPSYSTEMNAME)$(INSTANCE_NAME) <br />Execute_04 = local rm -f $(_EN) <br />Execute_05 = local ln -s -f $(DIR_EXECUTABLE)/enserver$(FT_EXE) $(_EN) <br />Start_Program_01 = local $(_EN) pf=$(_PF)<br />  </pre><br />To reconfigure this section for ENSA2:1. Change the `_EN` program prefix to `_ENQ` based on the latest information from SAP (OSS Note 2501860; requires an [SAP ONE Support Launchpad user account](https://support.sap.com/en/my-support/knowledge-base.html)).<br />2. Change the binary for enqueue server from `enserver` to `enq_server`.<br />3. Set the new parameter `enq/server/replication/enable` to `TRUE`.<br />4. Make sure that `Autostart = 0`.<br />This profile section would look something like the following after your changes.<pre>#--------------------------------------------------------------<br />Start SAP enqueue server<br />#-------------------------------------------------------------- <br />_ENQ = enq.sap$(SAPSYSTEMNAME)$(INSTANCE_NAME) <br />Execute_04 = local rm -f $(_ENQ) <br />Execute_05 = local ln -s -f $(DIR_EXECUTABLE)/enq_server$(FT_EXE) $(_ENQ) <br />Start_Program_01 = local $(_ENQ) pf=$(_PF) <br />... <br />enq/server/replication/enable = TRUE <br />Autostart = 0</pre>`_ENQ` must not have the restart option enabled. If `RestartProgram_01` is set for `_ENQ`, change it to `StartProgram_01`. This prevents SAP from restarting the service or interfering with cluster-managed resources. | SAP |
| Configure the ERS profile. | If you want to upgrade to ENSA2 while staying on the same SAP release or if your target release defaults to ENSA1, set the following parameters in the ERS instance profile.<br />Find the section where the enqueue replicator is defined. It will be similar to the following.<pre>#------------------------------------------------------<br />Start enqueue replication server<br />#------------------------------------------------------ <br />_ER = er.sap$(SAPSYSTEMNAME)$(INSTANCE_NAME) <br />Execute_03 = local rm -f $(_ER) <br />Execute_04 = local ln -s -f $(DIR_EXECUTABLE)/enrepserver$(FT_EXE) $(_ER) <br />Start_Program_00 = local $(_ER) pf=$(_PF) NR=$(SCSID)<br />  </pre><br />To reconfigure this section for Enqueue Replicator 2:1. Change the `_ER` program prefix to `_ENQR` based on the latest notes from SAP (OSS Note 2501860; requires an [SAP ONE Support Launchpad user account](https://support.sap.com/en/my-support/knowledge-base.html)).<br />2. Change the binary for the enqueue replicator to `enq_replicator` instead of `enrepserver`.<br />3. Make sure that `Autostart = 0`.<br />This profile section should look something like the following after your changes.<pre>#------------------------------------------------------<br />Start enqueue replication server<br />#------------------------------------------------------ <br />_ENQR = enqr.sap$(SAPSYSTEMNAME)$(INSTANCE_NAME) <br />Execute_01 = local rm -f $(_ENQR) <br />Execute_02 = local ln -s -f $(DIR_EXECUTABLE)/enq_replicator$(FT_EXE) $(_ENQR) <br />Start_Program_00 = local $(_ENQR) pf=$(_PF) NR=$(SCSID) <br />… <br />Autostart = 0</pre>`_ENQR` must not have the restart option enabled. If `RestartProgram_01` is set for `_ENQR`, change it to `StartProgram_01`. This prevents SAP from restarting the service or interfering with cluster-managed services. | SAP |
| Restart SAP Start Services. | After you change the profiles described previously in this epic, restart SAP Start Services for both ASCS/SCS and ERS.<br />`sapcontrol -nr 10 -function RestartService SCT`<br />`sapcontrol -nr 11 -function RestartService SCT`<br />where `SCT` refers to the SAP system ID, and assuming that 10 and 11 are the instance numbers for ASCS/SCS and ERS instances, respectively. | SAP |

### Reconfigure the cluster for ENSA2 (required for both scenarios)
<a name="reconfigure-the-cluster-for-ensa2-required-for-both-scenarios"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify version numbers in SAP resource agents. | When you use SUM to upgrade SAP to S/4HANA 1809 or later, SUM handles the parameter changes in the SAP profiles. Only the cluster requires manual adjustment. However, we recommend that you verify the parameter settings before you make any changes to the cluster.The examples in this epic assume that you’re using the SUSE operating system. If you’re using RHEL, you will need to use tools such as YUM and the **pcs** shell instead of Zypper and **crm**.<br />Check both nodes in the architecture to confirm that the `resource-agents` package matches the minimum version recommended by SAP. For SLES, check SAP OSS Note 2641019. For RHEL, check SAP OSS Note 2641322. (SAP Notes require an [SAP ONE Support Launchpad user account](https://support.sap.com/en/my-support/knowledge-base.html).)<pre>sapers:sctadm 23> zypper search -s -i resource-agents<br />Loading repository data...<br />Reading installed packages...<br />S | Name | Type | Version | Arch | Repository<br />--+-----------------+---------+------------------------------------+--------+-----------------------------<br />i | resource-agents | package | 4.8.0+git30.d0077df0-150300.8.28.1 | x86_64 | SLE-Product-HA15-SP3-Updates</pre><br />Update the `resource-agents` version if necessary. | AWS systems administrator |
| Back up cluster configuration. | Back up the CRM cluster configuration as follows.<br />`crm configure show > /tmp/cluster_config_backup.txt` | AWS systems administrator |
| Set maintenance mode. | Set the cluster to maintenance mode.<br />`crm configure property maintenance-mode="true"` | AWS systems administrator |
| Check cluster configuration. | Check the current cluster configuration.<br />`crm configure show`<br />Here is an excerpt from the full output:<pre>node 1: sapascs<br />node 2: sapers<br />...<br />primitive rsc_sap_SCT_ASCS10 SAPInstance \<br />operations $id=rsc_sap_SCT_ASCS10-operations \<br />op monitor interval=120 timeout=60 on-fail=restart \<br />params InstanceName=SCT_ASCS10_sapascsvirt START_PROFILE="/sapmnt/SCT/profile/SCT_ASCS10_sapascsvirt" \ <br />   AUTOMATIC_RECOVER=false \<br />meta resource-stickiness=5000 failure-timeout=60 migration-threshold=1 priority=10<br />primitive rsc_sap_SCT_ERS11 SAPInstance \<br />operations $id=rsc_sap_SCT_ERS11-operations \<br />op monitor interval=120 timeout=60 on-fail=restart \<br />params InstanceName=SCT_ERS11_sapersvirt START_PROFILE="/sapmnt/SCT/profile/SCT_ERS11_sapersvirt" \<br />   AUTOMATIC_RECOVER=false IS_ERS=true \<br />meta priority=1000<br />...<br />colocation col_sap_SCT_no_both -5000: grp_SCT_ERS11 grp_SCT_ASCS10<br />location loc_sap_SCT_failover_to_ers rsc_sap_SCT_ASCS10 \<br />rule 2000: runs_ers_SCT eq 1<br />order ord_sap_SCT_first_start_ascs Optional: rsc_sap_SCT_ASCS10:start rsc_sap_SCT_ERS11:stop symmetrical=false<br />...</pre><br />where `sapascsvirt` refers to the virtual hostname for the ASCS instances, `sapersvirt` refers to the virtual hostname for the ERS instances, and `SCT` refers to the SAP system ID. | AWS systems administrator |
| Remove failover colocation constraint. | In the previous example, the location constraint `loc_sap_SCT_failover_to_ers`  specifies that the ENSA1 feature of ASCS should always follow the ERS instance upon failover. With ENSA2, ASCS should be able to fail over freely to any participating nodes, so you can remove this constraint.<br />`crm configure delete loc_sap_SCT_failover_to_ers` | AWS systems administrator |
| Adjust primitives. | You will also need to make minor changes to the ASCS and ERS SAPInstance primitives.<br />Here is an example of an ASCS SAPInstance primitive that is configured for ENSA1.<pre>primitive rsc_sap_SCT_ASCS10 SAPInstance \<br />operations $id=rsc_sap_SCT_ASCS10-operations \<br />op monitor interval=120 timeout=60 on-fail=restart \<br />params InstanceName=SCT_ASCS10_sapascsvirt START_PROFILE="/sapmnt/SCT/profile/SCT_ASCS10_sapascsvirt" \<br />   AUTOMATIC_RECOVER=false \<br />meta resource-stickiness=5000 failure-timeout=60 migration-threshold=1 priority=10</pre><br />To upgrade to ENSA2, change this configuration to the following.<pre>primitive rsc_sap_SCT_ASCS10 SAPInstance \<br />operations $id=rsc_sap_SCT_ASCS10-operations \<br />op monitor interval=120 timeout=60 on-fail=restart \<br />params InstanceName=SCT_ASCS10_sapascsvirt START_PROFILE="/sapmnt/SCT/profile/SCT_ASCS10_sapascsvirt" \<br />   AUTOMATIC_RECOVER=false \<br />meta resource-stickiness=3000 </pre><br />This is an example of an ERS SAPInstance primitive that is configured for ENSA1.<pre>primitive rsc_sap_SCT_ERS11 SAPInstance \<br />operations $id=rsc_sap_SCT_ERS11-operations \<br />op monitor interval=120 timeout=60 on-fail=restart \<br />params InstanceName=SCT_ERS11_sapersvirt START_PROFILE="/sapmnt/SCT/profile/SCT_ERS11_sapersvirt" \<br />   AUTOMATIC_RECOVER=false IS_ERS=true \<br />meta priority=1000</pre><br />To upgrade to ENSA2, change this configuration to the following.<pre>primitive rsc_sap_SCT_ERS11 SAPInstance \<br />operations $id=rsc_sap_SCT_ERS11-operations \<br />op monitor interval=120 timeout=60 on-fail=restart \<br />params InstanceName=SCT_ERS11_sapersvirt START_PROFILE="/sapmnt/SCT/profile/SCT_ERS11_sapersvirt" \<br />   AUTOMATIC_RECOVER=false IS_ERS=true</pre><br />You can change primitives in various ways. For example, you can revise them in an editor such as vi, as in the following example.<br />`crm configure edit rsc_sap_SCT_ERS11` | AWS systems administrator |
| Disable maintenance mode. | Disable maintenance mode on the cluster.<br />`crm configure property maintenance-mode="false"`<br />When the cluster is out of maintenance mode, it attempts to bring the ASCS and ERS instances online with the new ENSA2 settings. | AWS systems administrator |

### (Optional) Add cluster nodes
<a name="optional-add-cluster-nodes"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Review best practices. | Before you add more nodes, make sure to understand best practices such as whether to use an odd or even number of nodes. | AWS systems administrator |
| Add nodes. | Adding more nodes involves a series of tasks, such as updating the operating system, installing software packages that match the existing nodes, and making mounts available. You can use the **Prepare Additional Host** option in SAP Software Provisioning Manager (SWPM) to create an SAP-specific baseline of the host. For more information, see the SAP guides listed in the next section. | AWS systems administrator |

## Related resources
<a name="upgrade-sap-pacemaker-clusters-from-ensa1-to-ensa2-resources"></a>

**SAP and SUSE references**

To access SAP Notes, you must have an SAP ONE Support Launchpad user account. For more information, see the [SAP Support website](https://support.sap.com/en/my-support/knowledge-base.html).
+ [SAP Note 2501860 ‒ Documentation for SAP NetWeaver Application Server for ABAP 7.52](https://launchpad.support.sap.com/#/notes/2501860)
+ [SAP Note 2641019 ‒ Installation of ENSA2 and update from ENSA1 to ENSA2 in SUSE HA environment](https://launchpad.support.sap.com/#/notes/2641019)
+ [SAP Note 2641322 ‒ Installation of ENSA2 and update from ENSA1 to ENSA2 when using the Red Hat HA solutions for SAP](https://launchpad.support.sap.com/#/notes/2641322)
+ [SAP Note 2711036 ‒ Usage of the Standalone Enqueue Server 2 in an HA Environment](https://launchpad.support.sap.com/#/notes/2711036)
+ [Standalone Enqueue Server 2](https://help.sap.com/docs/ABAP_PLATFORM/cff8531bc1d9416d91bb6781e628d4e0/902412f09e134f5bb875adb6db585c92.html) (SAP documentation)
+ [SAP S/4 HANA ‒ Enqueue Replication 2 High Availability Cluster - Setup Guide](https://documentation.suse.com/sbp/all/html/SAP_S4HA10_SetupGuide-SLE12/index.html) (SUSE documentation)

**AWS references**
+ [SAP HANA on AWS: High Availability Configuration Guide for SLES and RHEL](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-on-aws-ha-configuration.html)
+ [SAP Lens - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/sap-lens.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
