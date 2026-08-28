---
source_url: https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/macos-install.html
---

# Amazon Corretto 21 Installation Instructions for macOS 11 or later
<a name="macos-install"></a>

 This topic describes how to install and uninstall Amazon Corretto 21 on a host running the Mac OS version 11 or later. You must have administrator permissions to install and uninstall Amazon Corretto 21.

## Install Amazon Corretto 21
<a name="macos-install-instruct"></a>

1.  Download the Mac `.pkg` file from the [Downloads](downloads-list.md) page.

1.  Double-click the downloaded file to begin the installation wizard and follow the steps in the wizard.

1.  Once the wizard completes, Amazon Corretto 21 is installed in `/Library/Java/JavaVirtualMachines/`.

    You can run the following command in a terminal to get the complete installation path.
**Example**

   ```
   /usr/libexec/java_home --verbose
   ```

1.  Run the following command in the terminal to set the `JAVA_HOME` variable to the Amazon Corretto 21 version of the JDK. If this was set to another version previously, it is overridden.
**Example**

   ```
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/amazon-corretto-21.jdk/Contents/Home
   ```

## Uninstall Amazon Corretto 21
<a name="macos-uninstall"></a>

You can uninstall Amazon Corretto 21 by running the following commands in a terminal.

**Example**

```
cd /Library/Java/JavaVirtualMachines/
sudo rm -rf amazon-corretto-21.jdk
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Corretto. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query corretto` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
