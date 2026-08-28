---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/pstools-welcome.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# What are the AWS Tools for PowerShell?
<a name="pstools-welcome"></a>

The AWS Tools for PowerShell are a set of PowerShell modules that are built on the functionality exposed by the AWS SDK for .NET. The AWS Tools for PowerShell enable you to script operations on your AWS resources from the PowerShell command line.

The cmdlets provide an idiomatic PowerShell experience for specifying parameters and handling results even though they are implemented using the various AWS service HTTP query APIs. For example, the cmdlets for the AWS Tools for PowerShell support PowerShell pipelining—that is, you can pipe PowerShell objects in and out of the cmdlets.

The AWS Tools for PowerShell are flexible in how they enable you to handle credentials, including support for the AWS Identity and Access Management (IAM) infrastructure. You can use the tools with IAM user credentials, temporary security tokens, and IAM roles.

The AWS Tools for PowerShell support the same set of services and AWS Regions that are supported by the SDK. You can install the AWS Tools for PowerShell on computers running Windows, Linux, or macOS operating systems.

**Note**
AWS Tools for PowerShell version 4 (V4) is a backward-compatible update to AWS Tools for PowerShell version 3.3. It adds significant improvements while maintaining existing cmdlet behavior. Your existing scripts should continue to work after upgrading to V4, but we recommend that you test them thoroughly before upgrading. For more information about the changes in V4, see [Migrating from AWS Tools for PowerShell Version 3.3 to Version 4](v4migration.md).

