---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-development-kit-cli.html
---

# AWS IoT Greengrass Development Kit Command-Line Interface
<a name="greengrass-development-kit-cli"></a>

The AWS IoT Greengrass Development Kit Command-Line Interface (GDK CLI) provides features that help you develop [custom Greengrass components](develop-greengrass-components.md). You can use the GDK CLI to create, build, and publish custom components. When you create a component repository with the GDK CLI, you can start from a template or a community component from the [Greengrass Software Catalog](greengrass-software-catalog.md). Then, you can choose a build system that packages files as ZIP archives, uses a Maven or Gradle build script, or runs a custom build command. After you create a component, you can use the GDK CLI to publish it to the AWS IoT Greengrass service, so you can use the AWS IoT Greengrass console or API to deploy the component to your Greengrass core devices.

When you develop Greengrass components without the GDK CLI, you must update the version and artifact URIs in the [component recipe file](component-recipe-reference.md) each time you create a new version of the component. When you use the GDK CLI, it can automatically update the version and artifact URIs for you each time you publish a new version of the component.

The GDK CLI is open source and available on GitHub. You can customize and extend the GDK CLI to meet your component development needs. We invite you to open issues and pull requests on the GitHub repository. You can find the GDK CLI source at the following link: [https://github.com/aws-greengrass/aws-greengrass-gdk-cli](https://github.com/aws-greengrass/aws-greengrass-gdk-cli).

## Prerequisites
<a name="gdk-cli-prerequisites"></a>

To install and use the Greengrass Development Kit CLI, you need the following:
+ An AWS account. If you don't have one, see [Set up an AWS account](setting-up.md#set-up-aws-account).
+ A Windows, macOS, or Unix-like development computer with an internet connection.
+ For GDK CLI version 1.1.0 or later, [Python](https://www.python.org/downloads/) 3.6 or later installed on your development computer.

  For GDK CLI version 1.0.0, [Python](https://www.python.org/downloads/) 3.8 or later installed on your development computer.
+ [Git](https://git-scm.com/) installed on your development computer.
+ <a name="development-component-aws-cli-prerequisite"></a>AWS Command Line Interface (AWS CLI) installed and configured with credentials on your development computer. For more information, see [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *AWS Command Line Interface User Guide*.
**Note**
If you use a Raspberry Pi or another 32-bit ARM device, install AWS CLI V1. AWS CLI V2 isn't available for 32-bit ARM devices. For more information, see [Installing, updating, and uninstalling the AWS CLI version 1](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html).
+ To use the GDK CLI to publish components to the AWS IoT Greengrass service, you must have the following permissions:
  + `s3:CreateBucket`
  + `s3:GetBucketLocation`
  + `s3:PutObject`
  + `greengrass:CreateComponentVersion`
  + `greengrass:ListComponentVersions`
+ To use the GDK CLI to build a component whose artifacts exist in an S3 bucket and not in the local file system, you must have the following permissions:
  + `s3:ListBucket`

  This feature is available for GDK CLI v1.1.0 and later.

## Changelog
<a name="gdk-cli-changelog"></a>

The following table describes the changes in each version of the GDK CLI. For more information, see the [GDK CLI Releases page](https://github.com/aws-greengrass/aws-greengrass-gdk-cli/releases) on GitHub.

|  **Version**  |  **Changes**  |
| --- | --- |
| 1.6.2 |  **Bug fixes and improvements**<br />   Fixes an issue where Windows gradlew.bat does not work due to the relative path.   Minor improvements to logging, testing, and packaging.     |
| 1.6.1 |  **Bug fixes and improvements**<br />   Adds a security fix for CLI argument parsing.   Enables the GDK to get the latest Greengrass Testing Framework (GTF) release name as the default GTF version.   Enables GDK to recommend customers using an older version of GTF that they update to the latest version.     |
| 1.6.0 |  **New features**<br />   Adds a recipe validation check against the Greengrass recipe schema during the `component build` and `component publish` commands. This update helps developers to identify actionable issues within their component recipes earlier in the component creation process.   Adds a confidence test suite to the template that can be pulled down by the `test-e2e init` command. This confidence test suite includes eight generic tests that can be used and extended to fit basic component testing needs.   <br />**Bug fixes and improvements**<br />   Updates the default Greengrass Testing Framework (GTF) version used by the `test-e2e` command to version 1.2.0.     |
| 1.5.0 |  **Bug fixes and improvements**<br /> Updates the patterns recognized by the `excludes` build option when `build_system` is `zip`. This version will now recognize glob patterns which match pathnames based on their wildcard characters. This enables custom specification of which directories to exclude from.   |
| 1.4.0 |  **New features**<br />   Adds a new `config` command that starts an interactive prompt to modify fields within an existing GDK configuration file.   Modifies the `gdk component build` and `gdk component publish` commands to verify that the recipe size is within Greengrass requirements (<=16000 bytes) before proceeding.   <br />**Bug fixes and improvements**<br />   Adds additional logging in the output of the `gdk component build` command when a recipe syntax error is preventing the build from completing for awareness.   Renames the `otf-options` and `otf-version` to `gtf-options` and `gtf-version` respectively, due to the renaming of Open Test Framework to Greengrass Testing Framework.     |
| 1.3.0 |  **New features**<br />   Adds a new `test-e2e` command to support end-to-end testing of components using Open Test Framework.   Adds a new configuration option, `zip_name`, to support configurable zip file names with the zip build system.   Makes the `region` property in the GDK configuration file optional.   <br />**Bug fixes and improvements**<br />   Fixes an issue where a new directory is created even when the specified template or repository doesn't exist when initializing a GDK project with the `--name` argument.     |
| 1.2.3 |  **Bug fixes and improvements**<br />   Fixes an issues where bucket creation fails due to incorrect error handling.   Fixes an issue where list structures in the component recipe are removed.     |
| 1.2.2 |  **Bug fixes and improvements**<br />   Recipe keys are no longer case sensitive.   Adds a check to determine if a bucket exists in an AWS Region and is accessible by the user before creating a new bucket. Requires the user to have the `GetBucketLocation` permission.   Fixes an issue with the `excludes` keyword in the GDK CLI configuration file.     |
| 1.2.1 |  **Bug fixes and improvements**<br />   Accepts the Canada (Central) (`ca-central-1`) AWS Region in the region configuration entry in the `gdk-config.json` file.   Fixes issues with the `--region` GDK CLI argument to the `publish` command.     |
| 1.2.0 |  **New features**<br />   Adds the `options` entry to the `build` configuration in the GDK CLI configuration file. Supports `excludes` under `options` to exclude certain files from the zip artifact when using the `zip` build system.   Adds the `gradlew` build system to use Gradle Wrapper to build components.   Adds support for Kotlin DSL build files for the `gradle` build option.   Adds an `options` entry to the `publish` configuration in the GDK CLI configuration file. Supports the `file_upload_args` under `options` to provide extra arguments when uploading files to Amazon S3.    **Bug fixes and improvements**<br />   Fixes an issue where Gradle builds didn't clean before running a build command.   Fixes an issue where the build didn't exit when the build command fails.   Improves the output format of the `gdk component list` command.     |
| 1.1.0 |  **New features**<br />   Adds support for the Gradle [build system](gdk-cli-configuration-file.md#gdk-cli-configuration-file-build-system).   Adds support for the Maven [build system](gdk-cli-configuration-file.md#gdk-cli-configuration-file-build-system) on Windows devices.   Adds the `--bucket` argument to the [component publish](greengrass-development-kit-cli-component.md#greengrass-development-kit-cli-component-publish) command. You can use this argument to specify the exact bucket where the GDK CLI uploads component artifacts.   Adds the `--name` argument to the [component init](greengrass-development-kit-cli-component.md#greengrass-development-kit-cli-component-init) command. You can use this option to specify the folder where the GDK CLI initializes the component.   Adds support for component artifacts that exist in an S3 bucket but not in the local component build folder. You can use this feature to reduce bandwidth costs for large component artifacts, such as machine learning models.   <br />**Bug fixes and improvements**<br />   Updates the [component publish](greengrass-development-kit-cli-component.md#greengrass-development-kit-cli-component-publish) command to check if the component is built before it publishes the component. If the component isn't built, this command now [builds the component](greengrass-development-kit-cli-component.md#greengrass-development-kit-cli-component-build) for you.   Fixes an issue where the zip build system fails to build on Windows devices when the ZIP file name contains capital letters.   Improves the log message format and changes the default log level to `INFO` on devices that run Python versions earlier than 3.8.   Changes the minimum Python version requirement to Python 3.6.     |
| 1.0.0 | Initial version. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
