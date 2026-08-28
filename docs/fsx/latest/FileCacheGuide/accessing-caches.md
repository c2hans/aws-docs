---
source_url: https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/accessing-caches.html
---

# Accessing caches
<a name="accessing-caches"></a>

In the following topics, you can learn how to access your cache on a Linux instance. In addition, you can find how to use the file `fstab` to automatically remount your cache after any system restarts.

Before you can mount a cache, you must create, configure, and launch your related AWS resources. For detailed instructions, see [Getting started with Amazon File Cache](getting-started.md).

Next, you can install and configure the Lustre client on your compute instance.

**Topics**
+ [Installing the Lustre client](install-lustre-client.md)
+ [Mounting from an Amazon EC2 instance](mounting-ec2-instance.md)
+ [Mounting from Amazon Elastic Container Service](mounting-ecs.md)
+ [Mounting caches from on-premises or a peered Amazon VPC](mounting-on-premises.md)
+ [Mounting your cache automatically](mount-fs-auto-mount-onreboot.md)
+ [Mounting specific filesets](mounting-from-fileset.md)
+ [Unmounting caches](unmounting-fs.md)
+ [Working with Amazon EC2 Spot Instances](working-with-ec2-spot-instances.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
