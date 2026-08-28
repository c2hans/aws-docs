---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/installing-sm-cli.html
---

# Installing Amazon DCV Session Manager Command Line Interface
<a name="installing-sm-cli"></a>

The Amazon DCV Session Manager Command Line Interface (CLI) is a powerful tool for managing remote desktop sessions on the Amazon DCV platform. To get started, you'll need to install the CLI on your local system. This section describes how to install the Session Manager CLI on Linux, macOS, and Windows.

**Topics**
+ [Prerequisites for installing Amazon DCV Session Manager CLI](#installing-sm-cli-prerequisites)
+ [Installing Amazon DCV Session Manager CLI](#installing-sm-cli-process)

## Prerequisites for installing Amazon DCV Session Manager CLI
<a name="installing-sm-cli-prerequisites"></a>

This section includes prerequisites for installing Amazon DCV Session Manager CLI on Linux, macOS, and Windows.

------
#### [ Linux and macOS ]
+ Python version 3.6 or later.
+ Ability to extract or unzip a downloaded, compressed file. If your operating system doesn't have the built-in `unzip` command, use an equivalent.

------
#### [ Windows ]
+ Python version 3.6 or later.
+ Python must be properly set in the PATH environment variable to run Amazon DCV Session Manager CLI using the startup script.

------

## Installing Amazon DCV Session Manager CLI
<a name="installing-sm-cli-process"></a>

This section describes the process to install Amazon DCV Session Manager CLI on Linux, macOS, and Windows.

------
#### [ Linux and macOS ]

**To Install Amazon DCV Session Manager CLI on Linux and macOS**

1. Download the zipped package from the [Amazon DCV website](http://download.amazondcv.com).

1. Unzip the downloaded package. If your Linux distribution doesn't have a built-in unzip command, use an equivalent to unzip it. The following example command unzips the package and creates a directory that's named `nice-dcv-session-manager-cli-1.0.0-37` under the current directory.

   ```
   $  unzip nice-dcv-session-manager-cli-1.0.0-37.zip
   ```

1. To validate the content of the zip file, run the following command inside the folder extracted in the previous step:

   ```
   ./dcvsm --version
   ```

------
#### [ Windows Amazon DCV server ]

**To install Amazon DCV Session Manager CLI on Windows**

1. Download the zipped package from the [Amazon DCV website](http://download.amazondcv.com).

1. Unzip the downloaded package.

1. To validate the content of the zip file, run the following command:

   ```
   C:\>  dcvsm --version
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
