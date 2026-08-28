---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-sas-viya-to-the-aws-cloud/assumptions-and-prerequisites.html
---

# Assumptions and prerequisites
<a name="assumptions-and-prerequisites"></a>

## Knowledge requirements
<a name="knowledge-requirements"></a>

The SAS Viya software uses containers to deploy to a Kubernetes cluster. The deployment is declarative and is based on a custom manifest that you create by using Kustomize. To deploy, update, and manage the SAS Viya software, you should have knowledge of the following:
+ Experience with the cloud provider that your site uses to deploy SAS Viya.
+ Kubernetes declarative deployments that use manifests and Kubectl.
+ Kustomize and a kustomization file to customize your deployment.
+ Kubectl commands to perform operations, such as kubectl apply, kubectl taint, kubectl label, and kubectl logs.

For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

## System requirements
<a name="system-requirements"></a>

There are many system requirements that are different from previous releases of SAS Viya. For example, SAS Viya requires Kubernetes to be deployed.

A shared file system is required for multiple purposes, including shared data storage and private user directories. A file server that uses the network file system (NFS) protocol is a minimum requirement. In an AWS environment, Amazon Elastic File System (Amazon EFS) performed well in SAS testing. The following options are recommended for Amazon EFS:
+ Set the performance mode to the maximum I/O.
+ Provision the throughput mode with 1,024 MiB/s or greater.

For more information, see [System Requirements for SAS Viya](https://documentation.sas.com/?cdcId=itopscdc&cdcVersion=default&docsetId=itopssr&docsetTarget=titlepage.htm#page=9) in the SAS documentation.

It is also assumed that you are familiar with all of the system requirements needed for a successful deployment. For more information, see [System Requirements for SAS Viya](https://documentation.sas.com/doc/en/itopscdc/v_012/itopssr/titlepage.htm).

## Full-system migration and content migration
<a name="full-system-migration-and-content-migration"></a>

**Content migration**

Content migration is defined as moving content from one system to another. Note that the SAS 9 process for this is different from the SAS Viya process.

**Full-system migration**

Full-system migration is defined as moving an entire SAS Viya system from one deployment to another. The target deployment can be either the same version or a more recent version of the software. You cannot migrate an entire SAS 9 system to SAS Viya. Instead, you must promote content from SAS 9 to SAS Viya.

If you move from SAS 9.4 to SAS Viya, you can migrate only content, which SAS considers a content migration. Migrating an entire system is considered a full-system migration. If you migrate from SAS Viya 3.x to SAS Viya, the entire system is backed up and restored, which is a full-system migration. Neither a content migration nor a full-system migration should be confused with an upgrade, which involves installing new releases of software on an existing system. Upgrade support is provided by SAS deployment tools, such as SAS Deployment Wizard, SAS Deployment Manager, and a SAS Viya playbook.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
