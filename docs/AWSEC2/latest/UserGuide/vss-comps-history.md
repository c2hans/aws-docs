---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vss-comps-history.html
---

# AWS VSS solution version history
<a name="vss-comps-history"></a>

This page includes release notes by version for the AWS VSS component package, as well as component and script version requirements for each supported version of Windows Server.

**Topics**
+ [AwsVssComponents package versions](#AwsVssComponents-history)
+ [Windows OS version support](#windows-version-support)

## AwsVssComponents package versions
<a name="AwsVssComponents-history"></a>

The following table describes the released versions of the AWS VSS component package.

| Version | Details | Release date | Downloadable |
| --- | --- | --- | --- |
| 2.5.1 | Fixed a case where SQL database restoration could fail when the target database parameter is specified. | March 13, 2025 | Yes |
| 2.5.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vss-comps-history.html)  | January 17, 2025 | Yes |
| 2.4.0 | Added the capability to save VSS metadata files on snapshot creation. To enable this feature, see SaveVssMetadata in [Parameters for Systems Manager VSS snapshot documents](create-vss-snapshots-ssm.md#create-vss-snapshots-ssm-params). | October 7, 2024 | Yes |
| 2.3.3 | Updated the VSS agent to ensure that the `Ec2VssProvider` is used during snapshot creation. | June 25, 2024 | Yes |
| 2.3.2 | Fixed a case where VSS provider registration is not removed on uninstallation. | May 9, 2024 | Yes |
| 2.3.1 | Added new default tag `AwsVssConfig` to identify snapshots and AMIs created by AWS VSS. | March 7, 2024 | Yes |
| 2.2.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vss-comps-history.html)  | January 18, 2024 | Yes |
| 2.1.0 | Added support for using the `CreateSnapshots` API. | November 6, 2023 | Yes |
| 2.0.1 | Added support for using the WinHTTP proxy settings. | October 26, 2023 | No |
| 2.0.0 | Added capability to the AWS VSS component to create snapshots and AMIs, which enables compatibility with PowerShell module logging, script block logging, and transcription features. | April 28, 2023 | No |
| 1.3.2.0 | Fixed a case where installation failure is not reported correctly. | May 10, 2022 | No |
| 1.3.1.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vss-comps-history.html)  | February 6, 2020 | Yes |
| 1.3.00 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vss-comps-history.html)  | March 19, 2019 | No |
| 1.2.00 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vss-comps-history.html)  | November 15, 2018 | No |
| 1.1 | Fixed AWS VSS components that were being used incorrectly as the default Windows Backup and Restore provider. | December 12, 2017 | No |
| 1.0 | Initial release.  | November 20, 2017 | No |

## Windows OS version support
<a name="windows-version-support"></a>

The following table shows which AWS VSS solution versions you should run on each version of Windows Server on Amazon EC2.

| Windows Server version | AwsVssComponents version | AWSEC2-VssInstallAndSnapshot version name | AWSEC2-CreateVssSnapshot version name |
| --- | --- | --- | --- |
| Windows Server 2025 | default | default | default |
| Windows Server 2022 | default | default | default |
| Windows Server 2019 | default | default | default |
| Windows Server 2016 | default | default | default |
| Windows Server 2012 R2 | 2.1.0 | not supported | 2012R2 |
| Windows Server 2012 | 2.1.0 | not supported | 2012R2 |
| Windows Server 2008 R2 | 1.3.1.0 | not supported | 2008R2 |
