---
source_url: https://docs.aws.amazon.com/linux/al2/ug/configure-ec2-instance.html
---

# Configure AL2 instances
<a name="configure-ec2-instance"></a>

After you have successfully launched and logged into your AL2 instance, you can make changes to it. There are many different ways you can configure an instance to meet the needs of a specific application. The following are some common tasks to help get you started.

**Topics**
+ [Common configuration scenarios](#instance-configuration-scenarios)
+ [Manage software on your AL2 instance](managing-software.md)
+ [Processor state control for your Amazon EC2 AL2 instance](processor_state_control.md)
+ [I/O scheduler for AL2](io-scheduler.md)
+ [Change the hostname of your AL2 instance](set-hostname.md)
+ [Set up dynamic DNS on your AL2 instance](dynamic-dns.md)
+ [Configure your network interface using ec2-net-utils for AL2](ec2-net-utils.md)

## Common configuration scenarios
<a name="instance-configuration-scenarios"></a>

The base distribution of Amazon Linux contains the software packages and utilities that are required for basic server operations. However, many more software packages are available in various software repositories, and even more packages are available for you to build from source code. For more information on installing and building software from these locations, see [Manage software on your AL2 instance](managing-software.md).

Amazon Linux instances come pre-configured with an `ec2-user`, but you may want to add other users that do not have super-user privileges. For more information on adding and removing users, see [Manage users on your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html) in the *Amazon EC2 User Guide*.

If you have your own network with a domain name registered to it, you can change the hostname of an instance to identify itself as part of that domain. You can also change the system prompt to show a more meaningful name without changing the hostname settings. For more information, see [Change the hostname of your AL2 instance](set-hostname.md). You can configure an instance to use a dynamic DNS service provider. For more information, see [Set up dynamic DNS on your AL2 instance](dynamic-dns.md).

When you launch an instance in Amazon EC2, you have the option of passing user data to the instance that can be used to perform common configuration tasks and even run scripts after the instance starts. You can pass two types of user data to Amazon EC2: cloud-init directives and shell scripts. For more information, see [Run commands on your Linux instance at launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
