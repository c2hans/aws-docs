---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/getting-started-prerequisites.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Prerequisites
<a name="getting-started-prerequisites"></a>

The sections below describe the prerequisites that you must verify before you run an assessment with Toolkit for .NET Refactoring. Additional prerequisites are required for testing your application on AWS. Those prerequisites are detailed in the [Setting up for testing on AWS](setup-for-testing.md) section of this guide.

**Topics**
+ [Supported versions](#supported-versions)
+ [General prerequisites](#general-prerequisites)
+ [Memory requirements](#memory-requirements)
+ [Automatic setup](#dotnet-refactoring-automatic-setup)

## Supported versions
<a name="supported-versions"></a>

Toolkit for .NET Refactoring supports the following .NET versions.
+ Source versions:
  + .NET Framework 3.5 and later
+ Target versions:
  + .NET Core 3.1
  + .NET 5.0
  + .NET 6.0 on Microsoft Visual Studio 2022
+ The AWS test environment supports the following runtime versions:
  + .NET Core 3.1
  + .NET 5.0
  + .NET 6.0

For compatibility assessments and porting, Windows services and [ASP.NET](http://ASP.NET) applications are supported.

The following Microsoft Visual Studio versions are supported:
+ Visual Studio 2019
+ Visual Studio 2022

## General prerequisites
<a name="general-prerequisites"></a>

Before you use the Toolkit for .NET Refactoring extension, verify the following prerequisites:
+ You must have either a local machine or an Amazon EC2 instance where you will install AWS CLI, Microsoft Visual Studio, the .NET version that you want to use, and Toolkit for .NET Refactoring. For information about using a local machine versus an Amazon EC2 instance, see [AWS Identity and Access Management (IAM) overview](test-prerequisites.md#dotnet-refactoring-iam-overview) in this guide.
+ One of the following .NET versions must be installed on the local machine or Amazon EC2 instance:
  + .NET 6.0
  + .NET 5.0
  + .NET Core 3.1

  To download and install, see [Download .NET](https://dotnet.microsoft.com/download/dotnet-core) on the Microsoft website.
+ AWS CLI must be installed on the local machine or Amazon EC2 instance. Toolkit for .NET Refactoring uses information from your AWS CLI profile to determine compatibility between:
  + Public NuGet packages
  + The APIs within the NuGet packages that your application uses
  + The AWS test environment

  The extension requires a valid AWS Command Line Interface (AWS CLI) profile to collect compatibility information on the public NuGet packages and the APIs within the packages that your application uses. For more information about the application data that Toolkit for .NET Refactoring collects, see [Data collected](data-protection.md#dotnet-data-collected) in this guide.

  For information about installing the AWS CLI, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS CLI User Guide*. For information about how to configure an AWS CLI profile, see [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *AWS CLI User Guide*.
+ Microsoft Visual Studio 2019 version 16.9 or later, or Visual Studio 2022 must be installed.

## Memory requirements
<a name="memory-requirements"></a>

Use the table below to determine how much memory is required for the Toolkit for .NET Refactoring extension to run based on the solution size.

| Solution size | Minimum memory |
| --- | --- |
| Small solutions (1,000 to 50,000 lines of code) | 4 GB |
| Medium solutions (50,000 to 400,000 lines of code) | 8 GB |
| Large solutions (400,000 or more lines of code) | 16 GB or more, depending on the size of the source code |

## Automatic setup
<a name="dotnet-refactoring-automatic-setup"></a>

You can automatically perform the prerequisite steps to use Toolkit for .NET Refactoring. You can perform the setup entirely from within the tool or by using a script. Administrative or similar privileges are required for automatic setup.

**Topics**
+ [Start setup](#dotnet-refactoring-automatic-setup-start)
+ [In-tool setup](#dotnet-refactoring-automatic-setup-tool)
+ [Script setup](#dotnet-refactoring-automatic-setup-script)

### Start the automatic setup process
<a name="dotnet-refactoring-automatic-setup-start"></a>

To install Toolkit for .NET Refactoring to perform the setup, see [Install Toolkit for .NET Refactoring](dotnet-refactoring-installation.md). From the **Get Started** page, following the credential selection, select **Prerequisite Setup**. You can perform the setup for your currently selected profile and the AWS account to which it belongs. Your selected credentials can be updated.

### In-tool setup
<a name="dotnet-refactoring-automatic-setup-tool"></a>

You can perform the setup from entirely within the tool. To do so, choose **Run Setup**. The tool will make all of the required calls using your selected credentials. The response to these calls will be displayed in the output window on the right. If your selected credentials are invalid, we recommend that you try the script setup.

### Script setup
<a name="dotnet-refactoring-automatic-setup-script"></a>

Alternatively, you can perform the setup using a script. Choose **Download** to generate a .ps1 script. Run the script to perform the setup. If the user to set up has insufficient permissions, an administrator can run the generated script. Verify the contents of the script before you run it to ensure that it has not been altered.
