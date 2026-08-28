---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/siemens-nx-appstream/snxa-teamcenter-fsx.html
---

# Siemens NX connected to Siemens Teamcenter
<a name="snxa-teamcenter-fsx"></a>

With this architecture, you can use [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/) as a storage option for Siemens NX streamed through [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/). This architecture uses [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/) for Microsoft Active Directory and connects to Siemens Teamcenter.

![Reference architecture for Siemens NX on Amazon WorkSpaces Applications with Amazon FSx and Siemens Teamcenter.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/siemens-nx-appstream/images/siemens-nx-architecture-diagram-ra-2.png)

The following steps describe the architecture:

1. Directory Service for Microsoft Active Directory manages users, computers, and storage as Amazon FSx. Amazon WorkSpaces Applications can then join the domain as configured in Active Directory. Authorized users in Active Directory can access WorkSpaces Applications sessions.

1. Amazon FSx replicates across multiple Availability Zones and is accessible in an WorkSpaces Applications session. You can configure user folders and shared folders in Amazon FSx by using Active Directory Group Policy access.

1. Single sign-in is established through federation of Active Directory SAML 2.0 with Auth0.

1. Siemens NX streams through WorkSpaces Applications and communicates through the Amazon VPC peer to Siemens Teamcenter running on another VPC.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Reference Architecture Diagrams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query reference-architecture-diagrams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
