---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/storage-modules.html
---

# Storage modules
<a name="storage-modules"></a>

Storage modules create the necessary resources to allow workstations to save and retrieve data from file systems in the post production environment. The following Storage modules are available in MCS after deployment:
+ FSx for Windows File Server module - Deploys a new Amazon FSx Windows Server file system and registers to the Microsoft Active Directory
+ FSx for Lustre File Server module - Deploys a new Amazon FSx Lustre file system

**Note**
Modular Cloud Studio on AWS allows you to deploy and manage a scalable, secure, and global content production infrastructure in the cloud. This includes custom modules, developed by AWS Partners or other third parties, that you can choose to use ("Third-Party Modules"). AWS does not own or otherwise have any control over Third-Party Modules.
Your use of the Third-Party Modules is governed by any terms provided to you by the Third-Party Module providers when you acquired your license to use them (for example, their terms of service, license agreement, acceptable use policy, and privacy policy). You are responsible for ensuring that your use of the Third-Party Modules comply with any terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.
You are also responsible for making your own independent assessment of the Third-Party Modules that you use. AWS does not make any representations, warranties, or guarantees regarding the Third-Party Modules, which are "Third-Party Content" under your agreement with AWS. Modular Cloud Studio on AWS is offered to you as "AWS Content" under your agreement with AWS.

## Amazon FSx for Windows File Server module
<a name="amazon-fsx-for-windows-file-server-module"></a>

![amazon fsx for windows file server module](https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/amazon-fsx-for-windows-file-server-module.png)

1. The solution deploys the Amazon FSx for Windows File Server file system and integrates it with the Microsoft Active Directory instance deployed by the Identity module.

1. You can mount this file system manually onto workstations started by the [Leostream Broker module](workstation-management-modules.md#leostream-broker-module) module.

## Amazon FSx for Lustre File Server module
<a name="amazon-fsx-for-lustre-file-server-modules"></a>

![amazon fsx for lustre file server module](https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/amazon-fsx-for-lustre-file-server-module.png)

1. You can mount this file system manually onto workstations started by the [Leostream Broker module](workstation-management-modules.md#leostream-broker-module) module.

1. You can optionally specify an S3 Path to enable a [Data Repository Association](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-data-repositories.html) for the file system.
