---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-understanding.html
---

# Amazon EC2 Dedicated Host auto-placement and host affinity
<a name="dedicated-hosts-understanding"></a>

Placement control for Dedicated Hosts happens on both the instance level and host level.

## Auto-placement
<a name="dedicated-hosts-auto-placement"></a>

Auto-placement is configured at the host level. It allows you to manage whether instances that you launch are launched onto a specific host, or onto any available host that has matching configurations.

When auto-placement is **disabled** for a Dedicated Host, it accepts only host tenancy instance launches that specify its unique host ID. This is the default setting for new Dedicated Hosts.

When auto-placement is **enabled** for a Dedicated Host, it accepts any untargeted, host tenancy instance launches that match its instance type configuration.

When launching an instance, you need to configure its tenancy. Launching an instance onto a Dedicated Host without providing a specific `HostId` enables it to launch on any Dedicated Host that has auto-placement *enabled* and that matches its instance type.

## Host affinity
<a name="dedicated-hosts-affinity"></a>

Host affinity is configured at the instance level. It establishes a launch relationship between an instance and a Dedicated Host.

When affinity is set to `Host`, an instance launched onto a specific host always restarts on the same host if stopped. This applies to both targeted and untargeted launches.

When affinity is set to `Default`, and you stop and restart the instance, it can be restarted on any available host. However, it tries to launch back onto the last Dedicated Host on which it ran (on a best-effort basis).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
