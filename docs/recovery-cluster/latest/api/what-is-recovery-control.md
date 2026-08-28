---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/what-is-recovery-control.html
---

# What is recovery control configuration in Amazon Application Recovery Controller (ARC)?
<a name="what-is-recovery-control"></a>

Welcome to the Recovery Control Configuration API Reference Guide for Amazon Application Recovery Controller (ARC).

With recovery control configuration in ARC, you can use extremely reliable routing control to enable you to recover applications by rerouting traffic, for example, across Availability Zones or Regions. Routing controls are simple on/off switches hosted on a ARC cluster. You integrate your routing controls with Amazon Route 53 health checks that are configured with DNS records. Then, to implement failover, you turn one routing control on and another one off to reroute traffic from one Availability Zone or AWS Region to another.

When you create routing controls, you add them to a control panel. All routing controls are grouped on control panels. You can use the default control panel that is created for each cluster, or create your own custom control panels. You must create a cluster before you can create a routing control or control panel.

After you create routing controls, you can create safety rules to put safeguards in place when you reroute traffic. Safety rules can help you avoid unintentional consequences, like turning two routing controls off at once and stopping all traffic flow.

**Important**
ARC is a global service that supports endpoints in multiple AWS Regions but you must specify the US West (Oregon) Region when you work with readiness and recovery control configuration resources, for example, to create readiness checks or routing controls. In addition, you must specify regional endpoints when you work with API cluster operations to update routing control states to reroute traffic for failover.

For more information about ARC, see the following:
+ Learn about the components in recovery control configuration, including clusters, routing controls, and control panels. For more information, see [ Recovery control components](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-components.html#introduction-components-routing) in the Amazon Application Recovery Controller Developer Guide.
+ You can set up readiness checks with ARC to ensure that your applications are scaled to handle failover traffic and configured so you can easily route around failures. For more information about the related API actions, see [Recovery Readiness API Reference Guide for Amazon Application Recovery Controller](https://docs.aws.amazon.com/recovery-readiness/latest/api/).
+ You can work with routing control states to reroute traffic for fail over. For more information about the related API actions, see [Routing Control API Reference Guide for Amazon Application Recovery Controller](https://docs.aws.amazon.com/routing-control/latest/APIReference/).
+ For more information about creating resilient applications and preparing for recovery readiness with ARC, see the [Amazon Application Recovery Controller Developer Guide](https://docs.aws.amazon.com/r53recovery/latest/dg/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