The AWS Tools for PowerShell are available as the following three distinct packages:
+ [`AWS.Tools`](#pwsh_structure_pstools)
+ [AWSPowerShell.NetCore](#pwsh_structure_pscore)
+ [AWSPowerShell](#pwsh_structure_psoldwin)

## Maintenance and support for SDK major versions
<a name="sdks-major-versions-maintenance-support"></a>

For information about maintenance and support for SDK major versions and their underlying dependencies, see the following in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html):
+ [AWS SDKs and tools maintenance policy](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html)
+ [AWS SDKs and tools version support matrix](https://docs.aws.amazon.com/sdkref/latest/guide/version-support-matrix.html)

## `AWS.Tools` - A modularized version of the AWS Tools for PowerShell
<a name="pwsh_structure_pstools"></a>

 [![PowerShell Gallery AWS.Tools.Installer module icon.](http://docs.aws.amazon.com/powershell/v4/userguide/images/PowerShell-Gallery-AWS.Tools.Installer-blue.png)](https://www.powershellgallery.com/packages/AWS.Tools.Installer) [![PowerShell Gallery module icon for AWS.Tools.Common.](http://docs.aws.amazon.com/powershell/v4/userguide/images/PowerShell-Gallery-AWS.Tools.Common-blue.png)](https://www.powershellgallery.com/packages/AWS.Tools.Common) [![Icon representing ZIP Archive AWS Tools, showing a folder with AWS logo.](http://docs.aws.amazon.com/powershell/v4/userguide/images/ZIP-Archive-AWS.Tools-yellow.png)](https://sdk-for-net.amazonwebservices.com/ps/v4/latest/AWS.Tools.zip)

This version of AWS Tools for PowerShell is the recommended version for any computer running PowerShell in a production environment. Because it's modularized, you need to download and load only the modules for the services you want to use. This reduces download times, memory usage, and, in most cases, enables auto-importing of `AWS.Tools` cmdlets without the need to manually call `Import-Module` first.

This is the latest version of AWS Tools for PowerShell and runs on all supported operating systems, including Windows, Linux, and macOS. This package provides one installation module, `AWS.Tools.Installer`, one common module, `AWS.Tools.Common`, and one module for each AWS service, for example, `AWS.Tools.EC2`, `AWS.Tools.IdentityManagement`, `AWS.Tools.S3`, and so on.

The `AWS.Tools.Installer` module provides cmdlets that enable you to install, update, and remove the modules for each of the AWS services. The cmdlets in this module automatically ensure that you have all the dependent modules required to support the modules you want to use.

The `AWS.Tools.Common` module provides cmdlets for configuration and authentication that are not service specific. To use the cmdlets for an AWS service, you just run the command. PowerShell automatically imports the `AWS.Tools.Common` module and the module for the AWS service whose cmdlet you want to run. This module is automatically installed if you use the `AWS.Tools.Installer` module to install the service modules.

You can install this version of AWS Tools for PowerShell on computers that are running:
+ PowerShell Core 6.0 or later on Windows, Linux, or macOS.
+ Windows PowerShell 5.1 or later on Windows with the .NET Framework 4.7.2 or later.

Throughout this guide, when we need to specify this version only, we refer to it by its module name: *`AWS.Tools`*.

## AWSPowerShell.NetCore - A single-module version of the AWS Tools for PowerShell
<a name="pwsh_structure_pscore"></a>

[![PowerShell Gallery and AWSPowerShell.NetCore module icons.](http://docs.aws.amazon.com/powershell/v4/userguide/images/PowerShell-Gallery-AWSPowerShell.NetCore-blue.png)](https://www.powershellgallery.com/packages/AWSPowerShell.NetCore/) [![ZIP Archive button next to AWSPowerShell.NetCore button.](http://docs.aws.amazon.com/powershell/v4/userguide/images/ZIP-Archive-AWSPowerShell.NetCore-yellow.png)](https://sdk-for-net.amazonwebservices.com/ps/v4/latest/AWSPowerShell.NetCore.zip)

This version consists of a single, large module that contains support for all AWS services. Before you can use this module, you must manually import it.

You can install this version of AWS Tools for PowerShell on computers that are running:
+ PowerShell Core 6.0 or later on Windows, Linux, or macOS.
+ Windows PowerShell 3.0 or later on Windows with the .NET Framework 4.7.2 or later.

Throughout this guide, when we need to specify this version only, we refer to it by its module name: *AWSPowerShell.NetCore*.

## AWSPowerShell - A single-module version for Windows PowerShell
<a name="pwsh_structure_psoldwin"></a>

[![PowerShell Gallery and AWSPowerShell module icons displayed side by side.](http://docs.aws.amazon.com/powershell/v4/userguide/images/PowerShell-Gallery-AWSPowerShell-blue.png)](https://www.powershellgallery.com/packages/AWSPowerShell/) [![Icon representing ZIP Archive with "AWSPowerShell" text label.](http://docs.aws.amazon.com/powershell/v4/userguide/images/ZIP-20Archive-AWSPowerShell-yellow.png)](https://sdk-for-net.amazonwebservices.com/ps/v4/latest/AWSPowerShell.zip)

This version of AWS Tools for PowerShell is compatible with and installable on only Windows computers that are running Windows PowerShell versions 2.0 through 5.1. It is not compatible with PowerShell Core 6.0 or later, or any other operating system (Linux or macOS). This version consists of a single, large module that contains support for all AWS services.

Throughout this guide, when we need to specify this version only, we refer to it by its module name: *AWSPowerShell*.

## How to use this guide
<a name="how-to-use-this-guide"></a>

The guide is divided into the following major sections.

** [Installing the AWS Tools for PowerShell](pstools-getting-set-up.md) **
This section explains how to install the AWS Tools for PowerShell. It includes how to sign up for AWS if you don't already have an account, and how to create an IAM user that you can use to run the cmdlets.

** [Get started with the AWS Tools for Windows PowerShell](pstools-getting-started.md) **
This section describes the fundamentals of using the AWS Tools for PowerShell, such as specifying credentials and AWS Regions, finding cmdlets for a particular service, and using aliases for cmdlets.

** [Work with AWS services in the AWS Tools for PowerShell](pstools-using.md) **
This section includes information about using the AWS Tools for PowerShell to perform some of the most common AWS tasks.

## Additional topics in this section
<a name="w2aab7c29"></a>
+ [Revision history](revision-history.md)
+ [What's new in the AWS Tools for PowerShell](whats-new.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
