---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-4/ug/revisions.html
---

# Revisions
<a name="revisions"></a>

For more information, see the [ CHANGELOG.md](https://github.com/aws/res/blob/mainline/CHANGELOG.md) file in the GitHub repository.

| Date | Change |
| --- | --- |
| July 2025 |  +  Release version 2025.06.01 <br />Enhancements   Improved launch time of infra hosts and default VDIs by using system default Python.   Added support for Ubuntu 24.04 VDI.   <br />Changes   Infra hosts and VDIs now use system default Python if it is available and meets RES requirements (version higher than 3.9.16).   <br />Bug Fixes   Resolved Windows and Linux VDI login issues when disable\_ad\_join is true.   Resolved an issue where custom IAM policies were not being attached to project-specific roles.     |
| June 2025 |  +  Release version 2025.06 <br />Enhancements   Added support for the AWS GovCloud (US-East) region.   Added support for g6e instance type.   Added support for launching virtual desktop sessions with Amazon Linux 2023.   Added support for launching virtual desktop sessions with Rocky Linux 9.   Added support for IAM resources prefix and path customization.   Added the ability to delete a mounted file system from the RES UI.   Added the ability to retrieve VDI bootstrap logs from Amazon CloudWatch.   Enabled hibernation for RedHat 8 and RedHat 9 VDIs.   <br />Changes   Scoped down IAM permissions for infrastructure hosts and VDI hosts.   Improved bootstrap process for infrastructure hosts and VDI hosts.   Increased the DCV broker DynamoDB tables WCU from 20 to 100.   <br />Bug Fixes   Resolved an issue where RES can fail to list Elastic Filesystem for onboarding.   Resolved an issue where RES can fail to apply snapshot caused by Elastic Filesystem listing.   Resolved an issue where DCV Console session resolution cannot be adjusted.   Resolved an issue where custom VDIs schedule can be deleted when re-saving the schedule without change.   Resolved an issue where File browser can become unresponsive with large number of users and groups in AD.   Resolved an issue where VDI sessions can be missing under Session Management.   Resolved an issue where VDI session can be missing under My Virtual Desktop page.   Resolved an issue where Idle timeout is not working for VDIs with hibernation enabled.   Resolved an issue where software stack AMIs predate older RES version.     |
| March 2025 |  +  Release version 2025.03 <br />Added sections —   [Disable a project](disable-project.md).   [Delete a project](delete-project.md).   [Cost analysis dashboard](cost-analysis-dashboard.md).   <br />Changed sections —   [Virtual desktops](virtual-desktops.md).   [Software Stacks (AMIs)](software-stacks.md).   [Configure RES-ready AMIs](res-ready-ami.md).   [Desktop settings](desktop-settings.md).   [Configuring SSH access](configuring-ssh-access.md).   [Active Directory Synchronization](active-directory-sync.md).     |
| December 2024 |  +  Release version 2024.12 <br />Added sections —   [Active Directory Synchronization](active-directory-sync.md).   [Configuring Desktop Permissions](configuring-desktop-permissions.md).   [Configuring File browser access](configuring-file-browser-access.md).   [Configuring SSH access](configuring-ssh-access.md).   [Setting up Amazon Cognito users](setting-up-cognito-users.md).   <br />Changed sections —   [Environment boundaries](permission-profiles-environment-boundaries.md).   [Configure a private VPC (optional)](prerequisites.md#private-vpc).     |
| October 2024 |  +  Release version 2024.10: Added support for —   [Environment boundaries](permission-profiles-environment-boundaries.md).   [Desktop sharing profiles](permission-profiles-desktop-sharing-profiles.md).   [Virtual desktop interface autostop](virtual-desktops-autostop.md).     |
| August 2024 |  +  Release version 2024.08: Added support for —   mounting Amazon S3 buckets to Linux Virtual Desktop Infrastructure (VDI) instances. See [Amazon S3 buckets](S3-buckets.md).   custom project permissions, an enhanced permission model that allows for customization of existing roles and the addition of custom roles. See [Permission policy](permission-profiles.md).   <br />+  User Guide: expanded the [Troubleshooting](troubleshooting.md) section.   |
| June 2024 |  +  Release version 2024.06 — Ubuntu support, Project owner permissions. <br />+  User Guide: added [Create a demo environment](create-demo-env.md)   |
| April 2024 | Release version 2024.04 — RES-ready AMIs and project launch templates |
| March 2024 | Additional troubleshooting topics, CloudWatch Logs retention, uninstall minor versions |
| February 2024 | Release version 2024.01.01 — updated deployment template |
| January 2024 | Release version 2024.01  |
| December 2023 | GovCloud directions and templates added |
|  November 2023  | Initial release |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
