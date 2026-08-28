---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm-instance.html
---

# Enable or stop using NitroTPM on an Amazon EC2 instance
<a name="nitrotpm-instance"></a>

You can enable an Amazon EC2 instance for NitroTPM only at launch. After an instance is enabled for NitroTPM, you can't disable it. If you no longer need to use NitroTPM, you must configure the operating system to stop using it.

**Topics**
+ [Launch an instance with NitroTPM enabled](#launch-instance-with-nitrotpm)
+ [Stop using NitroTPM on an instance](#disable-nitrotpm-support-on-instance)

## Launch an instance with NitroTPM enabled
<a name="launch-instance-with-nitrotpm"></a>

When you launch an instance with the [ prerequisites](enable-nitrotpm-prerequisites.md), NitroTPM is automatically enabled on the instance. You can enable NitroTPM on an instance only at launch. For information about launching an instance, see [Launch an Amazon EC2 instance](LaunchingAndUsingInstances.md).

## Stop using NitroTPM on an instance
<a name="disable-nitrotpm-support-on-instance"></a>

After launching an instance with NitroTPM enabled, you can't disable NitroTPM for the instance. However, you can configure the operating system to stop using NitroTPM by disabling the TPM 2.0 device driver on the instance by using the following tools:
+ For **Linux instances**, use tpm-tools.
+ For **Windows instances**, use the TPM management console (tpm.msc).

For more information about disabling the device driver, see the documentation for your operating system.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
