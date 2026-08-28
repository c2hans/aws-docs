---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/history-pst.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Document history
<a name="history-pst"></a>

This topic describes significant changes to the documentation for the AWS Tools for PowerShell.

We also update the documentation periodically in response to customer feedback. To send feedback about a topic, use the feedback buttons next to "Did this page help you?" located at the bottom of each page.

For additional information about changes and updates to the AWS Tools for PowerShell, see the [release notes](https://aws.amazon.com/releasenotes/PowerShell). For notification about updates to this documentation, you can subscribe to an [RSS feed](https://docs.aws.amazon.com/powershell/v4/userguide/toolsforpowershell.rss).

| Change | Description | Date |
| --- |--- |--- |
| [What's new](whats-new.md) | End-of-support has been announced for V4 of the AWS Tools for PowerShell. | September 17, 2025 |
| [What's new](whats-new.md) | Version 5 (V5) of the AWS Tools for PowerShell is generally available\! For more information, see the [AWS Tools for PowerShell User Guide (V5)](https://docs.aws.amazon.com/powershell/v5/userguide/), especially the topic for [Migrating to V5](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html). | June 23, 2025 |
| [What's new](whats-new.md) | Released preview content for V5 of the AWS Tools for PowerShell. | June 13, 2025 |
| [What's new](whats-new.md) | Published the [user guide](https://docs.aws.amazon.com/powershell/v5/userguide/) for version 5 (preview) of the AWS Tools for PowerShell. | May 28, 2025 |
| [Observability](observability.md) | Announced the GA release for observability | February 10, 2025 |
| [What's new](whats-new.md) | Added information about new default behavior for integrity protection. | January 15, 2025 |
| [What's new](whats-new.md) | Added information about the first preview release of the AWS Tools for PowerShell version 5. | November 18, 2024 |
| [Pipelining, output, and iteration](pstools-pipelines.md) | Replaced content about $AWSHistory, which has been deprecated. | October 10, 2024 |
| [Observability](observability.md) | Added preview information about observability in the AWS Tools for PowerShell, which enables the gathering of telemetry data. | September 13, 2024 |
| [Installing the AWS Tools for PowerShell on Windows](pstools-getting-set-up-windows.md) | Added information about unblocking ZIP files before extracting the contents. | August 5, 2024 |
| [Information about EC2-Classic](#history-pst) | Removed information about EC2-Classic, which has been retired. | August 1, 2024 |
| [Code Examples](#history-pst) | Included a chapter with cmdlet examples. | April 17, 2024 |
| [Additional security considerations](additional-security-considerations.md) | Included information about potential logging of sensitive data. | April 16, 2024 |
| [Configure tool authentication with AWS](creds-idc.md) | Added information about support for SSO in the AWS Tools for PowerShell. | March 15, 2024 |
| [Cmdlet reference for the Tools for PowerShell](pstools-cmdlet-ref.md) | Added section with a link to the Tools for PowerShell cmdlet reference. | November 17, 2023 |
| [Included more IAM best practices updates](#history-pst) | Updated guide to align with the IAM best practices. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). | October 12, 2023 |
| [Installing on Windows](pstools-getting-set-up-windows.md) | Removed information about installing the Tools for Windows PowerShell by using the MSI, which has been deprecated. | September 25, 2023 |
| [IAM best practices updates](#history-pst) | Updated guide to align with the IAM best practices. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). | September 8, 2023 |
| [Pipelining and $AWSHistory](pstools-pipelines.md) | Added the `IncludeSensitiveData` parameter to the `Set-AWSHistoryConfiguration` cmdlet. | March 9, 2023 |
| [Using the ClientConfig parameter in cmdlets](pstools-clientconfig.md) | Added information about support for the ClientConfig parameter. | October 28, 2022 |
| [Launch an Amazon EC2 Instance Using Windows PowerShell](pstools-ec2-launch.md) | Added notes about retiring EC2-Classic. | July 26, 2022 |
| [AWS Tools for PowerShell Version 4](#history-pst) | Added information about version 4, including installation instructions for both [Windows](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-getting-set-up-windows.html) and [Linux/macOS](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-getting-set-up-linux-mac.html), and a [migration](https://docs.aws.amazon.com/powershell/v4/userguide/v4migration.html) topic that describes the differences from version 3 and introduces new features. | November 21, 2019 |
| [AWS Tools for PowerShell 3.3.563](#history-pst) | Added information about how to install and use the preview version of the `AWS.Tools.Common` module. This new module breaks apart the older monolithic package into one shared module and one module per AWS service. | October 18, 2019 |
| [AWS Tools for PowerShell 3.3.343.0](#history-pst) | Added information to the [Using the AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-using.html) section introducing the AWS Lambda Tools for PowerShell for PowerShell Core developers to build AWS Lambda functions. | September 11, 2018 |
| [AWS Tools for Windows PowerShell 3.1.31.0](#history-pst) | Added information to the [Getting Started](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-getting-started.html) section about new cmdlets that use Security Assertion Markup Language (SAML) to support configuring federated identity for users. | December 1, 2015 |
| [AWS Tools for Windows PowerShell 2.3.19](#history-pst) | Added information to the [Cmdlets Discovery and Aliases](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-discovery-aliases.html) section about the new `Get-AWSCmdletName` cmdlet that can help users more easily find their desired AWS cmdlets. | February 5, 2015 |
| [AWS Tools for Windows PowerShell 1.1.1.0](#history-pst) | Collection output from cmdlets is always enumerated to the PowerShell pipeline. Automatic support for pageable service calls. New $AWSHistory shell variable collects service responses and optionally service requests. AWSRegion instances use Region field instead of SystemName to aid pipelining. Remove-S3Bucket supports a -DeleteObjects switch option. Fixed usability issue with Set-AWSCredentials. Initialize-AWSDefaults reports from where it obtained credentials and region data. Stop-EC2Instance accepts Amazon.EC2.Model.Reservation instances as input. Generic List<T> parameter types replaced with array types (T[]). Cmdlets that delete or terminate resources prompt for confirmation prior to deletion. Write-S3Object supports in-line text content to upload to Amazon S3.  | May 15, 2013 |
| [AWS Tools for Windows PowerShell 1.0.1.0](#history-pst) | The install location of the Tools for Windows PowerShell module has changed so that environments using Windows PowerShell version 3 can take advantage of auto-loading. The module and supporting files are now installed to an `AWSPowerShell` subfolder beneath `AWS ToolsPowerShell`. Files from previous versions that exist in the `AWS ToolsPowerShell` folder are automatically removed by the installer. The `PSModulePath` for Windows PowerShell (all versions) is updated in this release to contain the parent folder of the module (`AWS ToolsPowerShell`). For systems with Windows PowerShell version 2, the Start Menu shortcut is updated to import the module from the new location and then run `Initialize-AWSDefaults`. For systems with Windows PowerShell version 3, the Start Menu shortcut is updated to remove the `Import-Module` command, leaving just `Initialize-AWSDefaults`. If you edited your PowerShell profile to perform an `Import-Module` of the `AWSPowerShell.psd1` file, you will need to update it to point to the file's new location (or, if using PowerShell version 3, remove the `Import-Module` statement as it is no longer needed). As a result of these changes, the Tools for Windows PowerShell module is now listed as an available module when executing `Get-Module -ListAvailable`. In addition, for users of Windows PowerShell version 3, the execution of any cmdlet exported by the module will automatically load the module in the current PowerShell shell without needing to use `Import-Module` first. This enables interactive use of the cmdlets on a system with an execution policy that disallows script execution. | December 21, 2012 |
| [AWS Tools for Windows PowerShell 1.0.0.0](#history-pst) | Initial release | December 6, 2012 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
