---
source_url: https://docs.aws.amazon.com/elemental-statmux/latest/installguide/install-sm-ig-licensing-lic-files.html
---

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Step d: Install the License Files
<a name="install-sm-ig-licensing-lic-files"></a>

Now that you have a `.tgz` compressed license file for each instance of the software you are running, you must point the software to it.

From your workstation, perform the following steps for each newly installed AWS Elemental system.

1. Navigate to the directory where you saved the `.tgz` file and unpack it.

1. Bring up the web interface for the AWS Elemental Statmux system. From the main menu, select **Settings** > **Licenses**. The Licenses screen appears.

1. Select **Choose File** and navigate to the directory where you placed the license files. Select the file name with the hostname portion matching the hostname of this node.
![Standalone License tab showing Browse button with no file selected and update option.](http://docs.aws.amazon.com/elemental-statmux/latest/installguide/images/install-installlic-shared-png.png)

1. Back on the Licenses screen, choose **Update**. The license file is installed.

1. Repeat steps 1 through 4 on each node.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Statmux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-statmux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
