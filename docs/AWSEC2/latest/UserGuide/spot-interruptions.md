---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html
---

# Spot Instance interruptions
<a name="spot-interruptions"></a>

You can launch Spot Instances on spare EC2 capacity for steep discounts in exchange for returning them when Amazon EC2 needs the capacity back. When Amazon EC2 reclaims a Spot Instance, we call this event a *Spot Instance interruption*.

Demand for Spot Instances can vary significantly from moment to moment, and the availability of Spot Instances can also vary significantly depending on how many unused EC2 instances are available. It is always possible that your Spot Instance might be interrupted. The following are the possible reasons that Amazon EC2 might interrupt your Spot Instances:

**Capacity**
Amazon EC2 can interrupt your Spot Instance when it needs it back. EC2 reclaims your instance mainly to repurpose capacity, but it can also occur for other reasons such as host maintenance or hardware decommission.

**Price**
The Spot price is higher than your maximum price.
You can specify the maximum price in your Spot request. However, if you specify a maximum price, your instances will be interrupted more frequently than if you do not specify it.

**Constraints**
If your Spot request includes a constraint such as a launch group or an Availability Zone group, the Spot Instances are terminated as a group when the constraint can no longer be met.

When Amazon EC2 interrupts a Spot Instance, it either terminates, stops, or hibernates the instance, depending on the interruption behavior that you specified when you created the Spot request.

**Topics**
+ [Interruption behavior](interruption-behavior.md)
+ [Prepare for interruptions](prepare-for-interruptions.md)
+ [Initiate an interruption](initiate-a-spot-instance-interruption.md)
+ [Spot Instance interruption notices](spot-instance-termination-notices.md)
+ [Find interrupted Spot Instances](finding-an-interrupted-Spot-Instance.md)
+ [Determine whether Amazon EC2 terminated a Spot Instance](BidEvictedEvent.md)
+ [Billing](billing-for-interrupted-spot-instances.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
