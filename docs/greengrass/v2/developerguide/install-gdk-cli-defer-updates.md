---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/install-gdk-cli-defer-updates.html
---

# Step 1: Install the Greengrass Development Kit CLI
<a name="install-gdk-cli-defer-updates"></a>

The [Greengrass Development Kit CLI (GDK CLI)](greengrass-development-kit-cli.md) provides features that help you develop custom Greengrass components. You can use the GDK CLI to create, build, and publish custom components.

If you haven't installed the GDK CLI on your development computer, complete the following steps to install it.

**To install the latest version of the GDK CLI**

1. On your development computer, run the following command to install the latest version of the GDK CLI from its [GitHub repository](https://github.com/aws-greengrass/aws-greengrass-gdk-cli).

   ```
   python3 -m pip install -U git+https://github.com/aws-greengrass/aws-greengrass-gdk-cli.git@v1.6.2
   ```

1. <a name="gdk-cli-verify-installation"></a>Run the following command to verify that the GDK CLI installed successfully.

   ```
   gdk --help
   ```

   If the `gdk` command isn't found, add its folder to PATH.
   + On Linux devices, add `/home/{{MyUser}}/.local/bin` to PATH, and replace {{MyUser}} with the name of your user.
   + On Windows devices, add `{{PythonPath}}\\Scripts` to PATH, and replace {{PythonPath}} with the path to the Python folder on your device.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
