---
source_url: https://docs.aws.amazon.com/lightsail/latest/userguide/troubleshooting-high-cpu-utilization.html
---

# Troubleshoot high CPU utilization for your Lightsail instance
<a name="troubleshooting-high-cpu-utilization"></a>

**Did you know?**
 You can change your instance bundle to a larger size when you create an instance from an instance snapshot. For more information, see [ Upsize a Lightsail instance, storage, or database from snapshots ](https://docs.aws.amazon.com/lightsail/latest/userguide/how-to-create-larger-instance-from-snapshot-using-console.html) .

Your instance will use all of its burst capacity if it operates in the bursting zone frequently, or for extended periods of time. This can signify that your instance is under-provisioned. It could also be that a service is running too frequently, or your instance is running unnecessary software.

Investigate what is causing your instance to burst using tools like top on Linux/Unix instances, and Task Manager on Windows Server instances. These tools show you the services that are consuming resources on your instance. Determine which services are consuming the most resources, and identify if they can be disabled without impacting the workload of your instance. By disabling services, or uninstalling software, you should be able to lower the bursting of your instance, and avoid having to up-size your instance.

If your instance is truly under-provisioned, and you cannot lower its CPU utilization, then you can mitigate burst capacity consumption by adding more processing power. You do this by creating a snapshot of your instance, and then creating a new instance from the snapshot using a larger Lightsail instance plan. For example, use the Linux or Unix-based $24 USD per month plan on your new instance instead of the Linux or Unix-based $12 USD per month plan used on the previous instance. When your new instance is up and running, make changes to your workload's DNS as necessary to swap the old instance with the new one. Delete your old under-provisioned instance after traffic starts routing to your new instance. For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
