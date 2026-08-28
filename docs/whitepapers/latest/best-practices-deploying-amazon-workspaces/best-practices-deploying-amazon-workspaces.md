---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/best-practices-deploying-amazon-workspaces.html
---

# Best Practices for Deploying Amazon WorkSpaces
<a name="best-practices-deploying-amazon-workspaces"></a>

Publication date: **June 1, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 This whitepaper outlines a set of best practices for the deployment of WorkSpaces. The whitepaper covers network considerations, directory services and user authentication, security, and monitoring and logging.

 This whitepaper also enables quick access to relevant information, and is intended for network engineers, directory engineers, or security engineers.

## Introduction
<a name="introduction"></a>

 [Amazon WorkSpaces](https://aws.amazon.com/workspaces/) is a managed desktop computing service in the cloud. Amazon WorkSpaces removes the burden of procuring or deploying hardware or installing complex software, and delivers a desktop experience with either a few clicks on the [AWS Management Console](https://aws.amazon.com/console/), using the Amazon Web Services (AWS) command line interface (CLI), or by using the application programming interface (API). With Amazon WorkSpaces, you can launch a Microsoft Windows or Amazon Linux desktop within minutes, which enables you to connect to and access your desktop software securely, reliably, and quickly from on-premises or from an external network. You can:
+  Leverage your existing, on-premises Microsoft Active Directory (AD) by using [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html): [Active Directory Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html) (AD Connector).
+  Extend your directory to the AWS Cloud.
+  Build a managed directory with [AWS Directory Service](https://aws.amazon.com/directoryservice/) Microsoft AD or Simple AD, to manage your users and WorkSpaces.
+  Leverage your on-premises or cloud-hosted RADIUS server with AD Connector to provide multi-factor authentication (MFA) to your WorkSpaces.

 You can automate the provisioning of Amazon WorkSpaces by using the CLI or API, which enables you to integrate Amazon WorkSpaces into your existing provisioning workflows.

 For security, in addition to the integrated network encryption that the Amazon WorkSpaces service provides, you can also enable encryption at rest for your WorkSpaces. Refer to the [Encrypted WorkSpaces](security.md#network-access-control-lists-acls) section of this document.

 You can deploy applications to your WorkSpaces by using your existing on-premises tools, such as Microsoft System Center Configuration Manager (SCCM), Puppet Enterprise, or Ansible.

 The following sections provide details about Amazon WorkSpaces, explain how the service works, describe what you need to launch the service, and tells you what options and features are available for you to use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
