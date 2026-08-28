---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-sas-viya-to-the-aws-cloud/high-level-full-system-migration-steps.html
---

# High-level, full-system migration steps
<a name="high-level-full-system-migration-steps"></a>

**Note**
This document is based on the 2020.1.5 stable release of SAS Viya 4. For more information, see [Full-System Migration and Content Migration](https://documentation.sas.com/doc/en/sasadmincdc/v_012/promigwlcm/home.htm) in the SAS documentation.

A full-system migration to SAS Viya 4 moves content and data from a specific version of a SAS Viya on-premises deployment (or from a SAS Viya deployment) in a hosting facility to a SAS Viya 4 cloud-based environment.

A full-system migration is a four-step process: plan, back up, restore, and validate. Although each step is independent, a successful full-system migration requires that you complete each step in order. An Ansible playbook lets you properly plan and back up your migration content so that you can curate what is migrated.

The following diagram illustrates the steps involved in migrating a Viya 3.x deployment to Viya4.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-sas-viya-to-the-aws-cloud/images/guide-img/6af091bd-620c-4ae4-9607-2e103616429a/images/d4bec5d8-8da8-43c5-bad9-59ea83ecf41b.png)

## Supported scenarios for full-system migration
<a name="supported-scenarios-for-full-system-migration"></a>

Full-system migration to SAS Viya 4 includes moving content and data from a single-tenant SAS Viya 3.4, a single-tenant SAS Viya 3.5, or from an existing SAS Viya 4 deployment. This document covers the following target SAS Viya 4 scenarios:
+ Migrating to a private cloud
+ Migrating to a public cloud

You cannot migrate from the following SAS Viya environments:
+ SAS Viya 3.3 or earlier
+ Multitenant environments
+ Microsoft Windows environments
+ PowerLinux (PLX) environments
+ SAS Viya 3.x or SAS Viya 4 SMP environments to SAS Viya 4 MPP environments
+ SAS Viya 3.x or SAS Viya 4 MPP environments to SAS Viya 4 SMP environments

Furthermore, you cannot migrate from SAS 9.x environments by using the same tools, processes, and steps that are used to migrate from SAS Viya, but content migration of SAS 9.x content is supported. For more information, see [Migration from SAS 9.4: Tasks](https://go.documentation.sas.com/doc/en/sasadmincdc/v_012/calcontentmig9x/n0qj0in535x3s8n1pdz5g4tgtg0c.htm) in the SAS documentation.

## Using Ansible for full-system migration
<a name="using-ansible-for-full-system-migration"></a>

Ansible is configuration-management software that provides a way to move to SAS Viya 4 by automating the commands for migrating and controlling content. SAS provides a playbook that facilitates this. For a list of supported versions, see [Ansible](https://support.sas.com/en/documentation/third-party-software-reference/viya/35/support-for-operating-systems.html#ansible) in the *Support for Operating Systems and Environments in SAS Viya 3.5* documentation.

To use Ansible for migration, customize your environment's files, and run the migration commands according to the values in those files. The files, known collectively as the *Plan and Backup Ansible Playbook*, provide the instructions for which content is migrated to which machines.

The migration process includes a planning step that runs scans and publishes a report in addition to a step that backs up the SAS Viya 3.x environment. Each step involves running an Ansible command that evokes a play—specifically, a scan play and a backup play.

Use the inventory plugin of the SAS Viya command line interface (CLI) to generate the Plan and Backup Ansible Playbook.

**SAS Viya 3.x deployment file used by full-system migration**

The inventory.ini file that is created during the SAS Viya 3.x deployment is used by Ansible to migrate to SAS Viya. The inventory.ini file defines which machines (or hosts) the SAS Viya components reside on.

## Step 1. Plan
<a name="step-1-plan"></a>

You should understand the source environment and plan for what you want to migrate and what your target environment's characteristics are. The SAS administrator inventory CLI plays a key part in migration to Viya. The inventory CLI:
+ Generates the Plan and Backup Ansible playbook.
+ Delivers the SAS Viya inventory reports.
+ Supports the system backup and user-created content of the migration package.

For more information, see [Step 1: Plan (SAS Administrator)](https://documentation.sas.com/doc/en/sasadmincdc/v_012/calmigration3x/p0s8n6d5si7oqun1ixkvuw10mzcx.htm#p0ofjfnlilu6sdn16ua9n41ddeeo) in the SAS documentation.

## Step 2. Back up
<a name="step-2-back-up"></a>

You can use the Ansible playbook to create the migration backup package. The Ansible playbook uses the backup CLI to package the Viya system content and configuration.

Running the backup play of the Plan and Backup Ansible playbook does the following:
+ Initiates another scan of the environment. If enough time has passed since you ran the scan play, this helps to ensure that any changes in the environment are also reflected in the scan.
+ Creates the SAS Viya 3.x migration package.

For more information, see [Step 2: Back Up (SAS Administrator)](https://documentation.sas.com/doc/en/sasadmincdc/v_012/calmigration3x/p0s8n6d5si7oqun1ixkvuw10mzcx.htm#n1fcjs49yjrajln1fqa884fiyjih) in the SAS documentation.

## Step 3. Restore
<a name="step-3-restore"></a>

The restore process creates a new Viya deployment and restores the content of an existing environment into it. This requires elevated privileges in the Kubernetes cluster and involves using Kubectl and Kustomize to modify the Kubernetes objects in the cluster to restore the content from the package to the new environment.

For more information, see [Step 3: Restore (Cluster Administrator)](https://documentation.sas.com/doc/en/sasadmincdc/v_012/calmigration3x/p0s8n6d5si7oqun1ixkvuw10mzcx.htm#p0m4kvxw22ixrfn1gdybn3ciiwjr) in the SAS documentation.

## Step 4. Validate
<a name="step-4-validate"></a>

SAS Viya 4 provides the SAS Viya 4 inventory and SAS Viya comparison reports for comparing content between the source SAS Viya 3.x and target SAS Viya 4 environments. These reports and the associated SASVIYATYPES table are accessible through the SAS environment manager.

For more information, see [Step 5: Validate](https://documentation.sas.com/doc/en/sasadmincdc/v_012/calmigration3x/p0s8n6d5si7oqun1ixkvuw10mzcx.htm#p1i6iynmof3andn1c2w9zoyreg8h) in the SAS documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
