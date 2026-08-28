---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Linux-Server-EC2Rescue.html
---

# Troubleshoot impaired Amazon EC2 Linux instance using EC2Rescue
<a name="Linux-Server-EC2Rescue"></a>

EC2Rescue for Linux is an easy-to-use, open-source tool that can be run on an Amazon EC2 Linux instance to diagnose, troubleshoot, and remediate common issues using its library of over 100 *modules*. Modules are YAML files that contain either a BASH or a Python script and the necessary metadata.

Some generalized use cases for EC2Rescue for Linux instances include:
+ Gathering syslog and package manager logs
+ Collecting resource utilization data
+ Diagnosing and remediating known problematic kernel parameters and common OpenSSH issues

**Note**
The `AWSSupport-TroubleshootSSH` AWS Systems Manager Automation runbook installs EC2Rescue for Linux and then uses the tool to check or attempt to fix common issues that prevent an SSH connection to a Linux instance. For more information, see [AWSSupport-TroubleshootSSH](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootssh.html).

If you are using a Windows instance, see [Troubleshoot impaired Amazon EC2 Windows instance using EC2Rescue](Windows-Server-EC2Rescue.md).

**Topics**
+ [Install EC2Rescue](ec2rl_install.md)
+ [Run EC2Rescue commands](ec2rl_working.md)
+ [Develop EC2Rescue modules](ec2rl_moduledev.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
